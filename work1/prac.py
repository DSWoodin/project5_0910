import mysql.connector
from mysql.connector import Error

def create_connection():
    """ 데이터베이스와 연결을 생성하는 함수 """
    try:
        connection = mysql.connector.connect(
            host='localhost',          # 데이터베이스 서버 주소
            user='your_username',      # MySQL 사용자 이름
            password='your_password',  # MySQL 사용자 비밀번호
            database='your_database'   # 사용할 데이터베이스 이름
        )
        if connection.is_connected():
            print("MySQL 데이터베이스에 성공적으로 연결되었습니다.")
            return connection
    except Error as e:
        print(f"오류 발생: {e}")
        return None

def close_connection(connection):
    """ 데이터베이스 연결을 종료하는 함수 """
    if connection.is_connected():
        connection.close()
        print("MySQL 데이터베이스 연결이 종료되었습니다.")

def fetch_data(connection):
    """ 데이터베이스에서 데이터를 조회하는 함수 """
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM your_table")  # your_table을 조회하려는 테이블명으로 변경
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"오류 발생: {e}")

def insert_data(connection):
    """ 데이터베이스에 데이터를 삽입하는 함수 """
    try:
        cursor = connection.cursor()
        query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"  # your_table과 column1, column2를 실제 테이블과 컬럼으로 변경
        values = ("value1", "value2")  # 삽입할 데이터로 변경
        cursor.execute(query, values)
        connection.commit()
        print("데이터가 성공적으로 삽입되었습니다.")
    except Error as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    conn = create_connection()
    if conn:
        fetch_data(conn)
        insert_data(conn)
        close_connection(conn)