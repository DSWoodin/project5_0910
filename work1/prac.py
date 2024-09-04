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