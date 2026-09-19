import torch

print("CUDA可用:", torch.cuda.is_available())
print("如果可用，当前设备:", torch.cuda.get_device_name(0))
