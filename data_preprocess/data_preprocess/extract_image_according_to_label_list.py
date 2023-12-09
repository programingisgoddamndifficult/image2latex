import os
import shutil

name_list = [r'\train', r'\test', r'\val']

label_input = r'D:\dataset2\output\labels2'
label_output = r'D:\dataset2\output\labels3'

image_input = r'D:\dataset2\output\images'
image_output = r'D:\dataset2\output\images1'

for name in name_list:
    image_src_path = image_input + name
    image_dst_path = image_output + name

    label_src_path = label_input + name
    label_dst_path = label_output + name

    label_name_list = os.listdir(label_src_path)

    for i in range(len(label_name_list)):
        label_name_list[i] = label_name_list[i][:-4]

    num = 0
    for label_name in label_name_list:
        print(label_name)
        shutil.copy(image_src_path + '\\' + label_name + '.png', image_dst_path + '\\' + str(num) + '.png')
        shutil.copy(label_src_path + '\\' + label_name + '.txt', label_dst_path + '\\' + str(num) + '.txt')
        num += 1

