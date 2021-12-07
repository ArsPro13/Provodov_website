import sqlite3

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()


print('выбор людей с заказами от определенной суммы')
for row in cursor.execute('SELECT (SELECT first_name FROM user WHERE user_id=user_id_ord) AS name,(SELECT last_name FROM user WHERE user_id=user_id_ord) AS surname,(SELECT adress FROM user WHERE user_id=user_id_ord) AS adress,amount FROM orders WHERE amount>=16;'):
    print(*row)

print()

print('выбор даты заказа и суммы заказов, сделанных из определенных городов')
for row in cursor.execute('SELECT (SELECT amount FROM orders WHERE user_id_ord=user_id) AS amount,(SELECT created_at FROM orders WHERE user_id_ord=user_id) AS when_made, adress FROM user WHERE (adress="london" or adress="LA");'):
    print(*row)

print()


print('выбор всех позиций из определенного заказа')
for row in cursor.execute('SELECT(SELECT item_name FROM item WHERE item_id=item_id_cart) AS item_name, ord_id AS id_zakaza FROM cart_item WHERE ord_id=2;'):
    print(*row)

print()


conn.close()
