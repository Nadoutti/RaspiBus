from ultralytics import YOLO


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