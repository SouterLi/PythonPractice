import os

# 读取环境变量
api_key = os.environ.get('DEEPSEEK_API_KEY')

# 验证输出
if api_key:
    print(f"✅ 环境变量配置成功！API Key（部分隐藏）：{api_key[:6]}****{api_key[-4:]}")
else:
    print("❌ 未读取到环境变量，请检查配置！")


import sys
import torch

# 1. 查看Python版本
print("Python版本：", sys.version)
# 2. 查看PyTorch版本
print("PyTorch版本：", torch.__version__)
# 3. 验证CUDA调用（核心）
print("CUDA是否可用：", torch.cuda.is_available())
# 4. 简单张量运算（验证基础功能）
x = torch.tensor([1.0, 2.0]).cuda()
y = x * 2
print("GPU张量运算结果：", y)