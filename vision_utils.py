import easyocr
from ultralytics import YOLO


def reading_text(image):
    reader = easyocr.Reader(['pt'])
    result = reader.readtext(image)

    for (bbox, text, prob) in result:
        if prob >= 0.80:
            return text
    


# detectando o onibus

def detecting_bus(frame):
    
    ncnn_model = YOLO('modelos\yolo11n_ncnn_model')

    results = ncnn_model.predict(frame, save=False, classes=5, half=True, save_conf=False, save_txt=False)

    for detection in results[0].boxes.data:
        x_min, y_min, x_max, y_max, confidence, class_id = detection
        return confidence 
    
    return .4