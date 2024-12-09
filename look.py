# Nesse arquivo vamos usar EasyOCR para reconhecer que um onibus chegou e entao reconhecer seu codigo

# retorna uma string

import cv2
import easyocr
import torch
import time

# especificando o modelo da IA

model = torch.hub.load('ultralytics/yolov5', 'yolov5', pretrained=True)

def taking_the_screenshot():
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


        
        
        if detecting_bus(frame): # detectando o onibus
            time.sleep(4) # espera 4 segundos
            cv2.imwrite('screenshot.png', frame) # cria o screenshot.png
            text, first_time = reading_text('screenshot.png') # pega o texto da leitura da imagem
            print(text)
            if first_time:
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()


def reading_text(image):
    reader = easyocr.Reader(['pt'])
    result = reader.readtext(image)

    for (bbox, text, prob) in result:
        if prob >= 0.80:
            return text, True


# detectando o onibus

def detecting_bus(frame):
    
    results = model(frame)

    detections = results.pred[0]

    for det in detections:
        if int(det[5]) == 0 and det[4] >= 0.60:
            return True
    
    
    return False

taking_the_screenshot()