#2.Create a random tensor with shape (7, 7)
import torch
a=torch.rand(7,7)
print(a)

#3.Perform a matrix multiplication on the tensor from 2 with another random tensor
#with shape (1, 7) (hint: you may have to transpose the second tensor).
b=torch.rand(1,7)
#b=b.T
b=b.reshape(7,1)
print(b)
c=torch.matmul(a,b)
print(c)

#4.Set the random seed to 0 and do exercises 2 & 3 over again.
torch.manual_seed(0)
a1=torch.rand(7,7)
a2=torch.rand(1,7).reshape(7,1)
a3=torch.matmul(a1,a2)
print(a3)

#5.Speaking of random seeds, we saw how to set it with torch.manual_seed() but is there a GPU
#equivalent? (hint: you'll need to look into the documentation for torch.cuda for this one).
#If there is, set the GPU random seed to 1234.
torch.cuda.manual_seed(1234)
a5=torch.rand(5,device='cuda')
print(a5)

#6.Create two random tensors of shape (2, 3) and send them both to the GPU (you'll need access to a GPU for this).
#Set torch.manual_seed(1234) when creating the tensors (this doesn't have to be the GPU random seed).
p=0
q=0
if torch.cuda.is_available():
    device=torch.device("cuda")
    torch.manual_seed(1234)
    p=torch.rand(2,3,device=device)
    torch.manual_seed(1234)
    q=torch.rand(2,3,device=device)
    print(p,q)

#7.Perform a matrix multiplication on the tensors you created in 6 (again, you may have
#to adjust the shapes of one of the tensors)
q=q.T
r=torch.matmul(p,q)
print(r)

#8.Find the maximum and minimum values of the output of 7.
print(r.max().item())
print(r.min().item())

#9. Find the maximum and minimum index values of the output of 7.
print(r.argmax())
print(r.argmin())

#10. Make a random tensor with shape (1, 1, 1, 10) and then create a new tensor with all the 1 dimensions removed
#to be left with a tensor of shape (10).Set the seed to 7 when you create it and print out the first tensor and
#it's shape as well as the second tensor and it's shape.
torch.manual_seed(7)
l=torch.rand(1,1,1,10)
o=l.squeeze()
print(l)
print(l.shape)
print(o)
print(o.shape)
