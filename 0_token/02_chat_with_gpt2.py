# Copyright (c) 2024 dongdongcan
# This code is licensed under the MIT License.
# See the LICENSE file for details.


import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

torch.manual_seed(torch.randint(0, 10000, (1,)).item())

# 加载模型和Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
print(model)

prompt = "How are you"
inputs = tokenizer.encode(prompt, return_tensors="pt")

# 生成固定文本
outputs = model.generate(inputs, max_length=20, num_return_sequences=1)
generated_text = tokenizer.decode(outputs[0])
print(generated_text)
