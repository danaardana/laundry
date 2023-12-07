
import mysql.connector

def update(id):
    mydb = mysql.connector.connect(
        user="root",
        database="laundry"
    )
    sql = mydb.cursor()
    query = "UPDATE `custumers` SET status = %s WHERE id = %s"
    value = ('1',id)
    sql.execute(query,value)
    result = sql.rowcount
    mydb.commit()
    mydb.close()
    return result


def delete(id):
    mydb = mysql.connector.connect(
        user="root",
        database="laundry"
    )
    sql = mydb.cursor()
    query = "DELETE FROM `custumers` WHERE id = %s "
    value = (id,)
    sql.execute(query,value)
    result = sql.rowcount
    mydb.commit()
    mydb.close()
    return result


def show_one(id):
    mydb = mysql.connector.connect(
        user="root",
        database="laundry"
    )
    sql = mydb.cursor()
    query = "SELECT * FROM custumers WHERE id = %s"
    value = (id, )
    sql.execute(query,value)
    data = sql.fetchall()
    mydb.close()
    result = sql.rowcount
    if result > 0:
        return data
    else:
        return False


def show_all():
    mydb = mysql.connector.connect(
        user="root",
        database="laundry"
    )
    sql = mydb.cursor()
    sql.execute("SELECT * FROM custumers")
    data = sql.fetchall()
    mydb.close()
    return data


def show_list(laundry):
    data = show_all()
    print('                  === Daftar pesanan ===          ') 
    for item in data:
        if laundry == 1:
            if item[1] == 'bojong':
                print(item)
        else:
            if item[1] == 'soang':
                print(item)
    

def insert(data):    
    mydb = mysql.connector.connect(
        user="root",
        database="laundry"
    )
    sql = mydb.cursor()
    query = "INSERT INTO custumers (`id`, `cabang`, `nama`, `berat`, `harga`, `tgl_selesai`) VALUES (%s, %s, %s, %s, %s, %s)"
    value = (data[1],data[2],data[3],(data[4]),data[5],data[6])
    sql.execute(query,value)
    result = sql.rowcount
    mydb.commit()
    mydb.close()
    return result
