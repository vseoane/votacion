import pymysql.connector

NOMBRE_DB = 'votacionesdb'
HOST = ''

def main():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db=NOMBRE_DB)
    cur = conn.cursor()
    cur.execute("SELECT Host,User FROM user")
    print(cur.description)
    print()
    for row in cur:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
