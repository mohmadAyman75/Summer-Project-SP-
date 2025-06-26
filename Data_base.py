import sqlite3



class Data_Base:
    def __init__(self):
        self.ID=0
        self.Name=""
        self.__user_Name=""
        self.__pass=0
        self.__url="C:\\my\\Projectes\\Summer Proejct (SP)\\Main Fill of SP\\library_DB.db"

    def get_ID(self):
        try:
            self.ID=int(input("Enter ID:"))
            if self.ID<0:
                raise
            else:
                return self.ID
        except Exception:
            print("invaild input try again:")


    def get_recent_book(self):   #abstract method
        self.ID=int(input("Enter ID:"))
        print("ID:",self.ID)
        pass



    def check_ID_in_table(self):
        pass



    def get_info_book(self):
        db=Data_Base()
        self.ID=db.get_ID()

        conn=sqlite3.connect(self.__url)
        cursor=conn.cursor()
        db.check_ID_in_table()
        def db():
            data=cursor.execute("SELECT info FROM Books WHERE id = ?",(self.ID,)).fetchall()
            if data:
                return 1
            else:
                return 0

        if db():
            Name_of_book=cursor.execute("SELECT name FROM books WHERE id = ?",(self.ID,)).fetchall()
            cursor.execute("SELECT info FROM Books WHERE id=?",(self.ID,))
            data=cursor.fetchall()
            print(f"Name:{Name_of_book[0]}\ninforamtion:{data[0]}")



    def get_branch_of_book(self):
        db=Data_Base()
        self.ID=db.get_ID()
        conn=sqlite3.connect(self.__url)
        cursor=conn.cursor().execute("SELECT branch_id FROM Books WHERE id=?",(self.ID,))
        branch_id=cursor.fetchall()
        print(branch_id)


    def check_login(self):
        #1=user ,2=librarian ,3=manager ,0=False
        self.__user_Name=input("Enter User_name:")
        self.__pass=input("Enter Password:")
        conn=sqlite3.connect(self.__url)
        user_name=conn.cursor().execute("SELECT user_name FROM Log_in WHERE user_name=?",(self.__user_Name,)).fetchall()
        password=conn.cursor().execute("SELECT pass FROM Log_in WHERE pass=?",(self.__pass,)).fetchall()
        self.ID=conn.cursor().execute("SELECT user_id FROM Log_in WHERE user_name=?",(self.__user_Name,)).fetchall()
        if(user_name and password and self.ID!=[(None,)]):
            print(self.ID)
            return 1
        self.ID = conn.cursor().execute("SELECT librarian_id FROM Log_in WHERE user_name=?",(self.__user_Name,)).fetchall()
        if(user_name and password and self.ID!=[(None,)]):
            return 2
        self.ID = conn.cursor().execute("SELECT manager_id FROM Log_in WHERE user_name=?",(self.__user_Name,)).fetchall()
        if(user_name and password and self.ID!=[(None,)]):
            return 3
        else:
            return 0


    def update(self):
        pass


    def search(self):
        pass

    def number_of_copies(self):
        pass

    def add_new(self):
        #stuff or user
        pass

    def remove(self):
        pass

    def add(self):
        #bounes
        pass
db=Data_Base()
print(db.check_login())