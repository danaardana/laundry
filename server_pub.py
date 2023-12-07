#Import Library
import paho.mqtt.client as mqtt
import time
import os
import json
import mysql.connector
from mysql.connector import errorcode

port = 1883
broker_address = 'localhost' 
client = mqtt.Client('P2')


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
    return data


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
    value = (data[0],data[1],data[2],(data[3]),data[4],data[5])
    sql.execute(query,value)
    result = sql.rowcount
    mydb.commit()
    mydb.close()
    return result

def on_message(client, userdata, msg): 
    dataMsg = msg.payload.decode()
    dataMsg = json.loads(dataMsg)
    if len(dataMsg) > 2:
        result = insert(dataMsg)
    if result > 0:
        print('')
        print('Notifikasi : Pesanan baru diterima')  
        print('')

def menu():        
    print('=======================================')
    print('|                                     |')
    print('|            Menu Laundry             |')
    print('|_____________________________________|')
    print('|                                     |')
    print('| [1] List pesanan                    |')
    print('| [2] Pengumuman                      |')
    print('| [3] Info Pemesanan                  |')
    print('| [4] Hapus pesanan                   |')
    print('|                                     |')
    print('| [0] Kembali                         |')
    print('=======================================')


def branch_menu():
    print('|=====================================|')
    print('|             Pilih Cabang            |')
    print('|=====================================|')
    print('| [1] Laundry Bojong                  |')
    print('| [2] Laundry Soang                   |')
    print('|                                     |')
    print('| [0] Keluar                          |')
    print('|=====================================|')



def run():
    client.on_message=on_message 
    client.connect(broker_address, port) 
    print('server has started')
    while True :
        branch_menu()
        laundry = input("Pilih Cabang Laundry: ")
        if laundry != '':
            if (laundry.isnumeric()):
                laundry = int(laundry)
                client.loop_start()

                if laundry == 1:
                    print('Laundry Bojong selected')
                    client.subscribe('laundry-bojong')

                elif laundry == 2:
                    print('Laundry Soang selected')
                    client.subscribe('laundry-soang')

                else : 
                    quit()

            else:
                print('Option not available')

            time.sleep(0.5)

       
        while True and laundry != '':
            menu()
            menu_option = input("Fitur yang dipilih: ")
            if menu_option != '':
                if (menu_option.isnumeric()):
                    menu_option = int(menu_option)
                    match menu_option:
                        case 1:
                            data = show_all()
                            print('                  === Daftar pesanan ===          ') 
                            for item in data:
                                if laundry == 1:
                                    if item[1] == 'bojong':
                                        print(item)
                                else:
                                    if item[1] == 'soang':
                                        print(item)


                        case 2:
                            bc_msg = input('Masukan pesan : ')
                            if laundry == 1:
                                client.publish('bojong', bc_msg)
                            else:
                                client.publish('soang', bc_msg)


                        case 3:
                            show_list(laundry)
                            id = input('Masukan ID : ')
                            update(id.upper())
                            client.publish(id.upper(), 'Pesanan anda sudah selesai')
                            print('Sudah diperbaharui')


                        case 4:                    
                            id = input('Masukan ID: ')
                            data = show_one(id.upper())
                            print('|=====================================|')
                            print('|     =  Konfirmasi Penghapusan =     |')
                            print('|=====================================|')
                            print('  Nama                : ',data[0][2])
                            print('  Berat Laundry       : ',data[0][3], 'kg')
                            print('  Total pembayaran    :  Rp.',data[0][4])
                            print('  Tanggal selesai     : ',data[0][5])
                            print('|=====================================|')
                            menu_del = input("Are you sure want to delete? (y/N) ")
                            if (menu_del == 'y') or (menu_del =='Y'):
                                delete(id.upper())
                            elif (menu_del == 'y') or (menu_del =='Y'):
                                print('Cenceled')
                            else:
                                print('Option not available')

                        case 0:
                            break

                else:
                    print('Option not available')
                
                print('')
                print('')
                input('Press any key to continue...')
                os.system('cls')
        os.system('cls')
if __name__ == '__main__':
    run()