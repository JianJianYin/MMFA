import logging
import torch.nn as nn
import numpy as np

class BaseModel(nn.Module):
    def __init__(self):
        super(BaseModel, self).__init__()
        self.logger = logging.getLogger(self.__class__.__name__) #self.__class__.__name__为获得此时的类名，即BaseModel

    def forward(self):
        raise NotImplementedError

    def summary(self):
        model_parameters = filter(lambda p: p.requires_grad, self.parameters())
        nbr_params = sum([np.prod(p.size()) for p in model_parameters])
        self.logger.info(f'Nbr of trainable parameters1: {nbr_params}') #会返回模型的总的需要更新梯度的参数量

    def __str__(self):
        total_num = sum(p.numel() for p in self.parameters())
        trainable_num = sum(p.numel() for p in self.parameters() if p.requires_grad)
        model_parameters = filter(lambda p: p.requires_grad, self.parameters())
        nbr_params = int(sum([np.prod(p.size()) for p in model_parameters]))
        return f'\nNbr of trainable parameters: {nbr_params},total_num:{total_num},trainable_num:{trainable_num}'
        #return super(BaseModel, self).__str__() + f'\nNbr of trainable parameters: {nbr_params}'
