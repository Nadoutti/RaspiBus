import onnxruntime as ort
import cv2
import numpy as np

# Carregar o modelo quantizado
session = ort.InferenceSession("treinado.onnx", providers=["CPUExecutionProvider"])
input_name = session.get_inputs()[0].name

# Carregar a imagem real
image_path = "testandoonibus.jpg"  # caminho para a imagem
image = cv2.imread(image_path)  # Ler a imagem no formato BGR
if image is None:
    raise ValueError(f"Imagem não encontrada no caminho: {image_path}")

# Pré-processar a imagem
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Converter para RGB
image_resized = cv2.resize(image_rgb, (640, 640))  # Redimensionar para (640, 640)
image_transposed = np.transpose(image_resized, (2, 0, 1))  # Reorganizar para CHW
image_normalized = image_transposed.astype(np.float32) / 255.0  # Normalizar para [0, 1]
input_tensor = np.expand_dims(image_normalized, axis=0)  # Adicionar dimensão do batch



outputs = session.run(None, {input_name: input_tensor}) # essa linha que faz a deteccao de fato

# daqui pra baixo e so codigo do gpt tentando conseguir o nivel de confianca


# Pós-processar as saídas
detections = outputs[0]  # A saída principal do modelo
print(f"Formato da saída: {detections.shape}")
print(f"Primeiros valores brutos: {detections[:5]}")

# Decodificação das detecções
boxes = detections[:, :4]  # Coordenadas das caixas delimitadoras (x, y, w, h)
confidences = detections[:, 4]  # Confiança dos objetos

# Verificar se há scores de classes na saída
if detections.shape[1] > 5:
    class_scores = detections[:, 5:]  # Pontuações das classes
else:
    print("A saída do modelo não contém pontuações de classes. Verifique a configuração do modelo.")
    class_scores = None

# Filtrar detecções com confiança baixa
threshold = 0.5  # Ajuste o limiar conforme necessário
indices = np.where(confidences > threshold)[0]

for idx in indices:
    box = boxes[idx]
    confidence = confidences[idx]

    if class_scores is not None and class_scores[idx].size > 0:
        class_id = np.argmax(class_scores[idx])
        class_confidence = class_scores[idx][class_id]
        print(f"Detecção: Classe {class_id}, Confiança {confidence:.2f}, Classe Confiança {class_confidence:.2f}")
    else:
        print(f"Detecção sem classes: Confiança {confidence:.2f}")
    
    print(f"Caixa: {box}")

print("Inferência concluída com a imagem real!")
