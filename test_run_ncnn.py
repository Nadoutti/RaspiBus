# aqui vai ficar o looping principal para o projeto
from ultralytics import YOLO


ncnn_model = YOLO('modelos\yolo11n_ncnn_model')

results = ncnn_model.predict('imagens/testeonibus1.jpg', save=False, classes=5, half=True, save_conf=False, save_txt=False)

for detection in results[0].boxes.data:
    x_min, y_min, x_max, y_max, confidence, class_id = detection
    print(f"Confianca: {confidence.item()}") 