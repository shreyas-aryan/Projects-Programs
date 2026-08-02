import torch
import torch.nn as nn
from torchvision import transforms, models
from PIL import Image
#LIST OF CLASSES(subfolders)
classes = ['sitting', 'standing', 'walking']

#LRMODEL same as main.py
net = models.resnet18(weights="IMAGENET1K_V1")
net.fc = nn.Linear(net.fc.in_features, 3)
#LOADING MODEL
net.load_state_dict(torch.load("model.pth"))
#TESTING MODE
net.eval()

#TRANSFORM same as main.py
tf = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

imgpath = input("Enter image path: ")

#access the image file
img = Image.open(imgpath).convert("RGB")#3 layers
img = tf(img)#transform to tensor
img = img.unsqueeze(0)#adds a single dimension at index 0 for batch no. as [batchno.,rgb,height,width]

with torch.no_grad():#can use no grad or inference mode
    out = net(img)#frwd pass- call the model basically
    _, pred = torch.max(out, 1) #determining the most likly prediction ie is it walk,stand or sit

print("Predicted activity:", classes[pred.item()])
