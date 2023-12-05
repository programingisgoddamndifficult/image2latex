import os
import random
import shutil

# shuffle
# input_dir = r'D:\dataset1\output\labels'
# output_dir = r'D:\dataset1\output\formulas'
# image_input_dir = r'D:\dataset1\output\images'
# image_output_dir = r'D:\dataset1\output\images1'
#
# train_label_name_list = os.listdir(image_input_dir + '\\' + 'train')
# test_label_name_list = os.listdir(image_input_dir + '\\' + 'test')
# val_label_name_list = os.listdir(image_input_dir + '\\' + 'val')
#
# train_num = len(train_label_name_list)
# test_num = len(test_label_name_list)
# val_num = len(val_label_name_list)



# for i in range(train_num):
#     img_name = train_label_name_list[i]
#     img_path = image_input_dir + '\\' + img_name
#     shutil.copy(image_input_dir + '\\' + img_name, image_output_dir + r'\train' + '\\' + img_name)
#
# for i in range(test_num):
#     img_name = test_label_name_list[i][:-4] + '.png'
#     img_path = r'D:\dataset1\output\images\test' + '\\' + img_name
#     shutil.copy(image_input_dir + '\\' + img_name, image_output_dir + r'\test' + '\\' + img_name)

# for i in range(train_num):
#     img_name = train_label_name_list[i]
#     img_src_path = image_input_dir + r'\train' + '\\' + img_name
#     img_dst_path = image_output_dir + r'\train' + '\\' + str(i) + '.png'
#     shutil.copy(img_src_path, img_dst_path)

# for i in range(test_num):
#     img_name = test_label_name_list[i]
#     img_src_path = image_input_dir + r'\test' + '\\' + img_name
#     img_dst_path = image_output_dir + r'\test' + '\\' + str(i) + '.png'
#     shutil.copy(img_src_path, img_dst_path)
#
# for i in range(val_num):
#     img_name = val_label_name_list[i]
#     img_src_path = image_input_dir + r'\val' + '\\' + img_name
#     img_dst_path = image_output_dir + r'\val' + '\\' + str(i) + '.png'
#     shutil.copy(img_src_path, img_dst_path)

# for i in range(total_num):
#     if i < train_num:
#         shutil.copy(input_dir + r'\total' + '\\' + total_label_name_list[i], input_dir + r'\train' + '\\' + total_label_name_list[i])
#     else:
#         shutil.copy(input_dir + r'\total' + '\\' + total_label_name_list[i], input_dir + r'\test' + '\\' + total_label_name_list[i])

'''
    生成norm.txt
'''

input_dir = r'D:\dataset1\output\labels'
output_dir = r'D:\dataset1\output\formulas'
image_input_dir = r'D:\dataset1\output\images'

train_label_name_list = os.listdir(input_dir + '\\' + 'train')
test_label_name_list = os.listdir(input_dir + '\\' + 'test')
val_label_name_list = os.listdir(input_dir + '\\' + 'val')

train_num = len(train_label_name_list)
test_num = len(test_label_name_list)
val_num = len(val_label_name_list)

with open(output_dir + '\\' + 'train.formulas.norm.txt', 'w', encoding='utf-8') as f1:
    for i in range(train_num):
        train_label_name = train_label_name_list[i]
        with open(input_dir + r'\train' + '\\' + train_label_name, 'r', encoding='utf-8') as f2:
            line = f2.read()
            f1.write(line + '\n')

with open(output_dir + '\\' + 'val.formulas.norm.txt', 'w', encoding='utf-8') as f1:
    for i in range(val_num):
        val_label_name = val_label_name_list[i]
        with open(input_dir + r'\val' + '\\' + val_label_name, 'r', encoding='utf-8') as f2:
            line = f2.read()
            f1.write(line + '\n')

with open(output_dir + '\\' + 'test.formulas.norm.txt', 'w', encoding='utf-8') as f1:
    for i in range(test_num):
        test_label_name = test_label_name_list[i]
        with open(input_dir + r'\images_test' + '\\' + test_label_name, 'r', encoding='utf-8') as f2:
            line = f2.read()
            f1.write(line + '\n')

# shuffle end
