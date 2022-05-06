import numpy as np
import torch



a = torch.tensor(0).float()
print(a)
print(a.max())

y = torch.tensor(([1,2,1],[1,2,3])).float()
print(y)

y = torch.where(y == 2, y, torch.tensor(0).float())
# y = torch.where(y == 3, y, torch.tensor(0).float())
print(y)
print(y.max())