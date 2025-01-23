# No fim esse arquivo vai retornar a string da deteccao do onibus

from ultralytics import YOLO
from process import processing
from speak import speak
import cv2
import easyocr
import time
# model = YOLO("modelos\yolo11n_ncnn_model") # aqui carrego o modelo que treinei

def main_loop():
    cap = cv2.VideoCapture(0)

    if not cap:
        print('nao foi possivel acessar a camera')
        quit()

    while True:
        frame_true, frame = cap.read()


        if not frame_true:
            print('o frame nao foi validado')

        # mostrando a imagem numa janela
        cv2.imshow('Camera', frame)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
        
        if detecting_bus(frame) > 0.5:
            time.sleep(4) # espera 4 segundos
            cv2.imwrite('screenshot.png', frame) # cria o screenshot.png
            text = reading_text('screenshot.png') # pega o texto da leitura da imagem
            linha = processing(text)
            speak(linha)
            time.sleep(10)
            
            

    cap.release()
    cv2.destroyAllWindows()


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


main_loop()