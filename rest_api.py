from flask import Flask, request, jsonify
# from db_config import mycursor, mydb
from db_config import Database
db = Database()

app = Flask(__name__)

@app.route("/get", methods=['GET'])
def get():

    sql = "select * from users"
    db.mycursor.execute(sql)
    result = db.mycursor.fetchall()
    data = []

    for r in result:
        id = r[0]
        firstname = r[1]
        lastname = r[2]
        data.append({'id':id, 'firstname':firstname, 'lastname':lastname})
    
    return jsonify(data)

@app.route("/post", methods=['POST'])
def post():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    sql = "insert into users (firstname, lastname) values (%s, %s)"
    val = (firstname, lastname)
    db.mycursor.execute(sql, val)
    db.mydb.commit()
    res = {
        "message": str(db.mycursor.rowcount) + " record(s) added"
    }
    print(db.mycursor.rowcount)
    return res

@app.route("/new-table", methods=['POST'])
def new_table():
    data = request.get_json()
    table_name = data['table_name']
    table_fields = data['table_fields']

    sql = 'create table ' + table_name + ' (id INT AUTO_INCREMENT PRIMARY KEY, '
    for field in table_fields:
        sql = sql + field
    sql = sql + ')'

    # val = (table_name)
    try:
        db.mycursor.execute(sql)
        message = "Table created successfully"
    except:
        message = "Table is already created"
    finally:
        db.mycursor.execute('show tables')
        tables = []
        for r in db.mycursor:
            tables.append(r[0])
            print(r)
        
    
    return jsonify({
        "message":message,
        "tables": tables
    })
    

@app.route("/delete", methods=["DELETE"])
def delete():
    data = request.get_json()
    # firstname=data['firstname']
    # lastname=data['lastname']
    id = data['id']
    sql = "delete from users where id = %s"
    val = ( id, )
    db.mycursor.execute(sql, val)
    db.mydb.commit()

    data = {
        "message": str(db.mycursor.rowcount) + " record(s) deleted"
    }
    return data

@app.route("/update", methods=['PUT'])
def update():
    data = request.get_json()
    firstname = data['firstname']
    lastname = data['lastname']
    id = data['id']
    sql = "UPDATE users SET firstname = %s, lastname = %s WHERE id = %s "
    val = (firstname, lastname, id)
    db.mycursor.execute(sql, val)
    db.mydb.commit()

    data = {
        "message": str(db.mycursor.rowcount) + " record(s) updated"
    }
    return data

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6002, debug=True)
