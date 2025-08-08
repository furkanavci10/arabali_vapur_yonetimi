from models.vehicle import Vehicle,Car,Truck,Motorcycle


vehicle_all = {}

def add_vehicle():
    ls_type = ["car","motorcycle","truck"]
    while True:
        vehicle_type = input("Araç bilgisi gir:(car / motorcycle / truck):").replace(" ", "").lower()
        if vehicle_type in ls_type:
            break
        else:
            print("Lütfen geçerli araç tiplerinden birini giriniz.")
    number_plate = input("Aracınızın plakasını giriniz:").replace(" ", "").lower()
    brand = input("Aracınızın markası:").replace(" ", "").lower()
    if vehicle_type.lower() == "car":
        vehicle_all[number_plate] = {
            "vehicle_type" : vehicle_type,
            "brand" : brand
        }
        
    elif (vehicle_type.lower() == "motorcycle"):
        vehicle_all[number_plate] = {
            "vehicle_type" : vehicle_type,
            "brand" : brand
        }
        
    elif (vehicle_type.lower() == "truck"):
        vehicle_all[number_plate] = {
            "vehicle_type" : vehicle_type,
            "brand" : brand
        }

    else:
        print("Geçersiz araç!")
 
    print("Mevcut kayıtlar", vehicle_all)



def del_vehicle():
    global vehicle_all
    dl_vehicle = input("Silmek istediğiniz aracın plakası :").replace(" ", "").lower()
    print(f"Girilen plaka:, {dl_vehicle}")
    if dl_vehicle in vehicle_all:
        vehicle_all.pop(dl_vehicle)  
        print(f"{dl_vehicle}, Plakalı araç silindi.")
            
    else:
        print(f"{dl_vehicle} Plakalı araç bulunamadı.")    

      
def updat_vehicle():
    global vehicle_all
    updt_vehicle = input("Güncellemek istediğiniz aracın plakası :").replace(" ", "").lower()
     
    if updt_vehicle in vehicle_all:
        print(f"Girilen araç plakası, {updt_vehicle}")
        lst_type = ["car","motorcycle","truck"]
        while True:
            new_type = input("Yeni araç bilgisi gir:(car / motorcycle / truck:").replace(" ", "").lower()
            if  new_type in lst_type:
                break
            else:
                print("Lütfen geçerli araç tiplerinden birini giriniz.")
        new_brand = input("Yeni girmek istediğiniz araç markası:").replace(" ", "").lower()        

        vehicle_all[updt_vehicle] = {
            "vehicle_type" : new_type,
            "brand" : new_brand
        }
        print(f"{updt_vehicle}, Plakalı araç güncellendi")
    else:
        print(f"{updt_vehicle}, Plakalı araç bulunamadı")    


def lst_vehicle():
    global vehicle_all
    lt_vehicle = input("Listelemek istediğiniz aracın plakası :").replace(" ", "").lower()
    
    if lt_vehicle in vehicle_all:
        x = vehicle_all[lt_vehicle]
        print(x)
    else:
        print("Plakalı araç bulunamadı.")    

