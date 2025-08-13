# list_Whisper_models.py 
from huggingface_hub import HfApi
import time
 
api = HfApi()
 
def list_whisper_models():
    print("查找 Whisper 相关模型：")
    print("-" * 50)
    
    try:
        # 添加更多筛选条件以减少结果数量
        models = api.list_models(
            search="whisper",
            limit=50,  # 限制返回结果数量
        )
        
        for model in models:
            print(f"模型名称: {model.id}")
            print(f"下载量: {model.downloads}")
            print(f"是否量化: {'是' if model.tags and 'quantized' in model.tags else '否'}")
            print(f"模型大小: {model.siblings[0].size if model.siblings else '未知'} bytes")
            print("-" * 50)
            
            # 添加延迟避免请求过快
            time.sleep(0.1)
            
    except Exception as e:
        print(f"获取模型列表时出错: {str(e)}")
 
if __name__ == "__main__":
    list_whisper_models()
