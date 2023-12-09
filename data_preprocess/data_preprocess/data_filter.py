# Created: 210313 14:02
# Last edited: 210421 14:02 

import os
import shutil

# 循环处理train、test、val三个目录
name_list = [r'\train', r'\test', r'\val']
input_label_dir = "D:\\dataset2\\output\\labels"
output_label_dir = "D:\\dataset2\\output\\labels1"
# if not os.path.exists(output_label_dir):
#     os.mkdir(output_label_dir)

for name in name_list:
    label_name_list = os.listdir(input_label_dir + name)
    for label_name in label_name_list:
        # 标签文件源路径
        label_src_path = input_label_dir + name + '\\' + label_name
        # 标签文件目标路径
        label_dst_path = output_label_dir + name + '\\' + label_name

        with open(label_src_path, 'r', encoding='utf-8') as f1:
            # 筛除多行的label.txt
            lines = f1.readlines()
            print(lines)
            if len(lines) > 1:
                print(lines[1])
                continue

            # 筛除error mathpix
            content = f1.read()
            if 'error mathpix' in content:
                print(content)
                continue

        # 若无错误，则将源标签文件复制至目标标签文件中
        shutil.copy(label_src_path, label_dst_path)