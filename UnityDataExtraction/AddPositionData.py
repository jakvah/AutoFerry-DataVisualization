import time
import mariadb as db
import math

# Name of the tables containing position data for the 3 objects
TABLE_NAME_1 = "obj1_pos"
TABLE_NAME_2 = "obj2_pos"
TABLE_NAME_3 = "obj3_pos"

TABLE_NAME_1_SPEED = "obj1_speed"
TABLE_NAME_2_SPEED = "obj2_speed"
TABLE_NAME_3_SPEED = "obj3_speed"

username = "root"
pwd = "eit123"
host = "localhost"
database = "eit"

# Will scan through txt file every READ_INTERVAL seconds
READ_INTERVAL = 10

# Change path to match the location of your unity project path
TXT_FILE = r"C:\Users\jakob\Documents\NTNU\EiT\Gemini\Gemini-Unity\Assets\Scripts\temp.txt"

def get_db_connection():
    try:
        conn = db.connect(
            user=username,
            password=pwd,
            host=host,
            database=database
        )
        return conn
    except db.Error as e:
        print(f"Error connection to the database: {e}")
        return None


def clear_table(table_name):
    conn = get_db_connection()
    cur = conn.cursor()

    query = f"DELETE FROM {table_name}"
    cur.execute(query)
    conn.commit()
    conn.close()


def ned_to_llh(x, z):
    lat0 = 63.435167
    long0 = 10.392917
    re = 6378137
    Rn = re / math.sqrt(1 - 0.0818 ** 2 * math.sin(lat0))
    Rm = (Rn * (1 - 0.0818 ** 2)) / math.sqrt(1 - 0.0818 ** 2 * math.sin(lat0))
    llh_array = []
    lat = x * math.atan2(1, Rm) + lat0
    long = z * math.atan2(1, Rn * math.cos(lat0)) + long0
    llh_array.append(lat)
    llh_array.append(long)
    return llh_array


def calculate_speed(x, previous_x, z, previous_z, timestamp, previous_timestamp):
    distance = math.sqrt(pow(float(x) - previous_x, 2) + pow(float(z) - previous_z, 2))
    time_diff = int(timestamp) - int(previous_timestamp)

    speed = abs(distance / time_diff)
    return speed

def insert_coordinates(x, y, timestamp, name):
    conn = get_db_connection()
    cur = conn.cursor()

    query = f"INSERT INTO {name} (x,z,time) VALUES (?,?,?)"
    cur.execute(query, (x, y, timestamp))
    conn.commit()
    conn.close()


def insert_speed(speed, timestamp, name):
    conn = get_db_connection()
    cur = conn.cursor()

    query = f"INSERT INTO {name} (speed,time) VALUES (?,?)"
    cur.execute(query, (speed, timestamp))
    conn.commit()
    conn.close()


def main():
    print("Clearing tables...")
    clear_table(TABLE_NAME_1)
    clear_table(TABLE_NAME_2)
    clear_table(TABLE_NAME_3)

    print("Clearing speed tables...")
    clear_table(TABLE_NAME_1_SPEED)
    clear_table(TABLE_NAME_2_SPEED)
    clear_table(TABLE_NAME_3_SPEED)

    obj_1_counter = 1
    obj_2_counter = 2
    obj_3_counter = 3

    print("Running infinite while loop! Kill with Ctrl + C")
    while True:
        pos_file = open(TXT_FILE, "r")
        try:
            for i, line in enumerate(pos_file):
                if i == obj_1_counter:
                    # Obj 1
                    cords = line.split("@")[0]
                    timestamp = line.split("@")[1]
                    
                    x = cords.split(",")[0]
                    z = cords.split(",")[2]

                    if obj_1_counter > 1:
                        speed = calculate_speed(x, x_previous_1, z, z_previous_1, timestamp, timestamp_previous_1)
                        insert_speed(speed, timestamp_previous_1, TABLE_NAME_1_SPEED)
                    x_previous_1 = float(x)
                    z_previous_1 = float(z)
                    
                    timestamp_previous_1 = timestamp

                    boat1_array = ned_to_llh(float(x), float(z))

                    x_new = boat1_array[0]
                    z_new = boat1_array[1]
                    #print(x_new, z_new)
                    insert_coordinates(x_new, z_new, timestamp, TABLE_NAME_1)
                    obj_1_counter += 3

                elif i == obj_2_counter:
                    # Obj 2
                    cords = line.split("@")[0]
                    timestamp = line.split("@")[1]
                    x = cords.split(",")[0]
                    z = cords.split(",")[2]

                    if obj_2_counter > 2:
                        speed = calculate_speed(x, x_previous_2, z, z_previous_2, timestamp, timestamp_previous_2)
                        insert_speed(speed, timestamp_previous_2, TABLE_NAME_2_SPEED)
                    x_previous_2 = float(x)
                    z_previous_2 = float(z)
                    timestamp_previous_2 = timestamp

                    boat2_array = ned_to_llh(float(x), float(z))
                    x = boat2_array[0]
                    z = boat2_array[1]
                    #print(x, z)
                    insert_coordinates(x, z, timestamp, TABLE_NAME_2)

                    obj_2_counter += 3

                elif i == obj_3_counter:
                    # Obj 3cords = line.split("@")[0]
                    timestamp = line.split("@")[1]

                    x = cords.split(",")[0]
                    z = cords.split(",")[2]

                    if obj_3_counter > 3:
                        speed = calculate_speed(x, x_previous_3, z, z_previous_3, timestamp, timestamp_previous_3)
                        insert_speed(speed, timestamp_previous_3, TABLE_NAME_3_SPEED)
                    x_previous_3 = float(x)
                    z_previous_3 = float(z)
                    timestamp_previous_3 = timestamp

                    boat3_array = ned_to_llh(float(x), float(z))
                    x = boat3_array[0]
                    z = boat3_array[1]
                    #print(x, z)
                    insert_coordinates(x, z, timestamp, TABLE_NAME_3)

                    obj_3_counter += 3
        except Exception as e:
            print(e)

        pos_file.close()
        print(f"Scanned through file. Will update file in {READ_INTERVAL} seconds.")
        time.sleep(READ_INTERVAL)


main()
