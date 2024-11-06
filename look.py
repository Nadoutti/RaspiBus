# Nesse arquivo vamos usar EasyOCR para reconhecer que um onibus chegou e entao reconhecer seu codigo

# retorna uma string

import cv2
import easyocr


def taking_the_screenshot():
    cap = cv2.VideoCapture(0)

    if not cap:
        print('nao foi possivel acessar a camera')

    while True:
        frame_true, frame = cap.read()


        if not frame_true:
            print('o frame nao foi validado')
        
        # mostrando a imagem numa janela

        cv2.imshow('Camera', frame)


        # colocando o programa pra esperar por uma tecla
        key = cv2.waitKey(1)

        if key == ord('s'):
            cv2.imwrite('screenshot.png', frame)
            print('Tirou print')
            return True

        elif key == ord('q'):
            print('saindo')
            break

    cap.release()
    cv2.destroyAllWindows()


def reading_text(image):
    reader = easyocr.Reader(['pt'])
    result = reader.readtext(image)

    for (bbox, text, prob) in result:
        if prob >= 0.80:
            return text

# valid = taking_the_screenshot()

print(reading_text('screenshot.png')) 