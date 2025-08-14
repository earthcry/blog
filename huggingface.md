


## HuggingFace Usage

'''
# setup linux env var; set mirror url
echo 'export HF_ENDPOINT="https://hf-mirror.com"' >> ~/.bashrc
source ~/.bashrc

# install depend; huggingface_hub client;
pip install huggingface_hub --upgrade
1. hfd.sh
use arsa2,

./hfd.sh username/repo-name 

./hfd.sh username/repo-name  --include filename

2. huggingface-cli
# 多线程下载
huggingface-cli download username/modelname --num-workers=3

# if error: command not found: huggingface-cli
echo "export PATH=\"`python3 -m site --user-base`/bin:\$PATH\"" >> ~/.bashrc
source ~/.bashrc

# 断点续传
huggingface-cli download username/modelname --resume-download

# download models
huggingface-cli download --resume-download model-name --local-dir ~/models --local-dir-use-symlinks false

# multi-download datasets
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






### models for whisper+ on android
https://hf-mirror.com/DocWolle/whisperOnnx/tree/main

./hfd DocWolle/whisperOnnx --include whisper_small_int8.zip


### models files for rtranslate on android
https://github.com/niedev/RTranslator/releases/tag/2.0.0

https://github.com/niedev/RTranslator/releases/download/2.0.0/NLLB_cache_initializer.onnx


    An_RTranslator_2.0.0.apk <https://github.com/niedev/RTranslator/
    releases/download/2.0.0/An_RTranslator_2.0.0.apk>
    94.7 MB 2024-06-16T20:01:40Z

    NLLB_cache_initializer.onnx <https://github.com/niedev/RTranslator/
    releases/download/2.0.0/NLLB_cache_initializer.onnx>
    24.2 MB 2024-06-16T14:11:47Z

    NLLB_decoder.onnx <https://github.com/niedev/RTranslator/releases/
    download/2.0.0/NLLB_decoder.onnx>
    171 MB 2024-06-16T14:12:05Z

    NLLB_embed_and_lm_head.onnx <https://github.com/niedev/RTranslator/
    releases/download/2.0.0/NLLB_embed_and_lm_head.onnx>
    500 MB 2024-06-16T14:14:07Z

    NLLB_encoder.onnx <https://github.com/niedev/RTranslator/releases/
    download/2.0.0/NLLB_encoder.onnx>
    254 MB 2024-06-16T14:20:34Z

    Whisper_cache_initializer.onnx <https://github.com/niedev/
    RTranslator/releases/download/2.0.0/Whisper_cache_initializer.onnx>
    13.7 MB 2024-06-16T14:23:40Z

    Whisper_cache_initializer_batch.onnx <https://github.com/niedev/
    RTranslator/releases/download/2.0.0/
    Whisper_cache_initializer_batch.onnx>
    13.7 MB 2024-06-16T14:23:49Z

    Whisper_decoder.onnx <https://github.com/niedev/RTranslator/
    releases/download/2.0.0/Whisper_decoder.onnx>
    173 MB 2024-06-16T14:25:01Z

    Whisper_detokenizer.onnx <https://github.com/niedev/RTranslator/
    releases/download/2.0.0/Whisper_detokenizer.onnx>
    461 KB 2024-06-16T14:23:57Z

    Whisper_encoder.onnx <https://github.com/niedev/RTranslator/
    releases/download/2.0.0/Whisper_encoder.onnx>
    88.2 MB 2024-06-16T14:23:58Z

    Whisper_initializer.onnx <https://github.com/niedev/RTranslator/
    releases/download/2.0.0/Whisper_initializer.onnx>
    69.7 KB 2024-06-16T14:25:01Z





