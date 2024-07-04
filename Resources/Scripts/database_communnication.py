class database_communication:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection(db_file)

    def __create_connection(self, db_file):
        conn = sqlite3.connect(db_file)
        return conn

    def __close_connection(self, conn):
        if conn:
            conn.close()

    def insert_account(self, account_name, login_data, password, salt):
        sql = "INSERT INTO account (account_name, login_data, password, salt) VALUES (?, ?, ?, ?)"
        cursor = self.conn.cursor()
        cur.execute(sql, (account_name, login_data, password, salt))
        self.conn.commit()
        cur.close()
        self.__close_connection(self.conn)

    def insert_user(self, user_name, master_password, salt):
        sql = "INSERT INTO user (account_name, master_password, salt) VALUES (?, ?, ?)"
        cursor = self.conn.cursor()
        cur.execute(sql, (user_name, master_password, salt))
        self.conn.commit()
        cur.close()
        self.__close_connection(self.conn)

    def get_user_accounts(self, user_id):
        sql = "SELECT account_name FROM account WHERE user_id = ?"
        cursor = self.conn.cursor()
        cur.execute(sql, (user_id))
        accounts = cur.fetchall()
        cur.close()
        self.__close_connection(self.conn)
        return accounts

    def get_users(self):
        sql = "SELECT user_name FROM user"
        cursor = self.conn.cursor()
        cur.execute(sql)
        users = cur.fetchall()
        cur.close()
        self.__close_connection(self.conn)
        return users

    def check_user_credenntials(self, user_name):
        sql = "SELECT user_id FROM user WHERE master_password =?"
        cursor = self.conn.cursor()
        cur.execute(sql, (hashed_password))
        user_id = cur.fetchone()
        cur.close()
        self.__close_connection(self.conn)
        return user_id

        
