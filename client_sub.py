# Library
import paho.mqtt.client as mqtt
import os
from datetime import date, timedelta
import string
import random

# temp store
data = []
success = False 

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

# payload
def on_message(client, userdata, message):
    print('')
    print('notifikasi : ', str(message.payload.decode('utf-8')))
    print("Pilihan anda: ")

# setup 
broker_address='localhost'
client = mqtt.Client('P1')
client.on_message=on_message
client.connect(broker_address, port=1883)

while True:
    # main-page
    print('|=====================================|')
    print('|            Pilih Cabang             |')
    print('|=====================================|')
    print('| [1] Laundry Bojong                  |')
    print('| [2] Laundry Soang                   |')
    print('|                                     |')
    print('| [0] Keluar                          |')
    print('|=====================================|')
    opsi = int(input("Pilih Laundry: "))

    if opsi == 1:
        # Bojong handler
        client.loop_start()
        client.subscribe('bojong')
        client_id = randomStr()
        client.subscribe(client_id)
        print('Anda telah memilih Laundry Bojong')
        input('Press any key to continue...')
        os.system('cls')
        while True:
            print('|=====================================|')
            print('|                  Menu               |')
            print('|               id : '+client_id+'          |')
            print('|=====================================|')
            print('| [1] Pesan                           |')
            print('| [2] Cek Status                      |')
            print('| [3] Batalkan                        |')
            print('|                                     |')
            print('| [0] Keluar                          |')
            print('|=====================================|')
            menu = int(input("Pilihan anda: "))
            if menu == 1:
                # input data
                laundry = 'bojong'
                nama = str(input('Nama : '))
                berat = int(input('Berat : '))
                Wkt_selesai = calculate_date(berat)
                Tot_biaya = calculate_costBojong(berat)
                
                # proses ke database
                list = [laundry, client_id, nama, berat, Tot_biaya, Wkt_selesai]
                data.append(list)
                f = open('database.py', 'w')
                bundle = 'data = '+str(data)
                f.write(bundle)
                f.close()
                print('Pesanan telah tersimpan')
                client.publish('laundry-bojong', 'Anda memiliki pesanan baru')

            elif menu == 2:
                #reload(database)
                nama = str(input('Masukan nama anda : '))
                for sub in data:
                    if sub[2] == nama and sub[0] == 'bojong':
                        success = True
                        print('|=====================================|')
                        print('|      = Struk Laundry Bojong =       |')
                        print('|=====================================|')
                        print('  Nama                : ',sub[2])
                        print('  Berat Laundry       : ',sub[3], 'kg')
                        print('  Total pembayaran    :  Rp.',sub[4])
                        print('  Tanggal selesai     : ',sub[5])
                        print('|=====================================|')
                if success == False:
                    print('Tidak ada pesanan')
                    success = False
                    
            elif menu == 3:
                nama = str(input('Masukan nama anda : '))
                new_arr = []
                for sub in data:
                    if sub[2] == nama:
                        pass
                    else:
                        new_arr.append(sub)
                    bundle = 'data = '+str(new_arr)
                f = open('database.py', 'w')
                f.write(bundle)
                f.close()
            elif menu == 0:
                break
            else:
                print('Inputan salah')

            input('Press any key to continue...')
            os.system('cls')

    elif opsi == 2:
        client.loop_start()
        client.subscribe('soang')
        client_id = randomStr()
        client.subscribe(client_id)
        print('Anda telah memilih Laundry Soang')
        input('Press any key to continue...')
        os.system('cls')
        while True:
            print('|=====================================|')
            print('|                  Menu               |')
            print('|               id : '+client_id+'          |')
            print('|=====================================|')
            print('| [1] Pesan                           |')
            print('| [2] Cek Status                      |')
            print('| [3] Batalkan                        |')
            print('|                                     |')
            print('| [0] Keluar                          |')
            print('|=====================================|')
            menu = int(input("Pilihan anda: "))
            if menu == 1:
                # prepare data
                laundry = 'soang'
                nama = str(input('Nama : '))
                berat = int(input('Berat : '))
                Wkt_selesai = calculate_date(berat)
                Tot_biaya = calculate_costBojong(berat)
                
                # proses ke database
                list = [laundry, client_id, nama, berat, Tot_biaya, Wkt_selesai]
                data.append(list)
                f = open('database.py', 'w')
                bundle = 'data = '+str(data)
                f.write(bundle)
                f.close()
                print('Pesanan telah tersimpan')
                client.publish('laundry-soang', 'Anda memiliki pesanan baru')
            elif menu == 2:
                #reload(database)
                nama = str(input('Masukan nama anda : '))
                for sub in data:
                    if sub[2] == nama and sub[0] == 'soang':
                        success = True
                        print('|=====================================|')
                        print('|      = Struk Laundry Soang =        |')
                        print('|=====================================|')
                        print('  Nama                : ',sub[2])
                        print('  Berat Laundry       : ',sub[3], 'kg')
                        print('  Total pembayaran    :  Rp.',sub[4])
                        print('  Tanggal selesai     : ',sub[5])
                        print('|=====================================|')
                if success == False:
                    print('Tidak ada pesanan')
                    success = False
            elif menu == 3:
                nama = str(input('Masukan nama anda : '))
                new_arr = []
                for sub in data:
                    if sub[2] == nama:
                        pass
                    else:
                        new_arr.append(sub)
                    bundle = 'data = '+str(new_arr)
                f = open('database.py', 'w')
                f.write(bundle)
                f.close()
            elif menu == 0:
                break
            else:
                print('Inputan salah')

            input('Press any key to continue...')
            os.system('cls')


    elif opsi == 0:
        break
    else:
        print('Inputan salah')
    
    input('Press any key to continue...')
    os.system('cls')