# relative import: models paketi ferry_project içinde
from .models.vehicle import Vehicle, Car, Truck, Motorcycle

# Uygulama belleğindeki veriler
vehicle_all = {}

def add_vehicle():
    ls_type = ["car", "motorcycle", "truck"]
    while True:
        vehicle_type = input("Araç bilgisi gir:(car / motorcycle / truck): ").replace(" ", "").lower()
        if vehicle_type in ls_type:
            break
        print("Lütfen geçerli araç tiplerinden birini giriniz.")
    number_plate = input("Aracınızın plakası: ").replace(" ", "").lower()
    brand = input("Aracınızın markası: ").replace(" ", "").lower()

    if vehicle_type == "car":
        vehicle_all[number_plate] = {"vehicle_type": vehicle_type, "brand": brand}
    elif vehicle_type == "motorcycle":
        vehicle_all[number_plate] = {"vehicle_type": vehicle_type, "brand": brand}
    elif vehicle_type == "truck":
        vehicle_all[number_plate] = {"vehicle_type": vehicle_type, "brand": brand}
    else:
        print("Geçersiz araç!")
        return

    print("Mevcut kayıtlar:", vehicle_all)

def del_vehicle():
    dl_vehicle = input("Silmek istediğiniz aracın plakası: ").replace(" ", "").lower()
    print(f"Girilen plaka: {dl_vehicle}")
    if dl_vehicle in vehicle_all:
        vehicle_all.pop(dl_vehicle)
        print(f"{dl_vehicle} plakalı araç silindi.")
    else:
        print(f"{dl_vehicle} plakalı araç bulunamadı.")

def updat_vehicle():
    updt_vehicle = input("Güncellemek istediğiniz aracın plakası: ").replace(" ", "").lower()
    if updt_vehicle in vehicle_all:
        lst_type = ["car", "motorcycle", "truck"]
        while True:
            new_type = input("Yeni araç tipi (car/motorcycle/truck): ").replace(" ", "").lower()
            if new_type in lst_type:
                break
            print("Lütfen geçerli araç tiplerinden birini giriniz.")
        new_brand = input("Yeni girmek istediğiniz araç markası: ").replace(" ", "").lower()
        vehicle_all[updt_vehicle] = {"vehicle_type": new_type, "brand": new_brand}
        print(f"{updt_vehicle} plakalı araç güncellendi.")
    else:
        print(f"{updt_vehicle} plakalı araç bulunamadı.")

def lst_vehicle():
    lt_vehicle = input("Listelemek istediğiniz aracın plakası (tümü için boş bırakın): ").replace(" ", "").lower()
    if lt_vehicle:
        x = vehicle_all.get(lt_vehicle)
        print(x if x else "Plakalı araç bulunamadı.")
    else:
        print(vehicle_all)
