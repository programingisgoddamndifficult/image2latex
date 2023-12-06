import numpy as np

import tensorflow as tf2
tf = tf2.compat.v1
tf.disable_v2_behavior()
GRUCell = tf.nn.rnn_cell.GRUCell
LSTMCell = tf.nn.rnn_cell.LSTMCell


from .components.positional import add_timing_signal_nd


class Encoder(object):
    """Class with a __call__ method that applies convolutions to an image"""

    def __init__(self, config):
        self._config = config


    def __call__(self, img, dropout):
        """Applies convolutions to the image
        Args:
            img: batch of img, shape = (?, height, width, channels), of type tf.uint8
            tf.uint8 因为 2^8 = 256，所以元素值区间 [0, 255]，线性压缩到 [-1, 1] 上就是 img = (img - 128) / 128
        Returns:
            the encoded images, shape = (?, h', w', c')
        """
        with tf.variable_scope("Encoder"):
            img = tf.cast(img, tf.float32) - 128.
            img = img / 128.

            with tf.variable_scope("convolutional_encoder"):
                # conv + max pool -> /2
                # 64 个 3*3 filters, strike = (1, 1), output_img.shape = ceil(L/S) = ceil(input/strike) = (H, W)
                out = tf.layers.conv2d(img, 64, 3, 1, "SAME", activation=tf.nn.relu)
                image_summary("out_1_layer", out)
                out = tf.layers.max_pooling2d(out, 2, 2, "SAME")

                # conv + max pool -> /2
                out = tf.layers.conv2d(out, 128, 3, 1, "SAME", activation=tf.nn.relu)
                image_summary("out_2_layer", out)
                out = tf.layers.max_pooling2d(out, 2, 2, "SAME")

                # regular conv -> id
                out = tf.layers.conv2d(out, 256, 3, 1, "SAME", activation=tf.nn.relu)
                image_summary("out_3_layer", out)
                out = tf.layers.conv2d(out, 256, 3, 1, "SAME", activation=tf.nn.relu)
                image_summary("out_4_layer", out)
                if self._config.encoder_cnn == "vanilla":
                    out = tf.layers.max_pooling2d(out, (2, 1), (2, 1), "SAME")

                out = tf.layers.conv2d(out, 512, 3, 1, "SAME", activation=tf.nn.relu)
                image_summary("out_5_layer", out)
                if self._config.encoder_cnn == "vanilla":
                    out = tf.layers.max_pooling2d(out, (1, 2), (1, 2), "SAME")

                if self._config.encoder_cnn == "cnn":
                    # conv with stride /2 (replaces the 2 max pool)
                    out = tf.layers.conv2d(out, 512, (2, 4), 2, "SAME")

                # conv
                out = tf.layers.conv2d(out, 512, 3, 1, "VALID", activation=tf.nn.relu)
                image_summary("out_6_layer", out)
                if self._config.positional_embeddings:
                    # from tensor2tensor lib - positional embeddings
                    # 嵌入位置信息（positional）
                    # 后面将会有一个 flatten 的过程，会丢失掉位置信息，所以现在必须把位置信息嵌入
                    # 嵌入的方法有很多，比如加，乘，缩放等等，这里用 tensor2tensor 的实现
                    out = add_timing_signal_nd(out)
                    image_summary("out_7_layer", out)
        return out

def image_summary(name_scope, tensor):
    with tf.variable_scope(name_scope):
        tf.summary.image("{}_{}".format(name_scope,0), tf.expand_dims(tf.expand_dims(tensor[0,:,:,0], 0), -1))
        # 磁盘炸了，只可视化一个
        # filter_count = tensor.shape[3]
        # for i in range(filter_count):
        #     tf.summary.image("{}_{}".format(name_scope,i), tf.expand_dims(tensor[:,:,:,i], -1))
            # tf.expand_dims(tensor[:,:,:,i], -1)
            # Tensor must be 4-D with last dim 1, 3, or 4, not [50,320], so we need to use expand_dims
