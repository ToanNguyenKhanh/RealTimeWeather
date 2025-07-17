from api_request import fetch_data
import psycopg2

def connect_to_db():
    print("Connecting to PostgreSQL database...")
    try:
        connection = psycopg2.connect(
            host="db", # docker services
            port=5432,
            dbname="db",
            user="db_user",
            password="db_password"

        )
        return connection
    except psycopg2.OperationalError:
        print("Database connection failed.")
        raise

def create_tables(connection):
    print("Creating tables...")
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_weather_data(
                id SERIAL PRIMARY KEY,
                city TEXT,
                temperature FLOAT,
                weather_descriptions TEXT,
                wind_speed FLOAT,
                time TIMESTAMP,
                inserted_at TIMESTAMP DEFAULT NOW(),
                utc_offset TEXT    
            );
        """)
        connection.commit()
        print("Tables created successfully.")
    except psycopg2.Error as error:
        print(f"Error while connecting to PostgreSQL: {error}")
        raise

def insert_records(connection, data):
    print("Inserting records...")
    try:
        weather = data["current"]
        location = data["location"]
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                city,
                temperature,
                weather_descriptions,
                wind_speed,
                time,
                inserted_at,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """, (
            location["name"],
            weather["temperature"],
            weather["weather_descriptions"][0],
            weather["wind_speed"],
            location["localtime"],
            location["utc_offset"],
        ))
        connection.commit()
        print("Records inserted successfully.")
    except psycopg2.Error as error:
        print(f"Error while inserting records: {error}")
        raise

def main():
    try:
        data = fetch_data()
        connection = connect_to_db()
        create_tables(connection)
        insert_records(connection, data)
    except Exception as error:
        print(f"Error occurred: {error}")
    finally:
        if "connection" in locals():
            connection.close()
            print("Connection closed.")

if __name__ == "__main__":
    main()