# 0.摘要
Abstract
You Only Look Once (YOLO) 系列探测器已经证明了它们是高效且实用的工具。You Only Look Once (YOLO) series of detectors have established themselves as efficient and practical tools.

然而，它们对预定义和训练过的对象类别的依赖限制了它们在开放场景中的适用性。However, their reliance on predefined and trained object categories limits their applicability in open scenarios.

为了解决这一限制，我们引入了 YOLO-World，这是一种创新方法，通过视觉-语言建模和大规模数据集上的预训练，增强了 YOLO 的开放词汇检测能力。Addressing this limitation, we introduce YOLO-World, an innovative approach that enhances YOLO with open-vocabulary detection capabilities through vision-language modeling and pre-training on large-scale datasets.

具体来说，我们提出了一种新的可重参数化视觉-语言路径聚合网络 (RepVL-PAN) 和区域-文本对比损失，以促进视觉和语言信息之间的交互。Specifically, we propose a new Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) and region-text contrastive loss to facilitate the interaction between visual and linguistic information.

我们的方法在以高效率的零样本方式检测广泛的对象方面表现出色。Our method excels in detecting a wide range of objects in a zero-shot manner with high efficiency.

在具有挑战性的 LVIS 数据集上，YOLO-World 在 V100 上达到了 35.4 AP 和 52.0 FPS，超越了许多在准确性和速度方面的最先进方法。On the challenging LVIS dataset, YOLO-World achieves 35.4 AP with 52.0 FPS on V100, which outperforms many state-of-the-art methods in terms of both accuracy and speed.

此外，经过微调的 YOLO-World 在几个下游任务上取得了显著的表现，包括对象检测和开放词汇实例分割。Furthermore, the fine-tuned YOLO-World achieves remarkable performance on several downstream tasks, including object detection and open-vocabulary instance segmentation.

# 1. 引言
1. Introduction

目标检测一直是计算机视觉中长期存在的基本挑战，应用广泛，包括图像理解、机器人技术和自动驾驶车辆。
Object detection has been a long-standing and fundamental challenge in computer vision with numerous applications in image understanding, robotics, and autonomous vehicles.

大量的工作[16, 27, 43, 45]在深度神经网络的发展下，已经在目标检测领域取得了重大突破。
Tremendous works [16, 27, 43, 45] have achieved significant breakthroughs in object detection with the development of deep neural networks.

尽管这些方法取得了成功，但它们仍然受限于只能处理固定词汇表的目标检测，例如COCO[26]数据集中的80个类别。
Despite the success of these methods, they remain limited as they only handle object detection with a fixed vocabulary, e.g., 80 categories in the COCO[26] dataset.

一旦对象类别被定义和标记，训练过的检测器只能检测这些特定的类别，从而限制了在开放场景中的能力和适用性。
Once object categories are defined and labeled, trained detectors can only detect those specific categories, thus limiting the ability and applicability in open scenarios.

最近的工作[8, 13, 48, 53, 58]通过从语言编码器（例如BERT[5]）中提取词汇知识，探索了流行的视觉-语言模型[19, 39]来解决开放词汇检测[58]的问题。
Recent works [8, 13, 48, 53, 58] have explored the prevalent vision-language models [19, 39] to address open vocabulary detection [58] through distilling vocabulary knowledge from language encoders, e.g., BERT [5].

然而，这些基于蒸馏的方法由于训练数据稀缺且词汇多样性有限（例如，OV-COCO[58]包含48个基础类别）而受到很大限制。
However, these distillation-based methods are much limited due to the scarcity of training data with a limited diversity of vocabulary, e.g., OV-COCO [58] containing 48 base categories.

几种方法[24, 30, 56, 57, 59]将目标检测训练重新构想为区域级视觉-语言预训练，并在大规模上训练开放词汇目标检测器。
Several methods [24, 30, 56, 57, 59] reformulate object detection training as region-level vision-language pretraining and train open-vocabulary object detectors at scale.

然而，这些方法在现实世界场景中的检测仍然面临挑战，主要受到两个方面的影响：（1）计算负担重（2）边缘设备部署复杂。
However, those methods still struggle for detection in real-world scenarios, which suffer from two aspects: (1) heavy computation burden and (2) complicated deployment for edge devices.

以前的工作[24, 30, 56, 57, 59]已经展示了大型检测器预训练的有前景的性能，而对小型检测器进行预训练以赋予它们开放识别能力的研究仍未探索。
Previous works [24, 30, 56, 57, 59] have demonstrated the promising performance of pre-training large detectors while pre-training small detectors to endow them with open recognition capabilities remains unexplored.

在本文中，我们提出了YOLO-World，旨在实现高效率的开放词汇目标检测，并探索大规模预训练方案，以提升传统YOLO检测器到一个新的开放词汇世界。
In this paper, we present YOLO-World, aiming for high-efficiency open-vocabulary object detection, and explore large-scale pre-training schemes to boost the traditional YOLO detectors to a new open-vocabulary world.

与以前的方法相比，所提出的YOLO-World在推理速度上非常高效，并且易于部署到下游应用。
Compared to previous methods, the proposed YOLO-World is remarkably efficient with high inference speed and easy to deploy for downstream applications.

具体来说，YOLO-World遵循标准的YOLO架构[20]并利用预训练的CLIP[39]文本编码器来编码输入文本。
Specifically, YOLO-World follows the standard YOLO architecture [20] and leverages the pre-trained CLIP [39] text encoder to encode the input texts.

我们进一步提出了可重参数化的视觉-语言路径聚合网络（RepVL-PAN），以连接文本特征和图像特征，实现更好的视觉-语义表达。
We further propose the Re-parameterizable Vision-Language Path Aggregation Network (RepVL-PAN) to connect text features and image features for better visual-semantic representation.

在推理过程中，可以移除文本编码器，并将文本嵌入重新参数化为RepVL-PAN的权重，以实现高效部署。
During inference, the text encoder can be removed and the text embeddings can be re-parameterized into weights of RepVL-PAN for efficient deployment.

我们进一步调查了YOLO检测器的开放词汇预训练方案，通过在大规模数据集上进行区域-文本对比学习，将检测数据、定位数据和图像-文本数据统一为区域-文本对。
We further investigate the open-vocabulary pre-training scheme for YOLO detectors through region-text contrastive learning on large-scale datasets, which unifies detection data, grounding data, and image-text data into region-text pairs.

经过预训练的YOLO-World拥有丰富的区域-文本对，展示了强大的大词汇检测能力，训练更多数据可以在开放词汇能力上取得更大的提升。
The pre-trained YOLO-World with abundant region-text pairs demonstrates a strong capability for large vocabulary detection and training more data leads to greater improvements in open vocabulary capability.

此外，我们探索了一种先提示后检测的范式，以进一步提高现实世界场景中开放词汇目标检测的效率。
In addition, we explore a prompt-then-detect paradigm to further improve the efficiency of open-vocabulary object detection in real-world scenarios.

如图2所示，传统的目标检测器[16, 20, 23, 41–43, 52]专注于使用预定义和训练过的类别进行固定词汇（封闭集）检测。
As illustrated in Fig. 2, traditional object detectors [16, 20, 23, 41–43, 52] concentrate on the fixed-vocabulary (close-set) detection with predefined and trained categories.

而以前的开放词汇检测器[24, 30, 56, 59]使用文本编码器对用户的提示进行在线词汇编码并检测对象。
While previous open vocabulary detectors [24, 30, 56, 59] encode the prompts of a user for online vocabulary with text encoders and detect objects.

值得注意的是，这些方法倾向于使用大型检测器和重型主干，例如Swin-L[32]，以增加开放词汇容量。
Notably, those methods tend to employ large detectors with heavy backbones, e.g., Swin-L [32], to increase the open-vocabulary capacity.

相比之下，先提示后检测范式（图2（c））首先对用户的提示进行编码，以构建离线词汇表，不同需求会有不同的词汇表变化。
In contrast, the prompt-then-detect paradigm (Fig. 2 (c)) first encodes the prompts of a user to build an offline vocabulary and the vocabulary varies with different needs.

然后，高效的检测器可以即时推断离线词汇表，无需重新编码提示。
Then, the efficient detector can infer the offline vocabulary on the fly without re-encoding the prompts.

对于实际应用，一旦我们训练了检测器，即YOLO-World，我们可以预先编码提示或类别以构建离线词汇表，然后将其无缝集成到检测器中。
For practical applications, once we have trained the detector, i.e., YOLO-World, we can pre-encode the prompts or categories to build an offline vocabulary and then seamlessly integrate it into the detector.

Our main contributions can be summarized into three folds:  
我们的主要贡献可以总结为三个方面：  
• We introduce the YOLO-World, a cutting-edge open vocabulary object detector with high efficiency for real world applications.  
• 我们介绍了YOLO-World，这是一个尖端的开放词汇对象检测器，具有高效的现实世界应用效率。 

• We propose a Re-parameterizable Vision-Language PAN to connect vision and language features and an open vocabulary region-text contrastive pre-training scheme for YOLO-World.  
• 我们提出了一个可重参数化的视觉-语言PAN，以连接视觉和语言特征，并为YOLO-World提供一个开放词汇区域-文本对比预训练方案。 

• The proposed YOLO-World pre-trained on large-scale datasets demonstrates strong zero-shot performance and achieves 35.4 AP on LVIS with 52.0 FPS. The pre-trained YOLO-World can be easily adapted to downstream tasks, e.g., open-vocabulary instance segmentation and referring object detection. Moreover, the pre-trained weights and codes of YOLO-World will be open-sourced to facilitate more practical applications.  
• 提出的YOLO-World在大规模数据集上进行预训练，展示了强大的零样本性能，并在LVIS上达到了35.4 AP和52.0 FPS。预训练的YOLO-World可以轻松适应下游任务，例如开放词汇实例分割和指代对象检测。此外，YOLO-World的预训练权重和代码将开源，以便于更多实际应用。

# 5. 结论
结论
Conclusion

我们提出了YOLO-World，这是一种尖端的实时开放词汇检测器，旨在提高现实世界应用中的效率和开放词汇能力。
We present YOLO-World, a cutting-edge real-time open-vocabulary detector aiming to improve efficiency and open-vocabulary capability in real-world applications.

在这篇论文中，我们重新塑造了流行的YOLO，将其作为开放词汇预训练和检测的视觉语言YOLO架构，并提出了RepVL-PAN，
In this paper, we have reshaped the prevalent YOLOs as a vision-language YOLO architecture for open-vocabulary pretraining and detection and proposed RepVL-PAN,

该网络连接了视觉和语言信息，并且可以为高效部署进行重新参数化。
which connects vision and language information with the network and can be re-parameterized for efficient deployment.

我们进一步提出了带有检测、定位和图像-文本数据的有效预训练方案，以赋予YOLO-World强大的开放词汇检测能力。
We further present the effective pre-training schemes with detection, grounding, and image-text data to endow YOLO-World with a strong capability for open-vocabulary detection.

实验可以证明YOLO-World在速度和开放词汇性能方面的优越性，并表明视觉语言预训练在小型模型上的有效性，这对未来的研究富有启示性。
Experiments can demonstrate the superiority of YOLO-World in terms of speed and open-vocabulary performance and indicate the effectiveness of vision-language pre-training on small models, which is insightful for future research.

我们希望YOLO-World能成为解决现实世界开放词汇检测的新基准。
We hope YOLO-World can serve as a new benchmark for addressing real-world open-vocabulary detection.