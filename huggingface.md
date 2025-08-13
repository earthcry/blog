


# HuggingFace Usage

'''
# setup linux env var; set mirror url
export HF_ENDPOINT=https://hf-mirror.com
source ~/.bashrc

# install depend; huggingface_hub client;
pip install huggingface_hub --upgrade

# 多线程下载
huggingface-cli download username/modelname --num-workers=3

# if error: command not found: huggingface-cli
echo "export PATH=\"`python3 -m site --user-base`/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc

# 断点续传
huggingface-cli download username/modelname --resume-download

# download models
huggingface-cli download --resume-download model-name --local-dir ~/models --local-dir-use-symlinks false

# multi-download datas
huggingface-cli download repo-type dataset --resume-download wikitext --local-dir wikitext

# cache_dir vs local_dir
参数       | 默认值 |存储位置 | 遵循HF缓存结构 | 自动复用 |
cache_dir   ~/.cache/huggingface/hub   Y             Y
local_dir      no     usercustom         No            NO

特点：
- 文件存储在标准HF缓存结构中
- 可以被其他HF工具识别复用
- 路径结构示例：
--- 源于CSDN.NET/hdu顶级牛马

长期用：cache_dir
临时用：local_dir

大文件下载：
huggingface-cli download username/modelname \
    --resume-download \
    --num-workers=3 \
    --cache-dir="~/hf_cache"

下载中断后如何继续？
huggingface-cli download username/modelname --resume-download

# Shell
huggingface-cli download --repo-type dataset --token [你的token] --resume-download [数据集名称] --cache-dir [/本地路径] --local-dir-use-symlinks False

'''


list-models-name.py
list-model-files.py





