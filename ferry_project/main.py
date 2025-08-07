def add_vehicle():
    vehicle_type = input("Araç bilgisi gir:")
    car_dct = {}
    motorcycle_dct = {}
    truck_dct = {}
    vehicle_all = {}
    vehicle_all.update(car_dct)
    vehicle_all.update(motorcycle_dct)
    vehicle_all.update(truck_dct)
    if (vehicle_type.lower() == "car"):
        car_brand = input(str("Arabanın markası:"))
        car_number_plate = input(str("Arabanızın plakasını giriniz:"))
        car_dct["vehicle_type"] = vehicle_type
        car_dct["car_brand"] = car_brand
        car_dct["car_number_plate"] = car_number_plate
        print(car_dct)
    elif (vehicle_type.lower() == "motorcycle"):
        motorcycle_brand = input(str("Motorsikletinizin markası:"))
        motorcycle_number_plate = input(str("Motorsikletinizin plakasını giriniz"))
        motorcycle_dct["vehicle_type"] = vehicle_type
        motorcycle_dct["motorcycle_brand"] = motorcycle_brand
        motorcycle_dct["motorcycle_number_plate"] = motorcycle_number_plate
        print(motorcycle_dct)
    elif (vehicle_type.lower() == "truck"):
        truck_brand = input(str("Kamyonuzun markası:"))
        truck_number_plate = input(str("Kamyonuzun plakasını giriniz"))
        truck_dct["vehicle_type"] = vehicle_type
        truck_dct["truck_brand"] = truck_brand
        truck_dct["truck_number_plate"] = truck_number_plate
        print(truck_dct)
    else:
        print("Geçersiz araç!")
    print("Mevcut kayıtlar", vehicle_all)
add_vehicle()


def del_vehicle():
    vehicle_all = {}
    number_plate = input("Silmek istediğiniz araç plakası")
    if number_plate in vehicle_all:
        silinen = vehicle_all.pop(number_plate)  
        print(f"{number_plate}:{silinen},silindi.")
del_vehicle()
      
    
     
