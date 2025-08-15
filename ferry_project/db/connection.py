import psycopg2
import os

def sync_full():
    # RAM'deki sözlüğü al (relative import!)
    from ..main import vehicle_all

    conn = None
    cur = None
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "127.0.0.1"),
            port=int(os.getenv("DB_PORT", "5432")),
            dbname=os.getenv("DB_NAME", "mydb"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "postgres"),
            sslmode=os.getenv("DB_SSLMODE", "prefer"),
        )
        cur = conn.cursor()

        # Tabloyu garanti et
        cur.execute("""
            CREATE TABLE IF NOT EXISTS vehicles(
                number_plate TEXT PRIMARY KEY,
                vehicle_type TEXT,
                brand        TEXT
            );
        """)

        # DB'deki ve RAM'deki plakaları karşılaştır
        cur.execute("SELECT number_plate FROM vehicles;")
        db_plates = {row[0] for row in cur.fetchall()}
        mem_plates = set(vehicle_all.keys())

        # 1) Yeni plakalar → INSERT (çatışmada DO NOTHING)
        for plate in (mem_plates - db_plates):
            data = vehicle_all[plate]
            cur.execute("""
                INSERT INTO vehicles (number_plate, vehicle_type, brand)
                VALUES (%s, %s, %s)
                ON CONFLICT (number_plate) DO NOTHING;
            """, (plate, data.get("vehicle_type"), data.get("brand")))

        # 2) Ortak plakalar → UPDATE
        for plate in (mem_plates & db_plates):
            data = vehicle_all[plate]
            cur.execute("""
                UPDATE vehicles
                SET vehicle_type=%s, brand=%s
                WHERE number_plate=%s;
            """, (data.get("vehicle_type"), data.get("brand"), plate))

        # 3) RAM'de olmayan ama DB'de duranlar → DELETE
        for plate in (db_plates - mem_plates):
            cur.execute("DELETE FROM vehicles WHERE number_plate=%s;", (plate,))

        conn.commit()
        print("DB RAM ile senkronize edildi.")

    except Exception as e:
        print("Bağlantı/Senkron hatası:", e)
    finally:
        if cur: cur.close()
        if conn: conn.close()
