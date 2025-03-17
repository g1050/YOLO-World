lvis 数据集  
```
{
    "info": {...},
    "licenses": [...],
    "categories": [...],
    "images": [...],
    "annotations": [...]
}
```

info  
```
{'year': 2020, 'version': '1', 'description': 'LVIS 2020 Dataset', 'contributor': 'Agrim Gupta, Piotr Dollar, Ross Girshick', 'url': 'http://lvisdataset.org'}
```

"categories":   
```
[
    {
        "id": 1,
        "name": "airplane",
        "supercategory": "vehicle"
    },
    {
        "id": 2,
        "name": "apple",
        "supercategory": "fruit"
    }
]
```

"images":   
```
[
    {
        "id": 12345,
        "width": 640,
        "height": 480,
        "file_name": "image_12345.jpg",
        "coco_url": "http://images.cocodataset.org/train2017/image_12345.jpg",
        "date_captured": "2021-08-01"
    }
]
```

"annotations":    
```
[
    {
        "id": 1001,
        "image_id": 12345,
        "category_id": 2,
        "segmentation": [[...]],
        "bbox": [x, y, width, height],
        "area": 23456,
        "iscrowd": 0
    }
]
```

# lvis数据集

1203类别，长尾分布
