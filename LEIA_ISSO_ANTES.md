# Como funciona essa coisa

## Arquivo Look.py:

- esse arquivo tem a logica ficar tirando as fotos para as deteccoes e la tem o modelo treinado original se voce quiser testar, **so rodar o arquivo**

## Exportacao e teste:

- No arquivo exportingmodel.py so exporto o modelo e posso ativar um outro codigo para checar se ta tudo certo

- O arquivo treinado.pt e o modelo treinado original

- O arquivo treinado.onnx e o modelo otimizado pro rasp

- No arquivo testOptimized.py voce vai ver que o codigo e dividido em duas partes, fazer a deteccao e tentar conseguir o nivel de confianca, a partir do momento que tentei conseguir o nivel de confianca ja deixei d entender oq tava acontecendo kkkkk

## Meus palpites do pq nao ta dando certo:

- Talvez o modelo otimizado nao tenha sido exportado ou configurado da maneira correta(so segui um tutorial qnd fui fzr) e isso caga os dados que estao sendo retornados

- Talvez os dados estejam cagados por causa de um mau tratamento usando a biblioteca numpy(nao faco ideia cmo usar ela direito) porque ela tem varios termos e operacoes que nunca vi antes.