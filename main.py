# No fim esse arquivo vai retornar a string da deteccao do onibus

from process import processing
from speak import speak
import cv2
from vision_utils import detecting_bus, reading_text
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
            break

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



if __name__ == '__main__':
    main_loop()
    