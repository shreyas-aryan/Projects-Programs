import torch
import torch.nn as nn
import cv2
import time
from torchvision import transforms, models
from PIL import Image

# LIST OF CLASSES (subfolders, alphabetical order from ImageFolder)
classes = ['animal', 'person', 'vehicle']

# maps predicted class to a monitoring alert level (same idea as sitting/standing/walking -> normal/warning/red alert)
alert_map = {
    'animal': 'NORMAL',       # wildlife/cattle near fence, low priority
    'vehicle': 'WARNING',     # vehicle near border, needs attention
    'person': 'RED ALERT'     # human intrusion, highest priority
}

# MODEL same as train.py
net = models.resnet18(weights="IMAGENET1K_V1")
net.fc = nn.Linear(net.fc.in_features, 3)
# LOADING TRAINED MODEL
net.load_state_dict(torch.load("border_model.pth"))
# TESTING MODE
net.eval()

# TRANSFORM same as train.py
tf = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

# SOURCE: 0 for webcam, or a path to a single image e.g. "test_frame.jpg"
source = input("Enter image path (or 0 for webcam): ")

# helper: runs one frame/image through the model and returns label + alert
def predict_frame(img_array):
    img = cv2.cvtColor(img_array, cv2.COLOR_BGR2RGB)  #opencv reads BGR, model expects RGB
    img = Image.fromarray(img)
    img = tf(img)              #transform to tensor
    img = img.unsqueeze(0)     #adds batch dimension [1,3,224,224]

    with torch.no_grad():
        out = net(img)
        _, pred = torch.max(out, 1)  #most likely class

    label = classes[pred.item()]
    alert = alert_map[label]
    return label, alert

if source == "0":
    # WEBCAM MODE: keep watching the feed, predict every 5 seconds
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("could not open webcam")
        exit()

    capture_interval = 5  # seconds, proposed frame-capture interval (same as CCTV case study in report)
    last_capture = 0

    print("starting monitoring... press q to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("feed lost")
            break

        now = time.time()
        if now - last_capture >= capture_interval:
            last_capture = now
            label, alert = predict_frame(frame)
            print(f"[{time.strftime('%H:%M:%S')}] Detected: {label} -> {alert}")

            # draw the result on the frame so it shows in the preview window
            cv2.putText(frame, f"{label} | {alert}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Border Surveillance Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

else:
    # IMAGE MODE: predict once on a single image, no window
    frame = cv2.imread(source)
    if frame is None:
        print("could not read image, check the path")
        exit()

    label, alert = predict_frame(frame)
    print(f"Detected: {label} -> {alert}")
