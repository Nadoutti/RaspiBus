dest = 'TERM. SAPOPEMBA - TEOTÔNIO VILELA - TERM. PQ. D.PEDRO II'

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
        resolvido = []


print(''.join(resolvido))