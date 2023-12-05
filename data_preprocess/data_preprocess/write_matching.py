import os

# 根据数据集路径改data_path, 其他参数不需要改
# data_path = '210705'

sub_name = ['train', 'val', 'test']
# formulas = '../../images/' + data_path + '/formulas/'
formulas = r'C:\Users\Aurora\Desktop\LaTeX_OCR_PRO-master\data\formulas'
match_path = r'C:\Users\Aurora\Desktop\LaTeX_OCR_PRO-master\data\matching'
# if not os.path.isdir(r'C:\Users\Aurora\Desktop\LaTeX_OCR_PRO-master\data\matching'):
#     os.mkdir(r'D:\dataset1\output' + r'\matching')



for sn in sub_name:
    match = match_path + '\\' + sn + '.matching.txt'
    with open(formulas + '\\' + sn + '.formulas.norm.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    size = len(lines)
    for i in range(size):
        with open(match, 'a', encoding='utf-8') as f:
            fileName = str(i) + '.png'
            f.write(fileName + ' ' + str(i) + '\n')
