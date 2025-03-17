# coco格式的测试集转yolo格式
# <class_id> <x_center> <y_center> <width> <height>
import json
import os
import sys
# 路径
json_path = sys.argv[1]  # 你的 COCO/LVIS JSON
labels_dir = sys.argv[2]  # YOLO 格式标签存放目录
os.makedirs(labels_dir, exist_ok=True)

# 读取 JSON 数据
with open(json_path, "r") as f:
    data = json.load(f)

# 读取类别 ID
categories = {cat["id"]: i for i, cat in enumerate(data["categories"])}  # 从0开始索引
# cocoID：index
# print(categories)

name = []
for i, cat in enumerate(data["categories"]):
    print(f"{cat['id']}:{cat['name']}")
    name.append(cat['name'])
yaml_path = os.path.join(labels_dir, f"data.yaml")
with open(yaml_path, "w") as yaml_file:
    yaml_file.write(f"nc: {len(name)}\n")
    yaml_file.write(f"name: {name}\n")

# 处理每张图片的标注
for image in data["images"]:
    image_id = image["id"]
    width, height = image["width"], image["height"]
    file_name = os.path.splitext(os.path.basename(image["file_name"]))[0]
    label_path = os.path.join(labels_dir, f"{file_name}.txt")
    
    with open(label_path, "w") as label_file:
        for ann in data["annotations"]:
            if ann["image_id"] == image_id:
                category_id = categories[ann["category_id"]]  # 类别索引
                x, y, w, h = ann["bbox"]
                # 归一化
                x_center, y_center = (x + w / 2) / width, (y + h / 2) / height
                w, h = w / width, h / height
                label_file.write(f"{category_id} {x_center} {y_center} {w} {h}\n")

# todo:上面的实现低效，遍历所有的标注然后去找某张图