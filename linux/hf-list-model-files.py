from huggingface_hub import list_repo_files
 
# 默认设置
DEFAULT_SAVE_DIR = "/home/nu/data2025/ai"
DEFAULT_REPO = "openai/whisper"
 
# 输入仓库名
print(f"仓库格式示例: {DEFAULT_REPO}")
input_repo = input(f"请输入模型仓库名: ").strip()
REPO_MODEL = input_repo if input_repo else DEFAULT_REPO
 
# 将仓库名中的 / 替换为 --
SAVE_DIR = f"{DEFAULT_SAVE_DIR}/{REPO_MODEL.replace('/', '--')}"
 
# 获取文件列表并生成命令
files = list_repo_files(REPO_MODEL)
 
print("\n# 创建下载目录")
print(f"mkdir -p {SAVE_DIR}")
print()
 
for file in files:
   # 跳过含有 original/ 或 .git 的文件
   if 'original/' in file or '.git' in file:
       continue
       
   cmd = f"huggingface-cli download {REPO_MODEL} {file} --local-dir {SAVE_DIR}"
   #print(f"# 下载 {file}")
   print(cmd)
   #print()
