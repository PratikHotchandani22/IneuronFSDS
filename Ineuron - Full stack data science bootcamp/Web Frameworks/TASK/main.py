# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string

from flask import Flask, render_template, request, jsonify
import mysql.connector as connection

app = Flask(__name__)
databaseSelected = ""
taskSelected = ""

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('homepage.html')


@app.route('/performCRUD_on_DatabaseSelected', methods=['POST'])  # This will be called from UI
def crud_page():
    if (request.method == 'POST'):
        global databaseSelected
        databaseSelected = request.form['operation']
        global taskSelected
        taskSelected = request.form['Task']
        databaseTaskDetails = "The database selected is : %s and task selected is %s" % (databaseSelected, taskSelected)
        database_tasks()
        return render_template('dataEntry.html', result=databaseTaskDetails)


def create_sql_table():
    return render_template('createTable.html')


def insert_oneData_sql():
    pass


def update_sql_table():
    pass


def bulkInsert_sql_table():
    pass


def deleteFrom_sql_table():
    pass


def downloadData_sql_table():
    pass


def perform_mySql_tasks():
    try:
        mydb = connection.connect(host="localhost", user="root", passwd="mysql123", use_pure=True)
        # check if the connection is established

        query = "CREATE DATABASE IF NOT EXISTS WebFrameworkTask;"

        cursor2 = mydb.cursor()  # create a cursor to execute queries
        cursor2.execute(query)

        cursor2.execute("SHOW DATABASES")

        print(cursor2.fetchall())

    except Exception as e:
        # mydb.close()
        print(str(e))

    if(taskSelected == 'createTable'):
        create_sql_table()
    elif(taskSelected == 'insertOneData'):
        insert_oneData_sql()
    elif(taskSelected == 'updateTable'):
        update_sql_table()
    elif (taskSelected == 'bulkInsert'):
        bulkInsert_sql_table()
    elif(taskSelected == 'deleteFromTable'):
        deleteFrom_sql_table()
    else:
        downloadData_sql_table()


def create_MongoDB_table():
    pass


def insert_MongoDB_sql():
    pass


def update_MongoDB_table():
    pass


def bulkInsert_MongoDB_table():
    pass


def deleteFrom_MongoDB_table():
    pass


def downloadData_MongoDB_table():
    pass


def perform_MongoDB_tasks():
    if (taskSelected == 'createTable'):
        create_MongoDB_table()
    elif (taskSelected == 'insertOneData'):
        insert_MongoDB_sql()
    elif (taskSelected == 'updateTable'):
        update_MongoDB_table()
    elif (taskSelected == 'bulkInsert'):
        bulkInsert_MongoDB_table()
    elif (taskSelected == 'deleteFromTable'):
        deleteFrom_MongoDB_table()
    else:
        downloadData_MongoDB_table()


def create_Cassandra_table():
    pass


def insert_Cassandra_sql():
    pass


def update_Cassandra_table():
    pass


def bulkInsert_Cassandra_table():
    pass


def deleteFrom_Cassandra_table():
    pass


def downloadData_Cassandra_table():
    pass


def perform_Cassandra_tasks():
    if (taskSelected == 'createTable'):
        create_Cassandra_table()
    elif (taskSelected == 'insertOneData'):
        insert_Cassandra_sql()
    elif (taskSelected == 'updateTable'):
        update_Cassandra_table()
    elif (taskSelected == 'bulkInsert'):
        bulkInsert_Cassandra_table()
    elif (taskSelected == 'deleteFromTable'):
        deleteFrom_Cassandra_table()
    else:
        downloadData_Cassandra_table()


@app.route('/performDatabaseTask', methods=['POST'])
def database_tasks():
    if (request.method == 'POST'):
        if (databaseSelected == 'mySql'):
            perform_mySql_tasks()
        elif (databaseSelected == 'MongoDB'):
            perform_MongoDB_tasks()
        else:
            perform_Cassandra_tasks()
        return render_template('dataEntry.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
