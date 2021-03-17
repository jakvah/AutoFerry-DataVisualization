import time
import mariadb as db
import sys

# Will scan through txt file every READ_INTERVAL seconds
READ_INTERVAL = 10

# Change path to match the location of your unity project path
TXT_FILE = r"C:\Users\jakob\Documents\NTNU\EiT\Gemini\Gemini-Unity\Assets\Scripts\temp.txt"
def get_db_connection():
    try:
        conn = db.connect(
            user = "root",
            password = "eit123",
            host = "localhost",
            database = "eit"
        )
        return conn
    except db.Error as e:
        print(f"Error connection to the datbase: {e}")
        return None

def clear_table(table_name):
    conn = get_db_connection()
    cur = conn.cursor()

    query = f"DELETE FROM {table_name}"
    cur.execute(query)
    conn.commit()
    conn.close()

def insert_coordinates(x,y,name):
    conn = get_db_connection()
    cur = conn.cursor()

    query = f"INSERT INTO {name} (x,z) VALUES (?,?)"
    cur.execute(query,(float(x),float(y)))
    conn.commit()
    conn.close()

def main():
    print("Clearing tables...")
    clear_table("ojb1")
    clear_table("ojb2")
    clear_table("ojb3")
    
    obj_1_counter = 1
    obj_2_counter = 2
    obj_3_counter = 3
    
    print("Running infinte while loop! Kill with Ctrl + C")
    while True:
        pos_file = open(TXT_FILE,"r")
        try:
            for i,line in enumerate(pos_file):
                if i == obj_1_counter:
                    # Obj 1
                    x = line.split(",")[0]
                    z = line.split(",")[2]
                    insert_coordinates(x,z,"ojb1")
                    obj_1_counter += 3

                elif i == obj_2_counter:
                    # Obj 2
                    x = line.split(",")[0]
                    z = line.split(",")[2]
                    insert_coordinates(x,z,"ojb2")

                    obj_2_counter += 3

                elif i == obj_3_counter:
                    # Obj 3
                    x = line.split(",")[0]
                    z = line.split(",")[2]
                    insert_coordinates(x,z,"ojb3")

                    obj_3_counter += 3
        except Exception as e:
            print(e)
        
        pos_file.close()
        print(f"Scanned through file. Will update file in {READ_INTERVAL} seconds.")
        time.sleep(READ_INTERVAL)
    
main()
