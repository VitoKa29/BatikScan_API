from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np
from io import BytesIO
from PIL import Image

app = FastAPI()

print("Loading model...")
model = load_model("best_model.h5")
print("Model loaded!")

class_names = [
    "JawaBarat_Megamendung",
    "Kalimantan_CorakInsang",
    "Kalimantan_Dayak",
    "Papua_Cendrawasih",
    "Solo_Parang",
    "Tiongkok_IkatCelup",
    "Yogyakarta_Kawung"
]

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Validasi tipe file
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(
            status_code=400,
            detail="File harus berupa gambar dengan format JPG, JPEG, atau PNG."
        )

    contents = await file.read()
    img = Image.open(BytesIO(contents)).convert("RGB")
    img = img.resize((224, 224))

    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)[0]
    idx = np.argmax(preds)

    return {
        "predicted_class": class_names[idx],
        "confidence": round(float(preds[idx] * 100), 2),
        "probabilities": {class_names[i]: round(float(preds[i] * 100), 2) for i in range(len(class_names))}
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
