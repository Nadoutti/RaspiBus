# Vai usar uma biblioteca para ler e falar a string
# retorna o arquivo de som ja pronto
# apaga o arquivo gerado para nao ficar ocupando espaco
import os

def speak(destino:str):
    os.system(f'start vozes/{destino}')
