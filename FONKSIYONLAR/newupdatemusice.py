import pygame
import time

def sarki_cal(sarki_yolu):
    pygame.init()
    pygame.mixer.init()
    
    try:
        pygame.mixer.music.load(sarki_yolu)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
    except Exception as e:
        print(f"Hata: {e}")
    finally:
        pygame.mixer.quit()

if __name__ == "__main__":
    sarki_yolu = "sarki.mp3"  # Çalmak istediğiniz şarkının dosya yolunu belirtin
    sarki_cal(sarki_yolu)