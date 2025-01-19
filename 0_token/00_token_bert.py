# Copyright (c) 2024 dongdongcan
# This code is licensed under the MIT License.
# See the LICENSE file for details.

# 从transformers库中导入BertTokenizer类
from transformers import BertTokenizer

# 初始化BertTokenizer，加载'bert-base-uncased'预训练模型。
# 这个模型处理的是不区分大小写的英文文本。
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# 定义一个示例文本字符串。
text = "I debug my code all day, and I am like a debugger."

# 使用tokenizer对文本进行编码，将文本分割成tokens，同时映射到相应的ID。
encoded_input = tokenizer(text)

# 使用tokenizer的convert_ids_to_tokens方法将tokens的ID转换回可读的tokens。
# 这个操作有助于人类理解模型是如何看待文本的。
tokens = tokenizer.convert_ids_to_tokens(encoded_input["input_ids"])

# 打印出tokens及其对应的ID。这有助于理解文本如何被分割和编码。
print("Tokens:", tokens)
print("Token IDs:", encoded_input["input_ids"])
