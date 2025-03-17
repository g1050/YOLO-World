<div align="center">
<img src="./assets/yolo_logo.png" width=60%>
<br>
<a href="https://scholar.google.com/citations?hl=zh-CN&user=PH8rJHYAAAAJ">Tianheng Cheng</a><sup><span>2,3,*</span></sup>, 
<a href="https://linsong.info/">Lin Song</a><sup><span>1,📧,*</span></sup>,
<a href="https://yxgeee.github.io/">Yixiao Ge</a><sup><span>1,🌟,2</span></sup>,
<a href="http://eic.hust.edu.cn/professor/liuwenyu/"> Wenyu Liu</a><sup><span>3</span></sup>,
<a href="https://xwcv.github.io/">Xinggang Wang</a><sup><span>3,📧</span></sup>,
<a href="https://scholar.google.com/citations?user=4oXBp9UAAAAJ&hl=en">Ying Shan</a><sup><span>1,2</span></sup>
</br>

\* Equal contribution 🌟 Project lead 📧 Corresponding author

<sup>1</sup> Tencent AI Lab,  <sup>2</sup> ARC Lab, Tencent PCG
<sup>3</sup> Huazhong University of Science and Technology
<br>
<div>

[![arxiv paper](https://img.shields.io/badge/Project-Page-green)](https://wondervictor.github.io/)
[![arxiv paper](https://img.shields.io/badge/arXiv-Paper-red)](https://arxiv.org/abs/2401.17270)
<a href="https://colab.research.google.com/github/AILab-CVC/YOLO-World/blob/master/inference.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
[![demo](https://img.shields.io/badge/🤗HugginngFace-Spaces-orange)](https://huggingface.co/spaces/stevengrove/YOLO-World)
[![Replicate](https://replicate.com/zsxkib/yolo-world/badge)](https://replicate.com/zsxkib/yolo-world)
[![hfpaper](https://img.shields.io/badge/🤗HugginngFace-Paper-yellow)](https://huggingface.co/papers/2401.17270)
[![license](https://img.shields.io/badge/License-GPLv3.0-blue)](LICENSE)
[![yoloworldseg](https://img.shields.io/badge/YOLOWorldxEfficientSAM-🤗Spaces-orange)](https://huggingface.co/spaces/SkalskiP/YOLO-World)
[![yologuide](https://img.shields.io/badge/📖Notebook-roboflow-purple)](https://supervision.roboflow.com/develop/notebooks/zero-shot-object-detection-with-yolo-world)
[![deploy](https://media.roboflow.com/deploy.svg)](https://inference.roboflow.com/foundation/yolo_world/)

</div>
</div>

## Notice

**YOLO-World is still under active development!**

We recommend that everyone **use English to communicate on issues**, as this helps developers from around the world discuss, share experiences, and answer questions together.

For business licensing and other related inquiries, don't hesitate to contact `yixiaoge@tencent.com`.

## 🔥 更新 
`[2025-2-8]:` 我们发布了新的 YOLO-World-V2.1，包括新的预训练权重和图像提示的训练代码。请查看 [YOLO-World-V2.1博客](./docs/update_20250123.md) 获取详细信息。\
`[2024-11-5]`: 我们更新了 `YOLO-World-Image`，您可以在 HuggingFace [YOLO-World-Image（预览版）](https://huggingface.co/spaces/wondervictor/YOLO-World-Image) 尝试它。这是一个*预览*版本，我们仍在改进中！关于训练和少量样本推理的详细文档即将发布。\
`[2024-7-8]`: YOLO-World 现已集成到 [ComfyUI](https://github.com/StevenGrove/ComfyUI-YOLOWorld) 中！快来尝试将 YOLO-World 添加到您的工作流程中！您可以在 [StevenGrove/ComfyUI-YOLOWorld](https://github.com/StevenGrove/ComfyUI-YOLOWorld) 访问它！\
`[2024-5-18]:` YOLO-World 模型已与 FiftyOne 计算机视觉工具包集成，用于跨图像和视频数据集的流畅开放词汇推理。\
`[2024-5-16]:` 嘿，大家好！好久不见！此次更新包含 (1) [微调指南](https://github.com/AILab-CVC/YOLO-World?#highlights--introduction) 和 (2) [TFLite 导出](./docs/tflite_deploy.md) 与 INT8 量化。\
`[2024-5-9]:` 此次更新包含真正的 [`重新参数化`](./docs/reparameterize.md) 🪄，它更适合在自定义数据集上进行微调，并提高了训练/推理效率 🚀！\
`[2024-4-28]:` 好久不见！此次更新包含错误修复和改进：(1) ONNX 演示；(2) 图像演示（支持张量输入）；(3) 新的预训练模型；(4) 图像提示；(5) 微调/部署的简化版本；(6) 安装指南（包括 `requirements.txt`）。\
`[2024-3-28]:` 我们提供：(1) 更多高分辨率的预训练模型（例如 S、M、X）([#142](https://github.com/AILab-CVC/YOLO-World/issues/142))；(2) 带有 CLIP-Large 文本编码器的预训练模型。最重要的是，我们初步修复了**没有 `mask-refine` 的微调**并探索了新的微调设置 ([#160](https://github.com/AILab-CVC/YOLO-World/issues/160),[#76](https://github.com/AILab-CVC/YOLO-World/issues/76))。此外，使用 `mask-refine` 微调 YOLO-World 也取得了显著改进，更多详情请查看 [configs/finetune_coco](./configs/finetune_coco/)。\
`[2024-3-16]:` 我们修复了关于演示的错误 ([#110](https://github.com/AILab-CVC/YOLO-World/issues/110),[#94](https://github.com/AILab-CVC/YOLO-World/issues/94),[#129](https://github.com/AILab-CVC/YOLO-World/issues/129), [#125](https://github.com/AILab-CVC/YOLO-World/issues/125))，包括分割掩码的可视化，并发布了支持提示调整、文本提示和图像提示的 [**YOLO-World with Embeddings**](./docs/prompt_yolo_world.md)。\
`[2024-3-3]:` 我们添加了**高分辨率 YOLO-World**，支持 `1280x1280` 分辨率，具有更高的准确性和对小物体的更好性能！\
`[2024-2-29]:` 我们发布了最新版本的 [**YOLO-World-v2**](./docs/updates.md)，具有更高的准确性和更快的速度！我们希望社区能加入我们，共同改进 YOLO-World！\
`[2024-2-28]:` 激动地宣布 YOLO-World 已被 **CVPR 2024** 接受！我们将继续使 YOLO-World 更快更强，同时使其更易于使用。\
`[2024-2-22]:` 我们衷心感谢 [RoboFlow](https://roboflow.com/) 和 [@Skalskip92](https://twitter.com/skalskip92) 制作的关于 YOLO-World 的 [**视频指南**](https://www.youtube.com/watch?v=X7gKBGVz4vs)，干得好！\
`[2024-2-18]:` 我们感谢 [@Skalskip92](https://twitter.com/skalskip92) 通过连接 YOLO-World 和 EfficientSAM 开发了精彩的分割演示。您现在可以在 [🤗 HuggingFace Spaces](https://huggingface.co/spaces/SkalskiP/YOLO-World) 尝试它。\
`[2024-2-17]:` YOLO-World 最大的模型 **X** 已发布，实现了更好的零样本性能！\
`[2024-2-17]:` 我们现在发布了 **YOLO-World-Seg** 的代码和模型！YOLO-World 现在支持开放词汇/零样本对象分割！\
`[2024-2-15]:` 发布了带有 CC3M-Lite 的预训练 YOLO-World-L！\
`[2024-2-14]:` 我们提供了用于图像或目录推理的 [`image_demo`](demo.py)。\
`[2024-2-10]:` 我们提供了用于在 COCO 数据集或自定义数据集上微调 YOLO-World 的 [微调](./docs/finetuning.md) 和 [数据](./docs/data.md) 详情！\
`[2024-2-3]:` 我们现在支持在仓库中的 `Gradio` 演示，您可以在自己的设备上构建 YOLO-World 演示！\
`[2024-2-1]:` 我们现在已发布 YOLO-World 的代码和权重！\
`[2024-2-1]:` 我们在 [HuggingFace 🤗](https://huggingface.co/spaces/stevengrove/YOLO-World) 上部署了 YOLO-World 演示，您现在可以尝试它！\
`[2024-1-31]:` 我们很兴奋地推出 **YOLO-World**，这是一款尖端的实时开放词汇对象检测器。


## TODO

YOLO-World is under active development and please stay tuned ☕️! 
If you have suggestions📃 or ideas💡,**we would love for you to bring them up in the [Roadmap](https://github.com/AILab-CVC/YOLO-World/issues/109)** ❤️!
> YOLO-World 目前正在积极开发中📃，如果你有建议或者想法💡，**我们非常希望您在 [Roadmap](https://github.com/AILab-CVC/YOLO-World/issues/109) 中提出来** ❤️！

## [FAQ (Frequently Asked Questions)](https://github.com/AILab-CVC/YOLO-World/discussions/149)

We have set up an FAQ about YOLO-World in the discussion on GitHub. We hope everyone can raise issues or solutions during use here, and we also hope that everyone can quickly find solutions from it.

> 我们在GitHub的discussion中建立了关于YOLO-World的常见问答，这里将收集一些常见问题，同时大家可以在此提出使用中的问题或者解决方案，也希望大家能够从中快速寻找到解决方案


## Highlights & Introduction

本仓库包含了YOLO-World的PyTorch实现、预训练权重以及预训练/微调代码。  
This repo contains the PyTorch implementation, pre-trained weights, and pre-training/fine-tuning code for YOLO-World.

* YOLO-World在包括检测、定位和图像-文本数据集的大规模数据集上进行了预训练。  
* YOLO-World is pre-trained on large-scale datasets, including detection, grounding, and image-text datasets.

* YOLO-World是下一代YOLO检测器，具有强大的开放词汇检测能力和定位能力。  
* YOLO-World is the next-generation YOLO detector, with a strong open-vocabulary detection capability and grounding ability.

* YOLO-World提出了一个高效的用户词汇推理范式——*先提示后检测*，它将词汇嵌入作为参数重新参数化到模型中，实现了卓越的推理速度。您可以在我们的[在线演示](https://huggingface.co/spaces/stevengrove/YOLO-World)中尝试导出您自己的检测模型，无需额外训练或微调！  
* YOLO-World presents a *prompt-then-detect* paradigm for efficient user-vocabulary inference, which re-parameterizes vocabulary embeddings as parameters into the model and achieve superior inference speed. You can try to export your own detection model without extra training or fine-tuning in our [online demo](https://huggingface.co/spaces/stevengrove/YOLO-World)!


<div align="center">
<img width=800px src="./assets/yolo_arch.png">
</div>

### Zero-shot Evaluation Results for Pre-trained Models
我们以零样本方式在LVIS、LVIS-mini和COCO上评估所有YOLO-World-V2.1模型，并与前一版本进行比较（改进点以上标形式标注）。  
We evaluate all YOLO-World-V2.1 models on LVIS, LVIS-mini, and COCO in the zero-shot manner, and compare with the previous version (the improvements are annotated in the superscripts).


<table>
    <tr>
        <th rowspan="2">Model</th><th rowspan="2">Resolution</th><th colspan="4" style="border-right: 1px solid">LVIS AP</th><th colspan="4">LVIS-mini</th><th colspan="4" style="border-left: 1px solid">COCO</th>
    </tr>
        <td>AP</td><td>AP<sub>r</sub></td><td>AP<sub>c</sub></td><td style="border-right: 1px solid">AP<sub>f</sub></td><td>AP</td><td>AP<sub>r</sub></td><td>AP<sub>c</sub></td><td>AP<sub>f</sub></td><td style="border-left: 1px solid">AP</td><td>AP<sub>50</sub></td><td>AP<sub>75</sub></td>
    <tr style="border-top: 2px solid">
        <td>YOLO-World-S</td><td>640</td><td>18.5<sup>+1.2</sup></td><td>12.6</td><td>15.8</td><td style="border-right: 1px solid">24.1</td><td>23.6<sup>+0.9</sup></td><td>16.4</td><td>21.5</td><td>26.6</td><td style="border-left: 1px solid">36.6</td><td>51.0</td><td>39.7</td>
    </tr>
    <tr>
        <td>YOLO-World-S</td><td>1280</td><td>19.7<sup>+0.9</sup></td><td>13.5</td><td>16.3</td><td style="border-right: 1px solid">26.3</td><td>25.5<sup>+1.4</sup></td><td>19.1</td><td>22.6</td><td>29.3</td><td style="border-left: 1px solid">38.2</td><td>54.2</td><td>41.6</td>
    </tr>
    <tr style="border-top: 2px solid">
        <td>YOLO-World-M</td><td>640</td><td>24.1<sup>+0.6</sup></td><td>16.9</td><td>21.1</td><td style="border-right: 1px solid">30.6</td><td>30.6<sup>+0.6</sup></td><td>19.7</td><td>29.0</td><td>34.1</td><td style="border-left: 1px solid">43.0</td><td>58.6</td><td>46.7</td>
    </tr>
    <tr>
        <td>YOLO-World-M</td><td>1280</td><td>26.0<sup>+0.7</sup></td><td>19.9</td><td>22.5</td><td style="border-right: 1px solid">32.7</td><td>32.7<sup>+1.1</sup></td><td>24.4</td><td>30.2</td><td>36.4</td><td style="border-left: 1px solid">43.8</td><td>60.3</td><td>47.7</td>
    </tr>
    <tr style="border-top: 2px solid">
        <td>YOLO-World-L</td><td>640</td><td>26.8<sup>+0.7</sup></td><td>19.8</td><td>23.6</td><td style="border-right: 1px solid">33.4</td><td>33.8<sup>+0.9</sup></td><td>24.5</td><td>32.3</td><td>36.8</td><td style="border-left: 1px solid">44.9</td><td>60.4</td><td>48.9</td>
    </tr>
    <tr>
        <td>YOLO-World-L</td><td>800</td><td>28.3</td><td>22.5</td><td>24.4</td><td style="border-right: 1px solid">35.1</td><td>35.2</td><td>27.8</td><td>32.6</td><td>38.8</td><td style="border-left: 1px solid">47.4</td><td>63.3</td><td>51.8</td>
    </tr>
    <tr>
        <td>YOLO-World-L</td><td>1280</td><td>28.7<sup>+1.1</sup></td><td>22.9</td><td>24.9</td><td style="border-right: 1px solid">35.4</td><td>35.5<sup>+1.2</sup></td><td>24.4</td><td>34.0</td><td>38.8</td><td style="border-left: 1px solid">46.0</td><td>62.5</td><td>50.0</td>
    </tr>
    <tr style="border-top: 2px solid">
        <td>YOLO-World-X</td><td>640</td><td>28.6<sup>+0.2</sup></td><td>22.0</td><td>25.6</td><td style="border-right: 1px solid">34.9</td><td>35.8<sup>+0.4</sup></td><td>31.0</td><td>33.7</td><td>38.5</td><td style="border-left: 1px solid">46.7</td><td>62.5</td><td>51.0</td>
    </tr>
    <tr>
        <td colspan="13">YOLO-World-X-1280 is coming soon.</td>
    </tr>
</table>

### Model Card

<table>
    <tr>
        <th>Model</th><th>Resolution</th><th>Training</th><th>Data</th><th>Model Weights</th>
    </tr>
    <tr style="border-top: 2px solid">
        <td>YOLO-World-S</td><td>640</td><td>PT (100e)</td><td>O365v1+GoldG+CC-LiteV2</td><td><a href="https://huggingface.co/wondervictor/YOLO-World-V2.1/resolve/main/x_stage1-62b674ad.pth"> 🤗 HuggingFace</a></td>
    </tr>
    <tr>
        <td>YOLO-World-S</td><td>1280</td><td>CPT (40e)</td><td>O365v1+GoldG+CC-LiteV2</td><td><a href="https://huggingface.co/wondervictor/YOLO-World-V2.1/resolve/main/s_stage2-4466ab94.pth"> 🤗 HuggingFace</a></td>
    </tr>
    <tr style="border-top: 2px solid">
        <td>YOLO-World-M</td><td>640</td><td>PT (100e)</td><td>O365v1+GoldG+CC-LiteV2</td><td><a href="https://huggingface.co/wondervictor/YOLO-World-V2.1/resolve/main/m_stage1-7e1e5299.pth"> 🤗 HuggingFace</a></td>
    </tr>
    <tr>
        <td>YOLO-World-M</td><td>1280</td><td>CPT (40e)</td><td>O365v1+GoldG+CC-LiteV2</td><td><a href="https://huggingface.co/wondervictor/YOLO-World-V2.1/resolve/main/m_stage2-9987dcb1.pth"> 🤗 HuggingFace</a></td>
    </tr>
    <tr style="border-top: 2px solid">
        <td>YOLO-World-L</td><td>640</td><td>PT (100e)</td><td>O365v1+GoldG+CC-LiteV2</td><td><a href="https://huggingface.co/wondervictor/YOLO-World-V2.1/resolve/main/l_stage1-7d280586.pth"> 🤗 HuggingFace</a></td>
    </tr>
    <tr>
        <td>YOLO-World-L</td><td>800 / 1280</td><td>CPT (40e)</td><td>O365v1+GoldG+CC-LiteV2</td><td><a href="https://huggingface.co/wondervictor/YOLO-World-V2.1/resolve/main/l_stage2-b3e3dc3f.pth"> 🤗 HuggingFace</a></td>
    </tr>
    <tr style="border-top: 2px solid">
        <td>YOLO-World-X</td><td>640</td><td>PT (100e)</td><td>O365v1+GoldG+CC-LiteV2</td><td><a href="https://huggingface.co/wondervictor/YOLO-World-V2.1/resolve/main/x_stage1-62b674ad.pth"> 🤗 HuggingFace</a></td>
    </tr>
</table>

**Notes:**
* PT: Pre-training, CPT: continuing pre-training
* CC-LiteV2: the newly-annotated CC3M subset, including 250k images.


## Getting started

### 1. Installation

YOLO-World is developed based on `torch==1.11.0` `mmyolo==0.6.0` and `mmdetection==3.0.0`. Check more details about `requirements` and `mmcv` in [docs/installation](./docs/installation.md).

#### Clone Project 

```bash
git clone --recursive https://github.com/AILab-CVC/YOLO-World.git
```
#### Install

```bash
# 安装 torch 和 wheel 包，-q 参数表示安静模式，即减少不必要的输出
pip install torch wheel -q
# 安装当前目录下的项目，-e 参数表示以开发模式安装，允许你修改代码并立即看到更改
pip install -e .
```

### 2. Preparing Data

We provide the details about the pre-training data in [docs/data](./docs/data.md).


## Training & Evaluation

我们采用 [mmyolo](https://github.com/open-mmlab/mmyolo) 的默认[训练](./tools/train.py)或[评估](./tools/test.py)脚本。  
We adopt the default [training](./tools/train.py) or [evaluation](./tools/test.py) scripts of [mmyolo](https://github.com/open-mmlab/mmyolo).  
我们在 `configs/pretrain` 和 `configs/finetune_coco` 提供了预训练和微调的配置。  
We provide the configs for pre-training and fine-tuning in `configs/pretrain` and `configs/finetune_coco`.  
训练 YOLO-World 很简单：  
Training YOLO-World is easy:  

```bash
chmod +x tools/dist_train.sh
# sample command for pre-training, use AMP for mixed-precision training
./tools/dist_train.sh configs/pretrain/yolo_world_l_t2i_bn_2e-4_100e_4x8gpus_obj365v1_goldg_train_lvis_minival.py 8 --amp
```
**NOTE:** YOLO-World is pre-trained on 4 nodes with 8 GPUs per node (32 GPUs in total). For pre-training, the `node_rank` and `nnodes` for multi-node training should be specified. 

Evaluating YOLO-World is also easy:

```bash
chmod +x tools/dist_test.sh
./tools/dist_test.sh path/to/config path/to/weights 8
```

**NOTE:** We mainly evaluate the performance on LVIS-minival for pre-training.

## Fine-tuning YOLO-World

<div align="center">
<img src="./assets/finetune_yoloworld.png" width=800px>
</div>


<div align="center">
<b><p>Chose your pre-trained YOLO-World and Fine-tune it!</p></b> 
</div>


YOLO-World 支持**零样本推理**，以及三种类型的**微调配方**：**(1) 常规微调**，**(2) 提示微调**，和**(3) 重参数化微调**。
YOLO-World supports **zero-shot inference**, and three types of **fine-tuning recipes**: **(1) normal fine-tuning**, **(2) prompt tuning**, and **(3) reparameterized fine-tuning**.  

* 常规微调：我们在 [docs/fine-tuning](./docs/finetuning.md) 提供了有关 YOLO-World 微调的详细信息。
* Normal Fine-tuning: we provide the details about fine-tuning YOLO-World in [docs/fine-tuning](./docs/finetuning.md).

* 提示微调：我们在 [docs/prompt_yolo_world](./docs/prompt_yolo_world.md) 提供了更多关于提示微调的详细信息。
* Prompt Tuning: we provide more details about prompt tuning in [docs/prompt_yolo_world](./docs/prompt_yolo_world.md).

* 重参数化微调：重参数化的 YOLO-World 更适合于远离通用场景的特定领域。您可以在 [docs/reparameterize](./docs/reparameterize.md) 中找到更多详细信息。
* Reparameterized Fine-tuning: the reparameterized YOLO-World is more suitable for specific domains far from generic scenes. You can find more details in [docs/reparameterize](./docs/reparameterize.md).

## Deployment

We provide the details about deployment for downstream applications in [docs/deployment](./docs/deploy.md).
You can directly download the ONNX model through the online [demo](https://huggingface.co/spaces/stevengrove/YOLO-World) in Huggingface Spaces 🤗.

- [x] ONNX export and demo: [docs/deploy](https://github.com/AILab-CVC/YOLO-World/blob/master/docs/deploy.md)
- [x] TFLite and INT8 Quantization: [docs/tflite_deploy](https://github.com/AILab-CVC/YOLO-World/blob/master/docs/tflite_deploy.md)
- [ ] TensorRT: coming soon.
- [ ] C++: coming soon.

## Demo

See [`demo`](./demo) for more details

- [x] `gradio_demo.py`: Gradio demo, ONNX export
- [x] `image_demo.py`: inference with images or a directory of images
- [x] `simple_demo.py`: a simple demo of YOLO-World, using `array` (instead of path as input).
- [x] `video_demo.py`: inference YOLO-World on videos.
- [x] `inference.ipynb`: jupyter notebook for YOLO-World.
- [x] [Google Colab Notebook](https://colab.research.google.com/drive/1F_7S5lSaFM06irBCZqjhbN7MpUXo6WwO?usp=sharing): We sincerely thank [Onuralp](https://github.com/onuralpszr) for sharing the [Colab Demo](https://colab.research.google.com/drive/1F_7S5lSaFM06irBCZqjhbN7MpUXo6WwO?usp=sharing), you can have a try 😊！

## Acknowledgement

We sincerely thank [mmyolo](https://github.com/open-mmlab/mmyolo), [mmdetection](https://github.com/open-mmlab/mmdetection), [GLIP](https://github.com/microsoft/GLIP), and [transformers](https://github.com/huggingface/transformers) for providing their wonderful code to the community!

## Citations
If you find YOLO-World is useful in your research or applications, please consider giving us a star 🌟 and citing it.

```bibtex
@inproceedings{Cheng2024YOLOWorld,
  title={YOLO-World: Real-Time Open-Vocabulary Object Detection},
  author={Cheng, Tianheng and Song, Lin and Ge, Yixiao and Liu, Wenyu and Wang, Xinggang and Shan, Ying},
  booktitle={Proc. IEEE Conf. Computer Vision and Pattern Recognition (CVPR)},
  year={2024}
}
```

## Licence
YOLO-World is under the GPL-v3 Licence and is supported for commercial usage. If you need a commercial license for YOLO-World, please feel free to contact us.
