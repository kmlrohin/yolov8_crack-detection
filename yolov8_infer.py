from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
model.predict(source=r"C:\Users\rohin\Desktop\NewData\project20.12.22\yolov8 model\Best Dunks Of The 2021-22 NBA Season 🔥🔥.mp4", show= True) # accepts all formats - img/folder/vid.*(mp4/format). 0 for webcam


