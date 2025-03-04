# main.py test 2 ta rasimni solishtirish uchun:
import cv2
import numpy as np
from insightface.app import FaceAnalysis
from sklearn.metrics.pairwise import cosine_similarity

def load_and_prepare_image(image_path):
    # Rasmni yuklash va RGB formatga o'tkazish
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def get_face_embedding(image_path):
    # FaceAnalysis modelini ishga tushirish
    app = FaceAnalysis(providers=['CPUExecutionProvider'])
    app.prepare(ctx_id=0, det_size=(640, 640))
    
    # Rasmni yuklash
    img = load_and_prepare_image(image_path)
    
    # Yuzni aniqlash va embedding olish
    faces = app.get(img)
    
    if len(faces) == 0:
        raise ValueError("Rasmda yuz topilmadi!")
    
    # Birinchi topilgan yuzning 512 o'lchamli vektorini qaytarish
    return faces[0].embedding

def compare_faces(image1_path, image2_path):
    try:
        # Har bir rasm uchun embeddinglarni olish
        embedding1 = get_face_embedding(image1_path)
        embedding2 = get_face_embedding(image2_path)
        
        # Kosinus o'xshashligini hisoblash
        similarity = cosine_similarity(
            embedding1.reshape(1, -1),
            embedding2.reshape(1, -1)
        )[0][0]
        
        # Foizga aylantirish (0-1 oralig'idan 0-100 ga)
        similarity_percent = similarity * 100
        
        return similarity_percent
    
    except Exception as e:
        return f"Xatolik yuz berdi: {str(e)}"

# Foydalanish misoli
if __name__ == "__main__":
    # Rasm fayllarining yo'llarini kiriting
    image1_path = "2025-03-03-100920.jpg"
    image2_path = "faceid/config/data/aligned_dataset/001/o'ng.jpg"
    
    # O'xshashlikni hisoblash
    result = compare_faces(image1_path, image2_path)
    
    if isinstance(result, float):
        print(f"Rasmlar orasidagi o'xshashlik: {result:.2f}%")
    else:
        print(result)