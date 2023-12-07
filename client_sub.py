# Library
import paho.mqtt.client as mqtt
import os
import time
import json
from datetime import date, timedelta
import string
import random

# setup 
broker_address='localhost'
client = mqtt.Client('P1')
port=1883

def menu(client_id):    
    print('|=====================================|')
    print('|                  MENU               |')
    print('|               id : '+client_id+'          |')
    print('|=====================================|')
    print('| [1] Pesan                           |')
    print('| [2] Cek Status                      |')
    print('| [3] Batalkan                        |')
    print('|                                     |')
    print('| [0] Keluar                          |')
    print('|=====================================|')


def branch_menu():
    print('|=====================================|')
    print('|            Pilih Cabang             |')
    print('|=====================================|')
    print('| [1] Laundry Bojong                  |')
    print('| [2] Laundry Soang                   |')
    print('|                                     |')
    print('| [0] Keluar                          |')
    print('|=====================================|')


# manual func
def calculate_date(berat):                 #menghitung tanggal pada saat pembuatan pesanan
    if berat <= 5 :                        #apabila kondisi pesanan beratnya dibawah 10
        dt = date.today() + timedelta(2)    #maka akan menambah 2 hari
    elif berat <= 10 :                     #apabila kondisi pesanan beratnya dibawah 20
        dt = date.today() + timedelta(3)    #maka akan menambah 3 hari
    else:                                   #apabila kondisi pesanan beratnya diatas 20
        dt = date.today() + timedelta(5) #  maka akan menambah 5 hari
    return dt.strftime("%m/%d/%Y")


def calculate_costBojong(berat): #menghitung berat dan harga
    if berat <= 5 :
        biaya = berat *7000
    elif berat <= 10 :
        biaya = berat *6000
    elif berat <= 15 :
        biaya = berat *5000
    else:
        biaya = berat *4000
    return biaya


def calculate_costSoang(berat):
    if berat <= 5 :
        biaya = berat *7000
    elif berat <= 10 :
        biaya = berat *6000
    elif berat <= 15 :
        biaya = berat *5000
    else:
        biaya = berat *4000
    return biaya


def randomStr():
    N = 7
    randmid = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
    return randmid


def on_message(client, userdata, message):
    print('')
    print('notifikasi : ', str(message.payload.decode('utf-8')))
    print("Pilihan anda: ")


def preview(data, branch):    
    print('|=====================================|')
    print('|      = Struk Laundry ' + branch + ' =       |')
    print('|=====================================|')
    print('  Nama                : ',data[0][2])
    print('  Berat Laundry       : ',data[0][3], 'kg')
    print('  Total pembayaran    :  Rp.',data[0][4])
    print('  Tanggal selesai     : ',data[0][5])
    print('|=====================================|')


client.on_message=on_message
client.connect(broker_address, port)

while True:
    branch_menu()
    laundry = input("Pilih Laundry: ")

    if laundry != '':
        if (laundry.isnumeric()):
            laundry = int(laundry)
            client.loop_start()
            if laundry ==  1:
                    client.subscribe('bojong')
                    branch = 'bojong'                    
                    topicNew = 'laundry-bojong'
                    print('Anda telah memilih Laundry Bojong')

            elif laundry == 2:                    
                    client.subscribe('soang')
                    branch = 'soang'          
                    topicNew = 'laundry-soang'
                    print('Anda telah memilih Laundry Soang')

            elif laundry == 0:
                    break
                    
            client_id = randomStr()
            client.subscribe(client_id)
            time.sleep(0.5)
            os.system('cls')

        else:
            print('Option not available')
    
    while True and laundry != '':
        menu(client_id)
        menu_option = input("Pilihan anda: ")
        if menu_option != '':
            if (menu_option.isnumeric()):
                menu_option = int(menu_option)
                match menu_option:
                    case 1:
                        while True:
                            nama = input('Nama : ')
                            if len(nama) < 20:
                                break
                            else:
                                print('Tolong dipersingkat nama anda, terima kasih')

                        berat = int(input('Berat : '))
                        Wkt_selesai = calculate_date(berat)
                        Tot_biaya = calculate_costBojong(berat)
                        
                        # proses ke database
                        data = [client_id, branch,  nama, berat, Tot_biaya, Wkt_selesai]
                        client.publish(topicNew, json.dumps(data))
                        print('Pesanan telah tersimpan')

                    case 2:
                        #reload(database)
                        nama = str(input('Masukan nama anda : '))
                        preview(data, branch)
                            
                    case 3:
                        nama = input('Masukan nama anda : ')

                    case 0:
                        break
            else:
                print('Option not available')

        os.system('cls')

    os.system('cls')