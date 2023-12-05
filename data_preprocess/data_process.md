

# 自己写的：数据划分(dataset_split.py)

1. 已知数据被划分为train、test、val三个集合，且每个集合均有图像与标签。
2. 将源数据的train按照7:2的比例划分成新的train与test。
2. 将train、test、val三个数据集中的标签与图片均按顺序命名



# 执行data_preprocess中的文件

1. **dataset_split.py**：实现数据划分
1. **data_filter.py**：过滤缺失/错误的label；
2. **extract_image_according_to_label_list.py**，根据标签使图像对齐；
3. **fmm.py**，根据公式生成vocab.txt与cn_vocab.txt（个人理解，因为词汇表不一定完整）
4. **shuffle_and_build_dataset.py**：生成.norm.txt
4. **write_matching.py**：生成.matching.txt