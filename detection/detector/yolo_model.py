from ultralytics import YOLO
from PIL import Image
import cv2
import matplotlib.pyplot as plt

model = YOLO('yolov8n.pt')  

def detect_objects(image_path):
    results = model.predict(image_path)
    annotated_image = results[0].plot(line_width=1)

    cv2.imwrite(image_path, annotated_image)

    return

