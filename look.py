# No fim esse arquivo vai retornar a string da deteccao do onibus

from ultralytics import YOLO
import cv2
import easyocr
import time


model = YOLO("treinado.pt") # aqui carrego o modelo que treinei

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
    
    results = model.predict(frame, show=True, save=True)
    print(results)


detecting_bus('testandoonibus.jpg')