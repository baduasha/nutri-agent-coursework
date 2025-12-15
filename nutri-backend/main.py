from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io

from transformers import pipeline

app = FastAPI(title="NutriAgent API", version="1.0")

# Готовая food-модель (Food-101). Док: модель на HF. 
classifier = pipeline("image-classification", model="nateraw/food", top_k=3)

# (можно расширять) — ккал/100г по популярным блюдам
KCAL_PER_100 = {
    "pizza": 260,
    "sushi": 140,
    "salad": 90,
    "ramen": 95,
    "hamburger": 295,
    "spaghetti_bolognese": 170,
    "fried_rice": 165,
    "ice_cream": 200,
    "cheesecake": 320,
    "spaghetti_carbonara": 190,
}

# (опционально) перевод названий — чтобы в приложении было по-русски
RU = {
    "pizza": "Пицца",
    "sushi": "Суши",
    "salad": "Салат",
    "ramen": "Рамен",
    "hamburger": "Бургер",
    "spaghetti_bolognese": "Паста болоньезе",
    "fried_rice": "Жареный рис",
    "ice_cream": "Мороженое",
    "cheesecake": "Чизкейк",
}

@app.post("/analyze")
async def analyze(image: UploadFile = File(...)):
    content = await image.read()

    try:
        img = Image.open(io.BytesIO(content)).convert("RGB")
    except Exception:
        return {"ok": False, "error": "file_is_not_image"}

    preds = classifier(img)  # top_k=3
    best = preds[0]
    label_raw = best["label"]
    confidence = float(best["score"])

    # в UI покажем по-русски, но сохраним raw
    label = RU.get(label_raw, label_raw)

    kcal_per_100 = KCAL_PER_100.get(label_raw, 200)

    return {
        "ok": True,
        "label": label,
        "label_raw": label_raw,
        "confidence": confidence,
        "kcalPer100": int(kcal_per_100),
        "top3": [{"label": p["label"], "score": float(p["score"])} for p in preds],
    }
