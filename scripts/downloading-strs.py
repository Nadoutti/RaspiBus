from gtts import gTTS
import csv
import time


# lendo e armazenando todos os destinos do arquivo csv


destinos = {}

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
                    continue
                if word == '-':
                    resolvido.append(word.replace('-', '_'))
                    continue
                
                resolvido.append(word)
                if len(resolvido) == len(dest):
                    destinos[''.join(resolvido)] = linha[4]
                    resolvido = []

        print('primeira etapa completa com sucesso')

time.sleep(2)
print('Passando para a segunda etapa..')
time.sleep(3)
num = 0
if download_mp3:
    for nome, voz in destinos.items():
        num += 1
        tts = gTTS(voz, lang='pt', tld="com.br")
        tts.save(f"vozes/{nome}.mp3")
        print(f'{num}')

print("Audios prontos!")
        
# resolver a pronuncia da filha da puta 