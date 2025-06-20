# YOLOv8 Inference Submit

Инференс по изображениям с использованием модели YOLOv8n (`best.pt`)

---

## Старт!

```bash
git clone https://github.com/zToasty/AI_Intro.git
cd AI_Intro
```
## Создайте Виртуальное окружение
```bash
python -m venv venv

ИЛИ

python3 -m venv venv
```
## Активируйте Виртуальное окружение
🔵 Windows
```bash
venv\Scripts\activate
```
🟢 Linux 
```bash
source venv/bin/activate
```
## Установка зависимостей
```bash
python -m pip install --upgrade pip
pip install ultralytics
```

## Пример запуска
```bash
python run.py --weights best.pt --input_dir путь\к\изображениям --output_dir путь\куда\сохранять

python run.py --weights best.pt --input_dir images/ --output_dir results/
```

## Веса в репозитории:

```best.pt```  Обучались на датасете Heridal

