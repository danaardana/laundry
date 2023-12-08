import paho.mqtt.client as mqtt
import time
import os
import json
from script_pub import *


broker_address = 'localhost' 
client = mqtt.Client('P2')
port = 1883


def on_message(client, userdata, msg): 
    dataMsg = msg.payload.decode()
    dataMsg = json.loads(dataMsg)
    if dataMsg[0] == 'insert':
        print('')
        print('Notifikasi : Pesanan baru diterima')  
        print('')
        result = insert(dataMsg)
        if result > 0:
            print('Sukses menambahkan ke databse')
            bc_msg = 'Sukses menambahkan ke databse'
        else:
            print('Gagal menambahkan ke database')
            bc_msg = 'Gagal menambahkan ke database'

    elif dataMsg[0] == 'delete':
        id = str(dataMsg[1]).upper()
        result = delete(id)
        print('')
        if result > 0 :
            print('Notifikasi : Penghapusan pelanggan dengan kode ', id, ' berhasil')  
            print('')
            bc_msg = ' Penghapusan pelanggan dengan kode ' + id + ' berhasil'
        else:
            print('Notifikasi : Tidak ditemukan pelanggan dengan kode ', id)  
            print('')
            bc_msg = ' Tidak ditemukan pelanggan dengan kode ' + id

    publish_msg(client, dataMsg[2], bc_msg)
    
  

def publish_msg(client, branch, msg):    
    if branch == 'bojong':
        client.publish('bojong', msg)
    else:
        client.publish('soang', msg)  


def menu():        
    print('=======================================')
    print('|                                     |')
    print('|            Menu Laundry             |')
    print('|_____________________________________|')
    print('|                                     |')
    print('| [1] List pesanan                    |')
    print('| [2] Pengumuman                      |')
    print('| [3] Perbaharui Info Pemesanan       |')
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
                            if data != False:
                                print('|=====================================|')
                                print('|     =  Konfirmasi Penghapusan =     |')
                                print('|=====================================|')
                                print('  Nama                : ',data[0][2])
                                print('  Berat Laundry       : ',data[0][3], 'kg')
                                print('  Total pembayaran    :  Rp.',data[0][4])
                                print('  Tanggal selesai     : ',data[0][5])
                                print('|=====================================|')
                                while True:
                                    menu_del = input("Are you sure want to delete? (y/N) ")
                                    if (menu_del == 'y') or (menu_del =='Y'):
                                        delete(id.upper())
                                        break

                                    elif (menu_del == 'n') or (menu_del =='N'):
                                        print('Cenceled')
                                        break

                                    else:
                                        print('Option not available')

                            else:
                                print('ID tidak ditemukan')

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