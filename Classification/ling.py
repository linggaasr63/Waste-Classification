import cv2
from ultralytics import YOLO

# Load your trained YOLOv8 model
model = YOLO('C:/Users/Ryu Aditya/Downloads/weights-20240711T045505Z-001/weights/best.pt')

# Initialize the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture image.")
        break
    
    # Perform detection
    results = model(frame)
    
    # Draw bounding boxes and labels on the frame
    for result in results[0].boxes.data:
        x1, y1, x2, y2, confidence, class_id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        
        # Draw the bounding box
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
        # Draw the label and confidence
        label = f"{model.names[int(class_id)]}: {confidence:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('YOLOv8 Real-Time Detection', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()
