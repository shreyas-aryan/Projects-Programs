#linear reg
import torch
import matplotlib.pyplot as plt
from torch import nn
import numpy as np
#LINEAR REG MODEL
class LRModel(nn.Module): #LRM inheriting properties of nn.module
    def __init__(self):  #input/constructor
        super().__init__()
        self.weight=nn.Parameter(torch.randn(1,requires_grad=True,dtype=torch.float))#giving weight randn parameter, following grad desecent
        self.bias=nn.Parameter(torch.randn(1,requires_grad=True,dtype=torch.float)) #same
    def forward(self,x):                  #x is expected torch.tensor and returns torch.tensor
        return self.weight*x+self.bias     #linreg

#VISUALIZATION
def plot(train_data,train_label,test_data,test_label,predictions):
    plt.scatter(train_data,train_label,c="g",s=4,label="Training Set")
    plt.scatter(test_data,test_label,c="y",s=4,label="Test Set")
    if predictions is not None:
        plt.scatter(test_data,predictions,c="r",s=4,label="Prediction")
    plt.legend()
    plt.show()

#TRAINING OR INITIAL DATASET WITH KNOWN PARAMETERS
weight=0.7
bias=0.2
X=torch.arange(0,1,0.02).unsqueeze(dim=1)
y=weight*X+bias
print(f"{X[:10]}\n\n\n{y[:10]}")

#TRAIN AND TEST SPLITS
print("\n\nTRAIN AND TEST SPLITS: ")
split=int(.8*len(X))
xtrain=X[:split]
ytrain=y[:split]
xtest=X[split:]
ytest=y[split:]
print(len(xtrain),len(ytrain),len(xtest),len(ytest))

#VISUALISING TRAIN AND TEST
print("\n\nPLOTTING DATA:")
plot(xtrain,ytrain,xtest,ytest,None)

#USING THE MODEL PREDICTING ON RANDOM VALUES FROM CLASS
#IMP: RANDOM SEED
torch.manual_seed(42)
model=LRModel()
print(list(model.parameters()))
print("\n\nPREDICTING BEGIN")
with torch.inference_mode():
    ypred=model(xtest)
print(ypred)

#VISUALING WITH PREDICTED DATA
plot(xtrain,ytrain,xtest,ytest,ypred)

#TRAINING THE MODEL, MOVING FROM UNKNOWN PARAMETERS(RANDN) TO SOME KNOWN PARAMETERS, to do that it uses loss function and optimizer
#and use train and test loop
#loss finds difference
loss=nn.L1Loss()
#optim minimizes the differences takes action reduce loss func(stochastic gradient descent)
opt=torch.optim.SGD(model.parameters(),lr=0.01)

#train loop
#0) model to train mode 1) frwd pass, 2)calc loss, 3)optim 0 grad, 4)loss bcwd, 5)optim step
print(list(model.parameters()))
torch.manual_seed(42)
r=200
count=[]
losscount=[]
tlosscount=[]
#training loop
for i in range(r):
    #set model to train
    model.train()#makes all req grad to req grad
    #forward pass, predict y on basis of x train data, remember its train loop not test loop everything on basis of train split
    ypred=model(xtrain)
    #calculating loss- loss(input,target)
    l=loss(ypred,ytrain)
    #optim zero grad
    opt.zero_grad()#reset the grad value throughout the loop for no ambiguity in step 5
    #back prop
    l.backward()
    #grad des
    opt.step()#incrementing the grad descent, changes will accumulate, so needs to be zeroed
    #off grad track
    model.eval()#turn off grad tracking/ all params needed for testing are enabled
    with torch.inference_mode():
        testpred=model(xtest)
        testloss=loss(testpred,ytest)
    #printing out data for steps
    if i%10==0:
        count.append(i)
        losscount.append(l)
        tlosscount.append(testloss)
        print(f"Loss: {l}| Test Loss: {testloss} | Iteration: {i}")
        print(model.state_dict())
        print()
with torch.inference_mode():
    ynpreds=model(xtest)
plot(xtrain,ytrain,xtest,ytest,ynpreds)

#visualising the loss curve and test loss curve
#loss curve
with torch.no_grad():
    plt.plot(count,np.array(torch.tensor(losscount).numpy()),label="Train loss")
    plt.plot(count,np.array(torch.tensor(tlosscount).numpy()),label="Test loss")
    plt.legend()
    plt.ylabel("LOSS")
    plt.xlabel("COUNT")
    plt.show()

#saving
torch.save(model.state_dict(),"LRModel.pth")
