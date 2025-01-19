from gtts import gTTS
import csv
import time


# lendo e armazenando todos os destinos do arquivo csv


destinos = []

pegando_strs = True
download_mp3 = True
if pegando_strs:
    with open('bus-dict-csv/mydb.csv', mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            dest = linha[4]
            dest = dest.split()
            resolvido = []
            for word in dest:
                # removendo os pontos finais
                if word[-1] == '.':
                    resolvido.append(word.replace('.', ''))
                if word == '-':
                    resolvido.append(word.replace('-', '_'))
                
                resolvido.append(word)
                if len(resolvido) == len(dest):
                    destinos.append(''.join(resolvido))
                    resolvido = []

        print('primeira etapa completa com sucesso')

time.sleep(2)
print('Passando para a segunda etapa..')
time.sleep(3)
num = 0
if download_mp3:
    for texto in destinos:
        num += 1
        tts = gTTS(texto, lang='pt', tld="com.br")
        tts.save(f"vozes/{texto}.mp3")
        print(f'{num}')

print("Audios prontos!")
        
