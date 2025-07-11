# 仓库介绍

本仓库为 《Transformer通关秘籍》专栏的配套代码仓库，[专栏点击这里](https://www.yuque.com/yuqueyonghupftxbc/ai100/wvyi8axax45piuxq)。

《Transformer通关秘籍》专栏有几十篇高质量文章，已经完成更新，专栏系统性的讲解了学习大模型（Transformer架构）需要的背景知识和原理。

[加入星球](https://www.yuque.com/yuqueyonghupftxbc/ai100/aiy5vb3bu2id5agp)，你也可以免费阅读到这些专栏文章。

# 更多学习教程
> 
> 《AI视觉入门与调优》专栏：[点击这里](https://www.yuque.com/yuqueyonghupftxbc/ai100/klydnq5blhqq8x1s)
> 
>
> 《从零手写大模型实战》专栏：[点击这里](https://www.yuque.com/yuqueyonghupftxbc/ai100/lc1bna1l1dl2zp39)
>
> 原创 AI 学习系列教程，点击这里：[AI小白到AI大神的天梯之路](https://www.yuque.com/yuqueyonghupftxbc/ai100/snfie4aka5fn5ykg)
>
> 加入《小而精的 AI 学习圈》知识星球，一起学习 AI ： [我们星球见](https://www.yuque.com/yuqueyonghupftxbc/ai100/aiy5vb3bu2id5agp)


# 专栏简介
大模型的发展早已势不可挡了。

你可能在很多场合都听到过 Transformer 的名字，你肯定也了解过这两年无论是国内还是国外，AI 大模型的发展非常迅速，已经在很多传统领域掀起了革命性的创新热潮。

在 AI 大模型面世后，人们纷纷使用 AI 大模型进行绘画和文章创作、自媒体创作（如小红书文案和配图）、代码续写、网页内容整理、思维导图制作、PPT制作甚至用 AI 制作短视频。

可以说，你所能想到的工作和生活场景，几乎都有 AI 大模型参与的身影。一句话：大模型可以落地并为你提效的场景太多了！

事实上，这些火爆、高效充满“智能”的大模型，无论是国外的GPT系列，还是 Meta (原FaceBook）的 LLaMa系列，还是国内的 Kimi、讯飞星火、百度文心、清华智浦、商汤小浣熊等大模型，基本上都是基于 Transformer 架构演化而来的。

可以说， Transformer 架构是目前主流 AI 大模型的核心。

本专栏便将围绕着 Transformer 这一架构，来拆解自然语言处理和 AI 大模型有关的背景、底层技术和算法原理。

在拆解的过程中，会有很多相关背景知识的介绍。希望你再阅读完本专栏后，不仅可以对以 Transformer 架构为核心的大模型有一定的了解，还可以对大模型的底层细节和技术背景有更加深刻的认识。

本专栏定位虽然是聚焦在算法和技术方面的内容，但为了让你在阅读过程中不至于过于枯燥，我会给出许多经典 AI 大模型的使用方法和体验链接，包括在网页上直接使用 AI 大模型，以及使用 Python 代码调用相关大模型的 API 接口等，当然，也会会给出一些好玩的大模型应用。

# 专栏大纲
温馨提示：下面展示专栏的大纲。

## 好玩实用的大模型
这里搜罗了在本专栏更新过程中发现的一些好玩、实用的大模型应用。

包括但不限于使用 AI 大模型完成文生图、文生视频、图生视频、智能体游戏等等，汇聚在这里。

- AI 大模型初体验（网页版）

这里整理了国内外知名 AI 公司发布的 AI 大模型的使用链接，以及相关模型的介绍，都汇总在上面的链接中。目前包括：百度文心一言、腾讯混元、阿里通义千问、讯飞星火、清华智谱清言（chatGLM）、月之暗面 Kimi、OpenAI GPT系列、POE、Llama系列、快手可灵等。

- AI 大模型初体验：使用 Python 调用 ChatGLM
- AI 大模型初体验：在笔记本上，利用 CPU 上部署 LLaMa2
- AI 大模型初体验：使用 Python 调用 LLaMa3
- 有趣的 AI 应用：利用 AI 生成视频（网页版）
- 有趣的 AI 应用：利用 AI 生成各种风格的漫画
- 实用的 AI 应用：手把手带你使用 AI 完成网页内容的总结
- 实用的 AI 应用：文生视频国产 Sora 平替
- 实用的 AI 应用：体验 MidJourney 绘画

## 环境配置相关
- 选配：安装 Ubuntu 系统 (非必须)
- 快速访问 Hugging Face (必看)
- 环境配置与代码仓库 (必看)

## 预处理阶段（基础）
该阶段完成输入句子（单词）到向量空间的表达，可以认为是大模型进行推理之前的，文本预处理阶段。

- Token 相关
- 了解 token
- 利用 BERT 对文本进行 token 化
- 利用 GPT2 将文本 token 化
- 文本 token 化的过程是怎样的（算法介绍）
- GPT3.5/4 的 token 可视化工具

## 词嵌入(Word Embedding)相关
- Token 到数值的转换（词汇表）
- Token 到词嵌入向量的转换（Word Embedding）
- 向量如何表示近义词？(余弦相似度)
- 词向量的值：实际上是特征
- 词向量运算：Python 实现"Queen = King - Man + Wowem"
- Word2Vec 及相关工具的使用

## Transformer 主干架构原理、背景和技术相关
- 什么是 Seq2Seq 模型？
- 什么是 Encoder-Decoder 模型？
- 基于 RNN 的 Encoder-Decoder 结构
- 以 LSTM 为例，通俗理解 RNN（循环神经网络）
- 基于 RNN 的 Encoder-Decoder 结构完成文本翻译的过程
- 初识注意力
- 当注意力遇上 Seq2Seq 模型
- 再看注意力（Query、Key、Value）
- 两个例子感受注意力的作用
- Transformer 论文通俗解读：摘要、引言、背景
- Transformer 论文通俗解读：编解码
- Transformer 论文通俗解读：注意力的运算
- Transformer 论文通俗解读：多头注意力
- Transformer 论文通俗解读：FFN 层
- FFN 中的非线性表达
- FFN 中的线性变换
- 线性层和矩阵乘法的区别和联系
- 模型输出线性层：从隐藏特征到样本特征的映射
- Softmax 是如何完成数值到概率转换的？
- MaskSoftmax 如何屏蔽未来信息？
- 残差结构在 Transformer 中的作用
- 为什么会有 LayerNorm 这类算法？
- 什么是 Pre-Norm 和 Post-Norm
- 位置编码：为什么需要位置编码？
- 位置编码：编码的是什么信息？
- 位置编码：需要具备什么特性？
- 位置编码：位置编码算法介绍
- 位置编码：基于正余弦函数的位置编码的公式理解
- 位置编码：一文搞懂旋转位置编码(RoPE)
- 大模型的推理过程：KVCache 的引入(Prefill 和 Decode)
- 如何实现 KVCache 优化

## 后处理相关
该部分对应的是 Transformer 推理完成后，对输出的原始得分进行后处理的内容，后处理的目的是为了让 AI 大模型输出的文本（Response）更加符合人类的需求，同时保持多样性。

- 后处理：为什么要对 Logits 进行惩罚
- 后处理：预测得分的 Top_k 采样
- 后处理：预测得分的 Top_p 采样
- 后处理：预测得分的温度参数和 Softmax 计算

## 一些模型结构介绍
- 模型：什么是 Decoder-Only 结构
- 模型：GPT 系列和 BERT 系列的结构
- 模型：Qwen2 的模型结构和细节

# 完整的学习路线和教程
加入知识星球，即可免费阅读到本项目的所有文章 ： [2025我们星球见](https://www.yuque.com/yuqueyonghupftxbc/ai100/aiy5vb3bu2id5agp)

# 其他
本项目所有代码和相关文章，均为个人原创，未经同意，请勿随意转载至任何平台，更不可用于商业目的，我已委托相关维权人士对原创文章和代码进行监督。

# 联系我
微信号：ddcsggcs
公众号：[董董灿是个攻城狮](https://mp.weixin.qq.com/s/-YVb5JM7HVqrkiVrraBlDA?token=1017142557&lang=zh_CN)
邮箱：dongdongcan2024@163.com。
