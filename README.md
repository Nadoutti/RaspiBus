# 🚌 RaspiBus

O **RaspiBus** é um projeto open source desenvolvido para **auxiliar pessoas com deficiência visual** a utilizarem o transporte público de São Paulo.  
Ele identifica os ônibus que passam por um ponto e **informa por áudio o destino do veículo**, permitindo maior autonomia e segurança na mobilidade urbana.

---

## 🎯 Objetivo

Facilitar a interação de pessoas com deficiência visual com o sistema de transporte público, oferecendo uma ferramenta acessível que **reconhece o ônibus pelo código exibido** e anuncia **para onde ele está indo**.

---

## ⚙️ Funcionalidades

- 📷 **Reconhecimento de ônibus por código** usando visão computacional.  
- 🔊 **Retorno em áudio** com o destino do ônibus.  
- 🧠 Utiliza **modelos de IA (YOLO + OCR)** para detecção e leitura das placas dos veículos.  
- 💡 Projetado para rodar em dispositivos de baixo custo, como o **Raspberry Pi**.  
- 🌍 Código aberto e em **desenvolvimento contínuo**.

---

## 🧰 Tecnologias Utilizadas

- **Python**  
- **Ultralytics (YOLO)** — para detecção de objetos (ônibus)  
- **EasyOCR** — para leitura do código numérico do ônibus  
- (Opcional: **PyAudio** ou **gTTS** para síntese de voz)

---

## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/RaspiBus.git
   cd RaspiBus
```

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o projeto:

   ```bash
   python main.py
   ```

---

## 🧩 Status do Projeto

🛠️ Em **desenvolvimento contínuo (open source)** — contribuições são bem-vindas!

---

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Faça commit das mudanças 
4. Envie um pull request

---

