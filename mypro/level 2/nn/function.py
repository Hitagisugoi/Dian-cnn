from typing import Union
from torch import Tensor
from torch.nn.modules import Module
from torch.nn.parameter import Parameter
import torch
from torch.nn.modules.conv import _ConvNd
# from cnnbase import ConvBase
from torch.nn.modules.utils import _pair
from torch.nn.common_types import _size_2_t
import torch.nn.functional as F
import numpy as np
import time
import math

class Conv2d(_ConvNd):
   
    def __init__(
        self,
        in_channels: int,   #输入图像的深度
        out_channels: int,    #输出图像的深度，亦即卷积核的个数
        kernel_size: _size_2_t,    #卷积核尺寸（宽高相同，一般取奇数）
        stride: _size_2_t = 1,   #步长
        padding: Union[str, _size_2_t] = 0,      #边缘拓展数
        dilation: _size_2_t = 1,   
        groups: int = 1,    #控制输入通道和输出通道的分组
        bias: bool = True,    #偏置
        padding_mode: str = 'zeros',    #填充方式：zeros则全填0  # TODO: refine this type
        device=None,
        dtype=None
    ):
        factory_kwargs = {'device': device, 'dtype': dtype}
        kernel_size_ = _pair(kernel_size)
        stride_ = _pair(stride)
        padding_ = padding if isinstance(padding, str) else _pair(padding)
        dilation_ = _pair(dilation)
        super(Conv2d, self).__init__(
            in_channels, out_channels, kernel_size_, stride_, padding_, dilation_,
            False, _pair(0), groups, bias, padding_mode, **factory_kwargs)
        
    def conv2d(self, input:Tensor, kernel:Tensor, bias = 0, stride=1, padding=0):
        if padding > 0:
            input = F.pad(input, (padding, padding, padding, padding))    #每个维度扩充数量为padding
        bs, in_channels, input_h,input_w = input.shape
        
        out_channel, in_channel,  kernel_h, kernel_w = kernel.shape
        #输出通道、输入通道、卷积核高度、卷积核宽度
        if bias is None:
            bias = torch.zeros(out_channel)

        output_h = (math.floor((input_h - kernel_h) / stride) + 1)
        output_w = (math.floor((input_w - kernel_w) / stride) + 1)

    # 初始化输出矩阵
        
        output = torch.zeros(bs, out_channel, output_h, output_w)
	
    # 不考虑性能
        for ind in range(bs):  #根据一组样本的数量，遍历隐藏子层的次数
            for oc in range(out_channel):
                for ic in range(in_channel):  #由输入、输出通道决定循环逻辑
                    for i in range(0, input_h - kernel_h + 1, stride):
                        for j in range(0, input_w - kernel_w + 1, stride):#卷积运算循环
                            region = input[ind, ic, i:i + kernel_h, j: j + kernel_w]
                        # 点乘相加
                            output[ind, oc, int(i / stride), int(j / stride)] += torch.sum(region * kernel[oc, ic])
                output[ind, oc] += bias[oc]

        return output
    
    def forward(self, input: Tensor):
        weight = self.weight
        bias = self.bias
        return self.conv2d(input, weight, bias)
    
    def backward(self, ones: Tensor):
        '''TODO backward的计算方法''' 
        return self.input.grad
    
class Linear(Module):
    __constants__ = ['in_features', 'out_features']
    in_features: int
    out_features: int
    weight: Tensor

    def __init__(self, in_features: int, out_features: int, bias: bool = True,
                 device=None, dtype=None):
        factory_kwargs = {'device': device, 'dtype': dtype}
        super(Linear, self).__init__()
        self.in_features = in_features          #输入的神经元个数
        self.out_features = out_features        #输出的神经元个数
        
        self.weight = Parameter(torch.empty((out_features, in_features), **factory_kwargs))    #随机weight
        if bias:
            self.bias = Parameter(torch.empty(out_features, **factory_kwargs))
            
            
    def forward(self, input):
      
        if input.dim() == 2 and self.bias is not None:
          self.output = torch.addmm(self.bias, input, self. weight.t())   #addmm函数实现将后两个矩阵（输入和权重）进行点乘，然后加上偏置self.bias
        return self.output
    def backward(self, ones: Tensor):
        '''TODO'''
        return self.input.grad

class CrossEntropyLoss():
    def __init__(self):
        pass
    def __call__(self, input, target):
        self.output = 0    #initialize output
        
        for i in range(input.size(0)):       #用样本数作为循环长度
            #概率化，每个张量中的数值化为指数函数，实质上实现了softmax函数的作用
            numer = torch.exp(input[i,target[i]])     #分子部分
            denom = torch.sum(torch.exp(input[i,:]))        #分母部分
            loss = -torch.log(numer / denom)         #每个样本的损失
            self.output += loss         #先把损失全部求和
            
        self.output /= input.size(0)     #除以样本数，得到代价函数
        
        return self.output
    def backward(self):
        '''
        sum = 0
        i = 0

        begin = time.clock()
        while True:
            batch, label = random_get_data(mat, batch_size)
            sig3, sig2, sig1 = cal_gradient(batch, label)
            update(batch, sig1, sig2, sig3)
            loss = cal_loss(batch, label)
            sum += loss
            i += 1
            if i % 1000 == 0:
                loss = sum/1000
                sum = 0
                print(loss)
                if loss < 0.01:
                    break
        end = time.clock()
        print('cost time = %f s' % (end-begin))
        '''
        return self.input.grad
        
