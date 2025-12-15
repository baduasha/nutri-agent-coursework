# NutriAgent — агент-нутрициолог

Android-приложение для оценки калорийности блюд по фотографии.

## Что сделано

* Фото с камеры или выбор из галереи
* Распознавание блюда по фото (ML-модель Food-101 через backend)
* Возвращается: `label`, `confidence`, `kcalPer100`
* Пересчёт общей калорийности по массе порции (ползунок “граммы”)

## Структура репозитория

* `NutriAgent.zip` — Android-приложение (Kotlin + Jetpack Compose)
* `nutri-backend/` — backend (FastAPI + PyTorch + Transformers)
* `README.md` — описание и инструкция запуска

## Как запустить backend (Python/FastAPI)

Открой терминал и перейди в папку `nutri-backend`:

```bash
cd nutri-backend
python -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows:
# .venv\Scripts\activate

pip install fastapi uvicorn torch torchvision transformers timm accelerate pillow
python -m uvicorn main:app --host 0.0.0.0 --port 8000
```

После запуска сервер доступен по адресу:

* на компьютере: `http://127.0.0.1:8000`

## Подключение Android к backend

* Если запуск на **Android Emulator**: использовать `http://10.0.2.2:8000`
* Если запуск на **реальном телефоне** в одной Wi‑Fi сети:

  * узнать IP компьютера (пример: `192.168.0.8`)
  * использовать `http://<IP_компьютера>:8000`

## Как запустить Android-приложение

1. Скачать `NutriAgent.zip`
2. Распаковать
3. Открыть проект в Android Studio
4. Запустить на эмуляторе/устройстве
5. Убедиться, что backend запущен

## Примечание по точности

Результат распознавания зависит от качества фото и освещения. Для курсовой допускается погрешность (до ~30%) при оценке блюда/калорийности.
