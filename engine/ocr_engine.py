import easyocr
import numpy as np

class OCRAgent:
    def __init__(self):
        self.reader = easyocr.Reader(['en', 'id'])

    def extract_text(self, image_np):
        results = self.reader.readtext(image_np, detail=0)
        return " ".join(results)