import torch
import cv2
import numpy as np
from PIL import Image
import yolov5
import os

# Load model
model = yolov5.load('turhancan97/yolov5-detect-trash-classification')

# Set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.agnostic = False  # NMS class-agnostic
model.multi_label = False  # NMS multiple labels per box
model.max_det = 1000  # Maximum number of detections per image

def object_detection(image_path, filename):
    # Read image
    img = Image.open(image_path)

    # Perform inference
    results = model(img, size=416)  # Use size=416 for better results on small objects

    # Parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4]  # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    # Load image again for drawing boxes
    image = cv2.imread(image_path)
    height, width, _ = image.shape

    # Create a list to hold the detected items
    text_list = []

    # Save original image to static folder for display
    original_image_path = os.path.join('static', 'télecharger', f'original_{filename}')
    cv2.imwrite(original_image_path, image)

    # Loop over all predictions
    for i in range(len(boxes)):
        if scores[i] > model.conf:  # Only consider high-confidence predictions
            x1, y1, x2, y2 = boxes[i].int().tolist()  # Convert tensor to integer and list

            # Draw bounding box on image
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

            # Draw label text
            label = f"{model.names[int(categories[i])]} {scores[i]:.2f}"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

            # Add label to the text_list
            text_list.append(label)

    # Save the processed image with bounding boxes to static folder
    processed_image_path = os.path.join('static', 'predict', f'{filename}')
    cv2.imwrite(processed_image_path, image)

    # Return both the original and processed image paths
    return original_image_path, processed_image_path, text_list
