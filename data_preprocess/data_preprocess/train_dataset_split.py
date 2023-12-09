import shutil
import os
import math

image_input_path = r"D:\dataset2\output\images1\train"
image_output_path = r"D:\dataset2\output\images1\train\train_split"
label_input_path = r"D:\dataset2\output\labels3\train"
label_output_path = r"D:\dataset2\output\labels3\train_split"

os.mkdir(image_output_path)
os.mkdir(label_output_path)

total_train_label = os.listdir(label_input_path)

max_image_num = 1600
cur_image_num = 0
dataset_num = math.ceil(len(total_train_label) / max_image_num)

for i in range(dataset_num):
    image_path = image_output_path + r'\train' + str(i + 1)
    label_path = label_output_path + r'\train' + str(i + 1)
    os.makedirs(image_path)
    os.makedirs(label_path)
    begin_index = i * max_image_num
    end_index = min((i + 1)*max_image_num, len(total_train_label))
    cur_image_num = 0
    for label in total_train_label[begin_index:end_index]:
        label_src_path = label_input_path + "\\" + label
        label_dst_path = label_path + "\\" + str(cur_image_num) + '.txt'
        shutil.copy(label_src_path, label_dst_path)

        image_src_path = image_input_path + "\\" + label[:-4] + '.png'
        image_dst_path = image_path + "\\" + str(cur_image_num) + '.png'
        shutil.copy(image_src_path, image_dst_path)

        cur_image_num += 1

'''
    生成norm.txt与matching.txt
'''

input_dir = label_output_path + r'\train'
output_dir = r"D:\dataset2\output\formulas"
match_path = r'D:\dataset2\output\matching'

for i in range(20):
    train_path = input_dir + str(i + 1)
    with open(output_dir + '\\' + 'train' + str(i + 1) + '.formulas.norm.txt', 'w', encoding='utf-8') as f1:
        train_label_list = os.listdir(train_path)
        train_label_num = len(train_label_list)
        for j in range(train_label_num):
            train_label_name = train_label_list[j]
            with open(train_path + '\\' + str(j) + ".txt", 'r', encoding='utf-8') as f2:
                line = f2.read()
                f1.write(line + '\n')

    match = match_path + '\\' + 'train' + str(i + 1) + '.matching.txt'
    with open(output_dir + '\\' + 'train' + str(i + 1) + '.formulas.norm.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    size = len(lines)
    for k in range(size):
        with open(match, 'a', encoding='utf-8') as f:
            fileName = str(k) + '.png'
            f.write(fileName + ' ' + str(k) + '\n')
