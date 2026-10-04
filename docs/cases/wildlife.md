# Wildlife Recognition & Intrusion Alert System

**02 / Desktop prototype**

Combines YOLOv8 detection with species classification, then confirms danger events with confidence thresholds, repeated detections, and alert cooldowns.

## Inside the system

Video or webcam frames pass through YOLOv8, animal crops are classified with the existing Keras model, and confirmed danger events save evidence and detection metrics. SMS providers and registered recipients are configurable.

**Built with:** Python · TensorFlow / Keras · OpenCV · YOLOv8

## Current scope

PC-based prototype. YOLO provides broad animal bounding boxes; the classifier identifies species from crops. SMS is disabled by default and requires provider credentials.

[Source repository ↗](https://github.com/NoirPrimordial7/wildlife_intrusion_detection_system) · [Back to profile](../../README.md#selected-work)
