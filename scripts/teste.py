dest = 'TERM. SAPOPEMBA - TEOTÔNIO VILELA - TERM. PQ. D.PEDRO II'

dest = dest.split()
resolvido = []
for word in dest:
    # removendo os pontos finais
    if word[-1] == '.':
        resolvido.append(word.replace('.', ''))
        continue
    elif word == '-':
        resolvido.append(word.replace('-', '_'))
        continue
    
    resolvido.append(word)
    if len(resolvido) == len(dest):
        resolvido = []


print(resolvido)