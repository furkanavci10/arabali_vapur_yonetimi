try:
    from ..main import add_vehicle, del_vehicle, updat_vehicle, lst_vehicle
    from ..db.connection import sync_full
except ImportError:
    # Dosya olarak çalıştırılıyorsa burası devreye girer:
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
    from ferry_project.main import add_vehicle, del_vehicle, updat_vehicle, lst_vehicle
    from ferry_project.db.connection import sync_full

def menu():
    while True:
        print("1 - Ekle")
        print("2 - Sil ")
        print("3 - Güncelle")
        print("4 - Listele ")
        print("0 - Programı kapat ")

        try:
            secim = int(input("> "))
        except ValueError:
            print("Lütfen sadece sayı giriniz")
            continue

        if secim == 1:
            add_vehicle()
            sync_full()      # yeni/güncel/silinmiş verileri DB ile eşitle
        elif secim == 2:
            del_vehicle()
            sync_full()
        elif secim == 3:
            updat_vehicle()
            sync_full()
        elif secim == 4:
            lst_vehicle()    # okuma işlemi, DB’ye yazmaya gerek yok
        elif secim == 0:
            print("Programdan çıkılıyor")
            break
        else:
            print("Geçersiz seçim")

if __name__ == "__main__":
    menu()



    





