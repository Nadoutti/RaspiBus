# Vai usar uma biblioteca para ler e falar a string
# retorna o arquivo de som ja pronto
# apaga o arquivo gerado para nao ficar ocupando espaco
import subprocess

def speak(destino:str):
    subprocess.run(["start", f"vozes/{destino}"], shell=True)
