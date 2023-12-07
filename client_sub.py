import paho.mqtt.client as mqtt
import os
import time
from datetime import date, timedelta
import string
import random
import json
from inputimeout import inputimeout 
from script_pub import *

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


def calculate_date(berat):                 
    if berat <= 5 :                        
        dt = date.today() + timedelta(2)    
    elif berat <= 10 :                     
        dt = date.today() + timedelta(3)    
    else:                                   
        dt = date.today() + timedelta(5) 
    return dt.strftime("%m/%d/%Y")


def calculate_costBojong(berat):
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
    print('ANNOUNCEMENT : ', str(message.payload.decode('utf-8')))
    print('')
    time.sleep(0.5)


def run():
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
                client_id_prev = ''
                client.subscribe(client_id)
                time.sleep(0.5)
                os.system('cls')

            else:
                print('Option not available')
        
        while True and laundry != '':
            menu_sub = ''
            menu(client_id)
            menu_option = input("Pilihan anda: ")

            if menu_option != '':

                if (menu_option.isnumeric()):
                    menu_option = int(menu_option)

                    match menu_option:
                        case 1:

                            if client_id_prev != '':
                                print('')
                                print('Untuk memesan ulang Kode ID akan diperbaharui')
                                print('')

                                while True:
                                    menu_sub = input('Perbaharui (Y/N) ') 
                                    
                                    if (menu_sub == 'y') or (menu_sub =='Y'):  
                                        client_id_prev = ''                          
                                        client.unsubscribe(client_id)
                                        client_id = randomStr()
                                        client.subscribe(client_id)
                                        os.system('cls')
                                        menu(client_id)
                                        break

                                    elif (menu_sub == 'n') or (menu_sub =='N'):
                                        print('Kode ID tidak diperbaharui')
                                        break

                                    else:
                                        print('Option not available')
                            
                            elif menu_sub == '' or (menu_sub == 'y') or (menu_sub =='Y'):

                                while True:
                                    client_nama = input('Nama : ')
                                    if len(client_nama) < 20:
                                        break

                                    else:
                                        print('Tolong dipersingkat nama anda, terima kasih')
                                
                                while True:
                                    client_berat = input('Berat : ')
                                    if client_berat.isnumeric():
                                        client_berat = int(client_berat)
                                        break

                                    else:
                                        print('Hanya menerima angka')

                                Wkt_selesai = calculate_date(client_berat)
                                Tot_biaya = calculate_costBojong(client_berat)
                                data = ['insert',client_id, branch,  client_nama, client_berat, Tot_biaya, Wkt_selesai]
                                client.publish(topicNew, json.dumps(data))
                                print('Pesanan telah tersimpan')
                                client_id_prev = client_id

                        case 2:

                            while True:
                                menu_sub2 = input('Menggunakan Kode ID yang lain (Y/N) ') 
                                
                                if (menu_sub2 == 'y') or (menu_sub2 =='Y'):  
                                    client_id = input('Masukan Kode ID: ')
                                    break

                                elif (menu_sub2 == 'n') or (menu_sub2 =='N'):
                                    print('Kode ID tidak diperbaharui')
                                    break

                                else:
                                    print('Option not available')
                            
                            data = show_one(client_id)
                            
                            if data != False:
                                print('|=====================================|')
                                print('|      = Struk Laundry ' + branch + ' =       |')
                                print('|=====================================|')
                                print('  Nama                : ',data[0][2])
                                print('  Berat Laundry       : ',data[0][3], 'kg')
                                print('  Total pembayaran    :  Rp.',data[0][4])
                                print('  Tanggal selesai     : ',data[0][5])
                                print('|=====================================|')
                                
                        case 3:

                            while True:
                                menu_sub2 = input('Menggunakan Kode ID yang lain (Y/N) ') 
                                
                                if (menu_sub2 == 'y') or (menu_sub2 =='Y'):  
                                    client_id = input('Masukan Kode ID: ')
                                    break

                                elif (menu_sub2 == 'n') or (menu_sub2 =='N'):
                                    print('Kode ID tidak diperbaharui')
                                    break

                                else:
                                    print('Option not available')

                            print('Pesanan akan dibatalkan ')
                            data = ['delete', client_id, branch]
                            client.publish(topicNew, json.dumps(data))

                        case 0:
                            break
                else:
                    print('Option not available')

            print('')
            input('Press to continue..')
            os.system('cls')

        os.system('cls')

if __name__ == '__main__':
    run()