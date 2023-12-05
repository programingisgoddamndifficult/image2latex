import os
import random
import shutil

'''
    1、划分数据集
'''
# 读取原有train的数据并随机打乱
original_train = r'D:\dataset1\train'
original_train_label_list = os.listdir(original_train + r'\labels')
random.shuffle(original_train_label_list)

output_label_dir = r'D:\dataset1\output\labels'
output_image_dir = r'D:\dataset1\output\images'
output_file = r'D:\dataset1\outputfile'

# 分割原有train数据集, 并将数据集中的数据按顺序命名
total_num = len(original_train_label_list)
train_num = 0.78 * total_num
test_num = total_num - train_num
print(total_num)
for i in range(total_num):
    if i < train_num:
        shutil.copy(original_train + r'\labels' + '\\' + original_train_label_list[i], output_label_dir + r'\train' +
                    '\\' + str(i) + '.txt')
        shutil.copy(original_train + r'\images' + '\\' + original_train_label_list[i], output_image_dir + r'\train' +
                    '\\' + str(i) + '.png')
    else:
        shutil.copy(original_train + r'\labels' + '\\' + original_train_label_list[i], output_label_dir + r'\test' +
                    '\\' + str(i - train_num) + '.txt')
        shutil.copy(original_train + r'\images' + '\\' + original_train_label_list[i], output_image_dir + r'\test' +
                    '\\' + str(i - train_num) + '.png')

# 单独处理验证集
val_label_list = os.listdir(r'D:\dataset1\val' + r'\labels')
val_num = len(val_label_list)
for i in range(test_num):
    shutil.copy(r'D:\dataset1\val\labels' + '\\' + val_label_list[i], output_label_dir + r'\val' +
                '\\' + str(i) + '.txt')
    shutil.copy(r'D:\dataset1\val\labels' + '\\' + val_label_list[i], output_image_dir + r'\val' +
                '\\' + str(i) + '.png')

# train_path = r'D:\dataset1\output\labels'
# val_path = r'D:\dataset1\output\labels'
# test_path = r'D:\dataset1\test'
#
# train_labels = os.listdir(train_path + r'\train')
# train_images = os.listdir(r'D:\dataset1\train\images')
# val_labels = os.listdir(val_path + r'\val')
# val_images = os.listdir(r'D:\dataset1\val\images')
# test_images = os.listdir(test_path + r'\images')
#
#
# train_labels_num = len(train_labels)
# val_labels_num = len(val_labels)
# test_images_num = len(test_images)

# print(train_labels_num)
# print(val_labels_num)


# for i in range(total_num):
#     if i < train_num:
#         train_list.append(label_name_list[i])
#     elif i < train_num + val_num:
#         val_list.append(label_name_list[i])
#     else:
#         test_list.append(label_name_list[i])


with open(output_file, 'w', encoding='utf-8') as f0:
    index = 0
    with open(output_dir + "\\" + 'im2latex_train_filter.lst', 'w', encoding='utf-8') as f1:
        for i in range(train_labels_num):
            print(index, end='\r')
            train_label_name = train_labels[i]
            # print(train_label_name)
            image_name = train_label_name[0:-4] + '.png'
            if image_name in train_images:
                f1.write(image_name + ' ' + str(index) + '\n')
                # shutil.copy(image_input_dir + image_name, image_output_dir + 'images_train/' + str(i) + '.png')
                with open(input_dir + r'\train' + '\\' + train_label_name, 'r', encoding='utf-8') as f2:
                    line = f2.read()
                    f0.write(line + '\n')
                index += 1

    with open(output_dir + "\\" + 'im2latex_validate_filter.lst', 'w', encoding='utf-8') as f1:
        for i in range(val_labels_num):
            print(index, end='\r')
            val_label_name = val_labels[i]
            image_name = val_label_name[0:-4] + '.png'
            if image_name in val_images:
                f1.write(image_name + ' ' + str(index) + '\n')
                # shutil.copy(image_input_dir + image_name, image_output_dir + 'images_val/' + str(i) + '.png')
                with open(input_dir +  r'\val' + "\\" + val_label_name, 'r', encoding='utf-8') as f2:
                    line = f2.read()
                    f0.write(line + '\n')
                index += 1

    # with open(output_dir + 'im2latex_test_filter.lst', 'w', encoding='utf-8') as f1:
    #     for i in range(test_num):
    #         print(index, end='\r')
    #         test_label_name = test_list[i]
    #         image_name = test_label_name[:-4] + '.png'
    #         if image_name in image_name_list:
    #             f1.write(image_name + ' ' + str(index) + '\n')
    #             # shutil.copy(image_input_dir + image_name, image_output_dir + 'images_test/' + str(i) + '.png')
    #             with open(input_dir + test_label_name, 'r', encoding='utf-8') as f2:
    #                 line = f2.read()
    #                 f0.write(line + '\n')
    #             index += 1
    


# shuffle end