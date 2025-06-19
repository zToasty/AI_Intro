# YOLOv8 Inference Submit

Инференс по изображениям с использованием модели YOLOv8n (`best.pt`) в рамках курса **"Введение в искусственный интеллект"**.

---

## 🚀 Бысткий старт

```bash
git clone https://github.com/zToasty/AI_Intro.git
cd AI_Intro

python -m venv venv
```
🔵 Windows
```bash
venv\Scripts\activate
```
🟢 Linux 
```bash
source venv/bin/activate
```
```bash
python -m pip install --upgrade pip
pip install ultralytics
```

Пример запуска
```bash
python run_inference.py --weights best.pt --input_dir путь\к\изображениям --output_dir путь\куда\сохранять

python run_inference.py --weights best.pt --input_dir images/ --output_dir results/
```

Веса в папке:

```best.pt```  Обучались на датасете Heridal

