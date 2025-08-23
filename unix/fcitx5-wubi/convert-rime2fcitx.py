#!/bin/python3

import pandas as pd
 
# 读取原始数据
df = pd.read_csv('wubi06_tygfhzb.dict', sep='\t', header=None)  # 假设数据用制表符分隔，没有列名
 
# 交换列，例如将第一列和第二列交换
cols = list(df.columns)
cols[0], cols[1] = cols[1], cols[0]  # 交换列的索引
df = df[cols]
 
# 将结果写入新文件
df.to_csv('fcitx5-table-wubi06.txt', sep='\t', header=False, index=False)  # 假设用制表符分隔，不写入列名和索引
#df.to_csv('new.txt', sep=' ', header=False, index=False)  # 假设用制表符分隔，不写入列名和索引






'''
import csv
 
# 打开原始文件和输出文件
with open('原始文件.txt', newline='', encoding='utf-8') as infile, \
     open('输出文件.txt', 'w', newline='', encoding='utf-8') as outfile:
    reader = csv.reader(infile, delimiter='\t')  # 假设数据用制表符分隔
    writer = csv.writer(outfile, delimiter='\t')
    
    for row in reader:
        if row:  # 确保行不为空
            # 交换行中的两列，例如第一列和第二列
            row[0], row[1] = row[1], row[0]
            writer.writerow(row)


'''






