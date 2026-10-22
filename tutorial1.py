# this tutorial is executed using my local GPU: NVIDIA GeForce RTX 4060 Laptop GPU

# GPU hardware verfication code
import tensorflow as tf
print("TensorFlow GPUs:", tf.config.list_physical_devices('GPU'))

import torch
print("PyTorch CUDA Available:", torch.cuda.is_available())

# additional
print("GPU Name and Specifications",tf.test.gpu_device_name())

# tensor creation and reshape tensorflow
import numpy as np
x = np.array([1.0, 2.0, 3.0, 4.0])
t_tf = tf.convert_to_tensor(x)

# reshape to 2x2 matrix
t_reshape = tf.reshape(t_tf, (2,2))
print("TF Shape:", t_reshape.shape)
print("TF tensor:", t_reshape)

# tensor creation and reshape torch

# create 1D tensor and view it as 2x2
t_torch = torch.tensor([1.0, 2.0, 3.0, 4.0])
t_view = t_torch.view(2,2)
print("TF torch:", t_view)

# transfer tensor to GPU accelerator
device = "cuda" if torch.cuda.is_available() else "cpu"
t_gpu = t_view.to(device)
print("TF torch gpu:", t_gpu)
