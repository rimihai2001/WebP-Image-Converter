import sys
from PIL import Image
import os

def convert_to_webp(input_path: str):
    try:
        if not os.path.exists(input_path):
            print(f"Error: The file {input_path} does not exist.")
            return
        
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}.webp"

        with Image.open(input_path) as img:
            img.save(output_path, format="WEBP")
            print(f"Image successfully converted to {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python convert_to_webp.py <path_to_image>")
    else:
        input_path = sys.argv[1]
        convert_to_webp(input_path)
