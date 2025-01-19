# Copyright (c) 2024 dongdongcan
# This code is licensed under the MIT License.
# See the LICENSE file for details.

from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm3-6b", trust_remote_code=True, device="cpu")
model = model.eval()
response, history = model.chat(tokenizer, "你好", history=[])
print(response)
