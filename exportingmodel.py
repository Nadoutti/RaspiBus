import onnx
from ultralytics import YOLO

# codigo para exportar o modelo original para o formato otimizado
onnx1 = False
if onnx1:    
    model = YOLO('treinado.pt')
    model.export(format='onnx')

onnx2 = False
if onnx2:
    model = YOLO('treinado.pt')
    model.export(format='onnx', dynamic=True, simplify=True, nms=True, imgsz=640)

# codigo para checar o novo modelo otimizado

check_onnx = False # so coloquei esse "if" para rodar as partes do codigo separadamente
if check_onnx:
    model = onnx.load("model_requantized.onnx")
    onnx.checker.check_model(model)
    print("Modelo ONNX validado hehe")

    for node in model.graph.node:
        print(f"Nome: {node.name}, Operação: {node.op_type}")


ncnn = True
if ncnn:
    # Load a YOLO11n PyTorch model
    model = YOLO("treinado.pt")

    # Export the model to NCNN format
    model.export(format="ncnn")  # creates 'yolo11n_ncnn_model'

    # Load the exported NCNN model
    ncnn_model = YOLO("treinado_ncnn_model")

    # Run inference
    results = ncnn_model("testeonibus2.jpg")