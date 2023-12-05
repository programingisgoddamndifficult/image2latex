import os
import shutil
import random

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