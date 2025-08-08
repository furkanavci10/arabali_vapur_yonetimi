import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import add_vehicle, del_vehicle, updat_vehicle, lst_vehicle

def menu():
    print("1 - Ekle")
    print("2 - Sil ")
    print("3 - Güncelle")
    print("4 - Listele ")
    print("0 - Programı kapat ")
    secim = int(input())
    try:
        if secim == 1:
            add_vehicle()
        elif secim == 2:
            del_vehicle()
        elif secim == 3:
            updat_vehicle()
        elif secim == 4:
            lst_vehicle()
        elif secim == 0:
            print("Programdan çıkılıyor")          
    except ValueError:
        print("Lütfen sadece sayı giriniz")
        


menu()


    





