import torch
import numpy as np
print("TENSOR TO NUMPY: (CPU)")
a=torch.ones(5)
b=a.numpy()
print(b)
print(type(b))
b+=1
print(a)
print("\n\nNUMPY TO TENSOR: (CPU)")
y=np.ones(5)
x=torch.from_numpy(y).int()
print(x)
print(type(x))
x+=1
print(y)
print("\n\nGPU TENSORS")
q=torch.ones(5)
#check if cuda is available to use and create gpu tensors
if torch.cuda.is_available():
    #assigning "device" var as cuda(gpu)
    device=torch.device("cuda")
    #creating new tensor which follows the device
    p=torch.ones(5,device=device)
    print(p)
    #applying cuda to existing cpu tensor to make it gpu
    q=q.to(device)
    #faster calculations
    r=p+q
    print(r)
    #making gpu tensor back to cpu
    #CANNOT CONVERT A GPU TENSOR TO NUMPY ARRAY DIRECTLY, FIRST CONVERT IT TO CPU
    p=p.to("cpu")
#to make numpy changes not affect tensor, we can create a numpy, convert it to tensor,
#then make that tensor use gpu, then make changes in the tensor or numpy then they would act individually
print("\n\nNUMPY TO GPU TENSOR: ")
l=np.arange(1,6,1)
k=torch.from_numpy(l).int()
if torch.cuda.is_available():
    device=torch.device("cuda")
    k=k.to(device)
    k+=2
    print(k)
    print(l)
