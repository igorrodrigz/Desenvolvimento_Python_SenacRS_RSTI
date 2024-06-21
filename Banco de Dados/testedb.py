import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senacrs",
    database="mydb"
)

mycursor = mydb.cursor()
mycursor.execute("INSERT INTO Produto (nome, descricao,valor) VALUES ('Piercing de Titânio', 'Piercing argola circular', '89.90')")
mydb.commit()
