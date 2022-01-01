import sqlite3, unittest

class DataBase():
    def __init__(self, name: str):
        self.__session = sqlite3.connect(name)
        self.__cursor = self.__session.cursor()
    
    def __del__(self):
        self.__session.close()

    @property
    def get_cursor(self):
        return(self.__cursor)


    @property
    def get_session(self):
        return(self.__session)

    def profile_info(self, id: int):
        request = 'SELECT phone_number, first_name, Last_name FROM user WHERE user_id = :id;'
        return self.__cursor.execute(request, {'id': id}).fetchall()
    
    def item_info(self, id: int):
        request = 'SELECT item_name, description FROM item WHERE item_id = :id;'
        return self.__cursor.execute(request, {'id': id}).fetchall()

    def orders_info(self, id: int):
        request = 'SELECT amount FROM orders WHERE order_id = :id;'
        return self.__cursor.execute(request, {'id': id}).fetchall()


class test(unittest.TestCase):
    def setUp(self):
        self.__tempdb = DataBase(':memory:')
        self.__tempdb.get_cursor.executescript(
            '''
            BEGIN TRANSACTION;
            CREATE TABLE IF NOT EXISTS "item" (
                    "item_id"       INTEGER,
                    "item_name"     TEXT,
                    "category"      TEXT,
                    "description"   TEXT,
                    PRIMARY KEY("item_id")
            );
            INSERT INTO item VALUES(1,'t-shirt#1','t-shirts','100% cotton');
            INSERT INTO item VALUES(2,'t-shirt#2','t-shirts','101% cotton');
            INSERT INTO item VALUES(3,'t-shirt#3','t-shirts','102% cotton');
            INSERT INTO item VALUES(4,'pencil1','pencils','for luck in exams');
            CREATE TABLE IF NOT EXISTS "User" (
                    "user_id"       INTEGER,
                    "username"      TEXT,
                    "password"      TEXT,
                    "first_name"    TEXT,
                    "Last_name"     TEXT,
                    "adress"        TEXT,
                    "phone_number"  TEXT,
                    "created_at"    TEXT,
                    UNIQUE("username"),
                    PRIMARY KEY("user_id")
            );
            INSERT INTO User VALUES(1,'AAAA','qwerty123','anton','pir','london','12335','02.01.2020');
            INSERT INTO User VALUES(2,'AAAAA','qwerty123','antony','piro','LA','123356','02.02.2020');
            INSERT INTO User VALUES(3,'AAAAAA','qwerty123','ars','pro','Moscow','1233567','03.02.2020');
            CREATE TABLE IF NOT EXISTS "orders" (
                    "order_id"      INTEGER,
                    "user_id_ord"   INTEGER,
                    "amount"        INTEGER,
                    "created_at"    TEXT,
                    "status"        INTEGER,
                    PRIMARY KEY("order_id"),
                    FOREIGN KEY("user_id_ord") REFERENCES "User"("user_id")
            );
            INSERT INTO orders VALUES(1,1,15,'01.01.2020',0);
            INSERT INTO orders VALUES(2,2,33,'02.01.2020',1);
            INSERT INTO orders VALUES(3,3,17,'02.01.2020',2);
            CREATE TABLE IF NOT EXISTS "cart_item" (
                    "user_id"       INTEGER,
                    "ord_id"        INTEGER,
                    "number"        INTEGER,
                    "price" INTEGER,
                    "cart_item_id"  INTEGER,
                    "item_id_cart"  INTEGER,
                    PRIMARY KEY("cart_item_id"),
                    FOREIGN KEY("user_id") REFERENCES "User"("user_id")
            );
            INSERT INTO cart_item VALUES(1,1,1,15,1,1);
            INSERT INTO cart_item VALUES(2,2,1,16,2,2);
            INSERT INTO cart_item VALUES(3,3,1,17,3,3);
            INSERT INTO cart_item VALUES(2,2,1,17,4,3);
            COMMIT;
            '''
        )

    def test_profile(self):
        request = self.__tempdb.profile_info(id=1)
        self.assertEqual(1, len(request))
        request = self.__tempdb.profile_info(id=2)
        self.assertEqual(1, len(request))
        request = self.__tempdb.profile_info(id=3)
        self.assertEqual(1, len(request))


    def test_item(self):
        request = self.__tempdb.item_info(id=1)
        self.assertEqual(1, len(request))
        request = self.__tempdb.item_info(id=2)
        self.assertEqual(1, len(request))
        request = self.__tempdb.item_info(id=3)
        self.assertEqual(1, len(request))

    def test_orders(self):
        request = self.__tempdb.orders_info(id=1)
        self.assertEqual(1, len(request))
        request = self.__tempdb.orders_info(id=2)
        self.assertEqual(1, len(request))
        request = self.__tempdb.orders_info(id=3)
        self.assertEqual(1, len(request))
    
    def tearDown(self):
        self.__tempdb.get_session.close()

if (__name__=='__main__'):
    unittest.main(failfast=False)