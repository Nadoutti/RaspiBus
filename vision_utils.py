import os
import easyocr
from ultralytics import YOLO

# inicializando variaveis de vision e reading

llm_path = os.path.join("modelos", "yolo11n_ncnn_model")
ncnn_model = YOLO(llm_path)
reader = easyocr.Reader(['pt'])


def reading_text(image):
    result = reader.readtext(image)

    for (bbox, text, prob) in result:
        if float( prob ) >= 0.80:
            return text
    


# detectando o onibus

def detecting_bus(frame):
    

    results = ncnn_model.predict(frame, save=False, classes=5, half=True, save_conf=False, save_txt=False)

    for detection in results[0].boxes.data:
        x_min, y_min, x_max, y_max, confidence, class_id = detection
        return confidence 
    
    return .4
