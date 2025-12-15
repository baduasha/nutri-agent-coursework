# NutriAgent — агент-нутрициолог

Android-приложение для оценки калорийности блюд по фотографии.

## Функциональность
- Распознавание блюда по фото (ML-модель Food-101)
- Расчёт калорийности на 100 г
- Пересчёт калорий при изменении массы порции
- Работа с камерой и галереей

## Структура проекта
- NutriAgent.zip — Android-приложение (Jetpack Compose)
- nutri-backend.zip — backend (FastAPI + PyTorch + Transformers)

## Запуск backend
```bash
pip install fastapi uvicorn torch torchvision transformers timm accelerate
python -m uvicorn main:app --host 0.0.0.0 --port 8000
