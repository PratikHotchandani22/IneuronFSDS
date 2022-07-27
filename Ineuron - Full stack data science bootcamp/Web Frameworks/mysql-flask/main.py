# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, request, jsonify
import mysql.connector as connection
import pymongo

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home_page():
    # try:
    #     global mydb
    #     mydb = connection.connect(host="localhost", user="root", passwd="mysql123", use_pure=True)
    #     # check if the connection is established
    #
    #     query = "CREATE DATABASE IF NOT EXISTS WebFrameworkTask;"
    #
    #     global cursor2
    #     cursor2 = mydb.cursor()  # create a cursor to execute queries
    #     cursor2.execute(query)
    #
    #     cursor2.execute("SHOW DATABASES")
    #
    #     print(cursor2.fetchall())
    #
    # except Exception as e:
    #     # mydb.close()
    #     print(str(e))
    client = pymongo.MongoClient("mongodb+srv://test:test@cluster0.bfl7m.mongodb.net/?retryWrites=true&w=majority")
    db = client["flaskDB"]
    collection = db["flaskCollection"]
    record = {'compnayName': 'pratik',
              'product': 'smart phones',
              'Services offered': 'teaching iOS'}
    collection.insert_one(record)
    print(collection)
    return render_template('homepage.html')

@app.route('/performSQLTask', methods=['POST'])
def sqlTasks():
    tableName = request.form['tableName']
    columnName = request.form['columnName']

    query = "CREATE TABLE IF NOT EXISTS WebFrameworkTask.%s (%s VARCHAR(20))" %(tableName,columnName)
    # cursor2.execute(query)
    return (jsonify("hwllo"))











# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
