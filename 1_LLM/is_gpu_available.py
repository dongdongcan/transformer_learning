# Copyright (c) 2024 dongdongcan
# This code is licensed under the MIT License.
# See the LICENSE file for details.

import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)
