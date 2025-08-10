import psycopg2
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from main import vehicle_all

try:
    # Bağlantı bilgilerini kendi PostgreSQL ayarlarına göre değiştir
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="mydb",   # bağlanmak istediğin veritabanı
        user="postgres",   # kullanıcı adı
        password="1234"    # parola
    )

    # Cursor oluştur
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS vehicles(
            number_plate TEXT PRIMARY KEY,
            vehicle_type TEXT,
            brand TEXT    );
    """)
    conn.commit()
    print(vehicle_all)
    for plate, data in vehicle_all.items():
        cur.execute("""
        INSERT INTO vehicles (number_plate, vehicle_type, brand)
        VALUES (%s, %s, %s)
        ON CONFLICT (number_plate) DO NOTHING;
    """, (plate, data["vehicle_type"], data["brand"]))

    conn.commit()
    print("Veriler başarıyla kaydedildi.")

    cur.execute("SELECT * FROM vehicles")

    conn.commit()
    # İşlemlerden sonra kapat
    cur.close()
    conn.close()

except Exception as e:
    print("Bağlantı hatası:", e)