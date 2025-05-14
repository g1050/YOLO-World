## 准备 YOLO-World 的数据

### 概览

为了预训练 YOLO-World，我们采用了以下表格中列出的几个数据集：

| 数据 | 样本数 | 类型 | 盒数 |
| :-- | :-----: | :---:| :---: | 
| Objects365v1 | 609k | detection | 9,621k |
| GQA | 621k | grounding | 3,681k |
| Flickr | 149k | grounding | 641k |
| CC3M-Lite | 245k | image-text | 821k |
 
### 数据集目录

We put all data into the `data` directory, such as:  
我们将所有数据放在 `data` 目录中，例如：

```bash
├── coco
│   ├── annotations
│   ├── lvis
│   ├── train2017
│   ├── val2017
├── flickr
│   ├── annotations
│   └── images
├── mixed_grounding
│   ├── annotations
│   ├── images
├── mixed_grounding
│   ├── annotations
│   ├── images
├── objects365v1
│   ├── annotations
│   ├── train
│   ├── val
```
**NOTE**: We strongly suggest that you check the directories or paths in the dataset part of the config file, especially for the values `ann_file`, `data_root`, and `data_prefix`.  
**注意**: 我们强烈建议您检查配置文件数据集部分中的目录或路径，特别是 `ann_file`、`data_root` 和 `data_prefix` 这些值。  

We provide the annotations of the pre-training data in the below table:  
我们在下面的表格中提供了预训练数据的标注：  

| Data | images | Annotation File |
| :--- | :------| :-------------- |
| Objects365v1 | [`Objects365 train`](https://opendatalab.com/OpenDataLab/Objects365_v1) | [`objects365_train.json`](https://opendatalab.com/OpenDataLab/Objects365_v1) |
| MixedGrounding | [`GQA`](https://nlp.stanford.edu/data/gqa/images.zip) | [`final_mixed_train_no_coco.json`](https://huggingface.co/GLIPModel/GLIP/tree/main/mdetr_annotations/final_mixed_train_no_coco.json) |
| Flickr30k | [`Flickr30k`](https://shannon.cs.illinois.edu/DenotationGraph/) |[`final_flickr_separateGT_train.json`](https://huggingface.co/GLIPModel/GLIP/tree/main/mdetr_annotations/final_flickr_separateGT_train.json) |
| LVIS-minival | [`COCO val2017`](https://cocodataset.org/) | [`lvis_v1_minival_inserted_image_name.json`](https://huggingface.co/GLIPModel/GLIP/blob/main/lvis_v1_minival_inserted_image_name.json) |

**Acknowledgement:** We sincerely thank [GLIP](https://github.com/microsoft/GLIP) and [mdetr](https://github.com/ashkamath/mdetr) for providing the annotation files for pre-training.  
**致谢:** 我们衷心感谢 [GLIP](https://github.com/microsoft/GLIP) 和 [mdetr](https://github.com/ashkamath/mdetr) 提供预训练的标注文件。  


### 数据集类别

> 对于在封闭集对象检测上微调 YOLO-World，推荐使用 `MultiModalDataset`。

#### 设置类别/分类

如果您使用 `COCO格式` 的自定义数据集，您“不需要”定义一个用于自定义词汇/分类的数据集类别。
在配置文件中通过 `metainfo=dict(classes=your_classes),` 明确设置类别是简单的：

```python

coco_train_dataset = dict(
    _delete_=True,
    type='MultiModalDataset',
    dataset=dict(
        type='YOLOv5CocoDataset',
        metainfo=dict(classes=your_classes),
        data_root='data/your_data',
        ann_file='annotations/your_annotation.json',
        data_prefix=dict(img='images/'),
        filter_cfg=dict(filter_empty_gt=False, min_size=32)),
    class_text_path='data/texts/your_class_texts.json',
    pipeline=train_pipeline)
```


For training YOLO-World, we mainly adopt two kinds of dataset classs:  
对于训练 YOLO-World，我们主要采用两种数据集类：  

#### 1. `MultiModalDataset`

`MultiModalDataset` is a simple wrapper for pre-defined Dataset Class, such as `Objects365` or `COCO`, which add the texts (category texts) into the dataset instance for formatting input texts.  
`MultiModalDataset` 是一个预定义数据集类的简单包装器，比如 `Objects365` 或 `COCO`，它将文本（类别文本）添加到数据集实例中以格式化输入文本。  

**Text JSON**

The json file is formatted as follows:

```json
[
    ['A_1','A_2'],
    ['B'],
    ['C_1', 'C_2', 'C_3'],
    ...
]
```

We have provided the text json for [`LVIS`](./../data/texts/lvis_v1_class_texts.json), [`COCO`](../data/texts/coco_class_texts.json), and [`Objects365`](../data/texts/obj365v1_class_texts.json)

#### 2. `YOLOv5MixedGroundingDataset`

The `YOLOv5MixedGroundingDataset` extends the `COCO` dataset by supporting loading texts/captions from the json file. It's desgined for `MixedGrounding` or `Flickr30K` with text tokens for each object.  
`YOLOv5MixedGroundingDataset` 通过支持从 json 文件加载文本/描述来扩展 `COCO` 数据集。它专为 `MixedGrounding` 或 `Flickr30K` 设计，每个对象都带有文本标记。  



### 🔥 自定义数据集

对于自定义数据集，我们建议用户根据使用情况转换注释文件。请注意，将注释转换为**标准的COCO格式**基本上是必需的。

1. **大词汇量、定位、引用：** 您可以遵循`MixedGrounding`数据集的注释格式，该格式为每个对象添加了`caption`和`tokens_positive`以分配文本。文本可以是一个类别或名词短语。

2. **自定义词汇（固定）：** 您可以采用`MultiModalDataset`包装器，如`Objects365`，并为您的自定义类别创建一个**文本json**。


### CC3M 伪标注

以下标注是根据我们论文中的自动标注过程生成的。并且我们根据这些标注报告了结果。

要使用 CC3M 标注，您首先需要准备 `CC3M` 图像。

| Data | Images | Boxes | File |
| :--: | :----: | :---: | :---: |
| CC3M-246K | 246,363 | 820,629 | [Download 🤗](https://huggingface.co/wondervictor/YOLO-World/blob/main/cc3m_pseudo_annotations.json) |
| CC3M-500K | 536,405 | 1,784,405| [Download 🤗](https://huggingface.co/wondervictor/YOLO-World/blob/main/cc3m_pseudo_500k_annotations.json) |
| CC3M-750K | 750,000 | 4,504,805 | [Download 🤗](https://huggingface.co/wondervictor/YOLO-World/blob/main/cc3m_pseudo_750k_annotations.json) |