# Copyright (c) 2024 dongdongcan
# This code is licensed under the MIT License.
# See the LICENSE file for details.


from transformers import GPT2Tokenizer

# 加载模型和Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# 初始文本
prompt = "I debug my code all day, and I am like a debugger."

encode_id = tokenizer.encode(prompt)
print(encode_id)

tokens = tokenizer.convert_ids_to_tokens(encode_id)
print(tokens)
