import mysql.connector as connection

# pip install mysql-connector-python

# connect to the DB
connect = connection.connect(host='localhost', user='root', password='boost@123', )

# CHECK IF THE CONNECTION IS SUCCESSFUL
print(connect.is_connected())

cursor = connect.cursor()
# cursor.execute('create database  ineuron;')

# cursor.execute('show databases;')
# for i in cursor.fetchall():
#    print(i[0])

cursor.execute('use ineuron;')

# create table
# --------------------------------------
# query = '''CREATE TABLE genre (
#   movie_id varchar(10) NOT NULL,
#   genre varchar(20) NOT NULL,
#   PRIMARY KEY (movie_id,genre)) '''
# cursor.execute(query)
# print(cursor.fetchall())


# insert data
# --------------------------------------
# query = '''INSERT INTO genre (movie_id,genre) VALUES ('12346','Romantic');'''
# cursor.execute(query)
# connect.commit()

# Select data
# --------------------------------------
# query = '''Select genre from genre'''
# cursor.execute(query)
# print(cursor.fetchall())

# Create Table
# --------------------------------------
# query = '''create table if  not exists bank_details(
# age int,
# job varchar(20),
# marital varchar(20),
# education varchar(20),
# `default` varchar(20),
# balance int,
# housing varchar(20),
# loan varchar(20),
# contact varchar(20),
# `day`	int,
# `month` varchar(20),
# duration int,
# campaign int,
# pdays int,
# previous int,
# poutcome varchar(20),
# y varchar(20))'''
#
# try:
#     cursor.execute(query)
#     cursor.fetchall()
# except Exception as e:
#     print('Table already exists')
#
#
# Show table
# --------------------------------------
# cursor.execute('show tables')
# print(cursor.fetchall())
#
# Describe data
# --------------------------------------
# cursor.execute('describe bank_details')
# print(cursor.fetchall())

# drop table
# --------------------------------------
# cursor.execute('drop table  bank_details')
# print(cursor.fetchall())

# Insert multiple data using file operations
# --------------------------------------
# with open('../Dataset/bank.csv') as f:
#     try:
#         f.readline()
#         for i in f.readlines():
#             query = [j.replace('"', '').replace('\n', '') for j in i.split(";")]
#             query = f'insert into bank_details values {tuple(query)}'
#             # print(query)
#             cursor.execute(query)
#         connect.commit()
#         print('Data inserted successfully')
#     except Exception as e:
#         print(f'Some exception has happened {e}')


# display a few columns
# --------------------------------------
# query = 'Select age, loan from bank_details'
# cursor.execute(query)
# print(cursor.fetchall())

# display a few columns with keywords
# --------------------------------------
# query = 'Select age, `default` from bank_details'
# cursor.execute(query)
# print(cursor.fetchall())


# display a few columns with where clause
# --------------------------------------
query = 'Select age, `default` from bank_details where age=41'
query = 'Select distinct job from bank_details where age=41'
query = 'Select distinct * from bank_details where job="retired" and balance<100'
query = 'Select distinct * from bank_details where education="primary" or balance<100'

query = 'Select distinct job from bank_details '
query = 'Select distinct balance from bank_details order by balance '
cursor.execute(query)
for i in cursor.fetchall():
    print(i)


