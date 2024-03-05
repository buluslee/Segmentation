import os

# 定义原始图片文件夹和目标图片文件夹
original_folder = r"D:\Codes\deeplabv3-plus-pytorch-main\VOCdevkit\VOC2007\SegmentationClass_Origin"
target_folder = r"D:\Codes\deeplabv3-plus-pytorch-main\VOCdevkit\VOC2007\SegmentationClass"

# 遍历所有图片文件
for i in range(7921):
    # 构建原始图片路径和目标图片路径
    original_path = os.path.join(original_folder, f"{i:05d}.jpg")
    target_path = os.path.join(target_folder, f"{i:05d}.png")
    
    # 将jpg后缀改为png，并保存
    os.rename(original_path, target_path)
