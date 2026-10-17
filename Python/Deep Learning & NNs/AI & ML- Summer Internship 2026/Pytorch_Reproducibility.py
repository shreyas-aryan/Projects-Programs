#stack,squeeze,permute
import torch
t1=torch.arange(2,11,2,device="cuda")
print(t1.size())
t2=torch.stack([t1,t1,t1],dim=0)
t3=torch.vstack([t1,t1,t1])                    #VERTICALLY, ON TOP EACH OTHER
print(t2)
print(t3)
t4=torch.stack([t1,t1,t1],dim=1)
t5=torch.hstack([t1,t1,t1])                    #DIFFERENT
print(t4)
print(t5)
#squeeze
t6=torch.ones(1,3,4,1,1)
print(t6)
t6=t6.squeeze()
print(t6)
t6=t6.unsqueeze(dim=0)
print(t6)
#permute
img=torch.rand(224,224,3) #image recog by tensors through height,width, colour channels
img_per=img.permute(2,0,1)# now its colour channels,height,width
print(img)
print(img_per)
torch.manual_seed(42)
t7=torch.rand(5)
torch.manual_seed(42)
t8=torch.rand(5)
print(t7)
print(t8)
print(t7==t8)
