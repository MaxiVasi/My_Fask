import sqlite3
from flask import Flask, request, render_template

data = [
    ('Maxim', 'Kolobov', 'Maxim@example.com', 'NY'),
    ('Vasiliy', 'Kolobov', 'Vasiliy@example.com', 'Paris'),
    ('Galina', 'Grapova', 'Galina@example.com', 'Tokio'),
    ('Svetlana', 'Svetikova', 'SS@example.com', 'Moscow'),
    ('Gena', 'Volkin', 'Gena@example.com', 'Kazan'),
    ('Guzzella', 'Puzella', 'Guz@example.com', 'Tumen'),
    ('Vanko', 'Zayzev', 'Vanko@example.com', 'Milan'),
    ('Galka', 'Zayzev', 'Galka@example.com', 'Madrid'),
    ('Sosulka', 'Zima', 'Sosulka@example.com', 'Berlin'),
    ('Pulka', 'War', 'Pulka@example.com', 'Washington'),
    ('Yulia', 'Zabiaka', 'Yulka@example.com', 'London'),
]

'''Создаем Базу и подключаемся к ней.'''
connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS MyTable (
name TEXT NOT NULL,
surname TEXT NOT NULL,
email TEXT NOT NULL,
city TEXT NOT NULL
)
''')

connection.commit()

'''Наполняем Базу данных из данных data.'''
for i in data:
    cursor.execute('''
    INSERT INTO MyTable (name, surname, email, city) VALUES (?, ?, ?, ?)''', i)

connection.commit()
connection.close()

app = Flask(__name__)

@app.route('/')
def MyTable():
    connection = sqlite3.connect('mydb.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM MyTable')
    my_data_db = cursor.fetchall()
    connection.close()
    return my_data_db

# С использованием index.html
@app.route('/my')
def home():
    connection = sqlite3.connect('mydb.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM MyTable')
    my_data_db = cursor.fetchall()
    connection.close()
    headers = ['name', 'surname', 'email', 'city']
    return render_template('index.html', headers=headers, data=my_data_db)

if __name__ == '__main__':
    app.run()
