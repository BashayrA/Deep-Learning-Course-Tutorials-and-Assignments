# Tensor Creation and Manipulation Using PyTorch

# Import the PyTorch library.
import torch
import numpy as np

# Create a 2D Tensor containing the students' data.
Study_Hours = np.array([2, 4, 6, 3])
Attendance_Percentage = np.array([80, 90, 95, 70])
Previous_Exam_Score = np.array([65, 75, 85, 60])

student_data = np.column_stack([Study_Hours, Attendance_Percentage, Previous_Exam_Score]) 
t_student_data = torch.tensor(student_data)

# Display the Tensor and its shape.
print("the tensor created presenting student data:", t_student_data)
print("tensor's shape:", t_student_data.shape)

# Print the number of dimensions of the Tensor. note: it is called rank fro tensorflow
print("tensor's dimesion:", t_student_data.dim())

# Check whether a GPU is available using PyTorch.
print("GPU is available:", torch.cuda.is_available())

# Transfer the Tensor to the GPU if available; otherwise, use the CPU.
device = "cuda" if torch.cuda.is_available() else "cpu"
t_student_data_gpu = t_student_data.to(device)

# Print the device used to store the Tensor.
print("original tensor:", t_student_data.device)      
print("moved tensor:  ", t_student_data_gpu.device)
print("the name of the GPU:", torch.cuda.get_device_name())   