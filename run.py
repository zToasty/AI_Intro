import argparse
from pathlib import Path
from ultralytics import YOLO


def run_inference(weights_path: str, input_dir: str, output_dir: str):
    model = YOLO(weights_path)
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    image_paths = list(input_dir.glob("*.jpg")) + list(input_dir.glob("*.png")) + list(input_dir.glob("*.jpeg"))

    if not image_paths:
        print("Нет изображений в указанной папке.")
        return

    for image_path in image_paths:
        result = model(image_path, save=True, save_txt=True, project=str(output_dir), name=image_path.stem)

    print(f"Обработка завершена. Результаты сохранены в: {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLO inference по изображениям в папке")
    parser.add_argument("--weights", type=str, required=True, help="Путь к файлу весов YOLOv8 (например, best.pt)")
    parser.add_argument("--input_dir", type=str, required=True, help="Папка с изображениями")
    parser.add_argument("--output_dir", type=str, required=True, help="Куда сохранять результаты")
    args = parser.parse_args()

    run_inference(args.weights, args.input_dir, args.output_dir)
