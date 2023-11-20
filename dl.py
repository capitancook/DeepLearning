


import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
image = cv2.imread("four dogs.jpg")
results = model(image)[0]