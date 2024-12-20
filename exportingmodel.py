import onnx
from ultralytics import YOLO

# codigo para exportar o modelo original para o formato otimizado

model = YOLO('treinado.pt')
model.export('onnx')

# codigo para checar o novo modelo otimizado

valid = False # so coloquei esse "if" para rodar as partes do codigo separadamente
if valid:
    model = onnx.load("model_requantized.onnx")
    onnx.checker.check_model(model)
    print("Modelo ONNX validado hehe")

    for node in model.graph.node:
        print(f"Nome: {node.name}, Operação: {node.op_type}")
