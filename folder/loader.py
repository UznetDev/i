import json
import logging
import time
import mysql.connector


class DB:
    def __init__(self,file):
        self.file = file
        try:
            with open(self.file, "r") as f:
                self.data = f.read()
        except (FileNotFoundError, json.JSONDecodeError):
            with open(self.file, "w") as f:
                f.write('57289')
            with open(self.file, "r") as f:
                self.data = f.read()
            logging.info(f' create table in file{file}')

    def get_count(self):
        with open(self.file, "r") as f:
            return int(f.read())

    def update_count(self, count):
        with open(self.file, "w") as f:
            f.write(str(count))


file_db = DB('data.db')


class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            autocommit=True
        )
        self.cursor = self.connection.cursor()

    def create_table(self):
        try:
            sql = """
            CREATE TABLE IF NOT EXISTS music (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message_id INT,
                file_id VARCHAR(250),
                file_unique_id VARCHAR(50),
                duration INT,
                performer VARCHAR(200),
                subject VARCHAR(200),
                title VARCHAR(200),
                file_name VARCHAR(200),
                mime_type VARCHAR(100),
                file_size INT,
                view_count INT,
                like_count INT,
                dislike_count INT)
            """
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as err:
            logging.error(err)
            self.reconnect()

    def add_data(self,message_id, file_id, file_unique_id, duration, performer, subject, title, file_name, mime_type, file_size):
        try:
            sql = """
            INSERT INTO `music`(`message_id`, `file_id`, `file_unique_id`, `duration`, `performer`, `subject`, `title`, `file_name`, `mime_type`, `file_size`) 
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            values = (message_id, file_id, file_unique_id, duration, performer, subject, title, file_name, mime_type, file_size)
            self.cursor.execute(sql, values)
            self.connection.commit()
        except Exception as err:
            self.reconnect()
            logging.error(err)

    def remove_music(self, file_unique_id):
        try:
            sql = "DELETE FROM `music` WHERE file_unique_id=%s"
            values = (file_unique_id, )
            self.cursor.execute(sql, values)
            self.connection.commit()
        except Exception as err:
            self.reconnect()
            logging.error(err)

    def count_music(self):
        try:
            sql = "SELECT COUNT(*) FROM `music`;"
            self.cursor.execute(sql)
            result = self.cursor.fetchone()
            return result[0]
        except Exception as err:
            self.reconnect()
            logging.error(err)


    def check_music(self, file_unique_id):
        try:
            self.cursor.execute("SELECT * FROM `music` WHERE `file_unique_id`=%s",
                                (file_unique_id,))
            result = self.cursor.fetchone()
            return result
        except Exception as err:
            self.reconnect()
            logging.error(err)

    def update_music(self, message_id, file_id, duration, performer, subject, title, file_name, mime_type, file_size, file_unique_id):
        try:
            sql = """
            UPDATE `music` SET `message_id`=%s,`file_id`=%s, `duration`=%s,`performer`=%s,`subject`=%s,`title`=%s,`file_name`=%s,`mime_type`=%s,`file_size`=%s WHERE file_unique_id=%s
            """
            value = (message_id, file_id, duration, performer, subject, title, file_name, mime_type, file_size, file_unique_id)
            self.cursor.execute(sql, value)
            self.connection.commit()
        except Exception as err:
            logging.error(err)
            self.reconnect()



    def reconnect(self):
        try:
            try:
                self.connection.close()
            except:
                pass
            time.sleep(1)
            try:
                self.connection = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    database=self.database,
                    autocommit=True
                )
                self.cursor = self.connection.cursor()
                logging.info('mysql reconnect')
            except Exception as err:
                logging.error(err)
        except Exception as err:
            logging.error(err)

    def __del__(self):
        try:
            self.connection.close()
        except Exception as err:
            self.reconnect()
            logging.error(err)
            
 db = Database(host='localhost', user='project', password='myproject', database='project')
