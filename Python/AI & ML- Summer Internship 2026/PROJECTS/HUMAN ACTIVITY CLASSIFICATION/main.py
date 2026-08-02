import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms, models
from pathlib import Path

# PATHS
imgpath = Path("activity")
train = imgpath/"train"
test = imgpath/"test"

# DATA PREPARATIONS- TO TENSOR
#converts the images into tensors
tf = transforms.Compose([
    transforms.Resize((224,224)),  #resizing images to 224 pixels, height,width 224 for resnet18
    transforms.ToTensor()  #converts the input to tensors
])

# DATA
traindata = datasets.ImageFolder(train, transform=tf)  #access the "train" folder, and transform becomes the tensor convertor
testdata = datasets.ImageFolder(test, transform=tf)  #access 1 folder when called, or 1 images, thus we use dataloader later on

classes = traindata.classes  #subfolders becomes classes, sit,walk,stand
print(classes)

trainload = DataLoader(traindata, batch_size=8, shuffle=True) #access all images in batchs ie 8 at a time in shuffled order, so order doesnt effect
testload = DataLoader(testdata, batch_size=8, shuffle=False) #verfication step, not training or learning thus no shuffle

# MODEL
net = models.resnet18(weights="IMAGENET1K_V1")  #resnet18, a nn for images used from torchvision, imgnet existing photos to be trained on for saftey

# freeze all layers, only train last layer since we have very little data, so that our training model not effected by existing models weight and bias
for p in net.parameters():
    p.requires_grad = False

net.fc = nn.Linear(net.fc.in_features, 3)#1000 layer or subfolders of imagenet outputting 3 layers for linreg, just like our classes

# LOSS AND OPTIM
lossfn = nn.CrossEntropyLoss()#for multiclass classification, this lossfn is used
opt = torch.optim.Adam(net.fc.parameters(), lr=0.001)#adam for imageclass on small data

#TRAIN LOOP
epochs = 15
for ep in range(epochs):
    net.train()                     #1)model to train
    for imgs, labels in trainload:
        opt.zero_grad()             #2)optim zero grad
        out = net(imgs)             #3)forward pass
        loss = lossfn(out, labels)  #4)calculate loss
        loss.backward()             #5)backpropogation
        opt.step()                  #6)gradient decent
    #imgs-[8,3,224,224], labels-[8]
    print(f"epoch {ep+1}/{epochs} loss {loss.item():.4f}")

# TEST LOOP
net.eval()
with torch.no_grad():
    for imgs, labels in testload:
        out = net(imgs) #forward pass- calling the model
        loss = lossfn(out, labels)  #calc loss
print(f"test loss {loss.item():.4f}")

# SAVE MODEL
torch.save(net.state_dict(), "model.pth")#state dict returning dict of parameters with their corresponing classes
