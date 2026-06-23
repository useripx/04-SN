import os
import sys
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()
    except Exception as e:
        print(f"Kesalahan: {e}")
        sys.exit()

nama = ["Serial number maker v1.0", "Terimakasih untuk:", "Yogi Ario"]
for i in nama:
  print(i)

print("\n")
print("Aplikasi ini berisi 2 kegunaan yakni SN maker diamana bisa membuat serial number secara otomatis,")
print("kedua aplikasi encrypt kata sederhana yang akan merubah kata dan angka yang anda masukkan menjadi sebuah kode yang unik.")
print("\n")

import random
import string

def generate_random_serial(length=7):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def custom_serial_with_jump(user_input):
    def shift_char(char, jump):
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - start + jump) % 26 + start)
        elif char.isdigit():
            return chr((ord(char) - ord('0') + jump) % 10 + ord('0'))
        else:
            return char

    jump = 6
    return ''.join(shift_char(c, jump) for c in user_input)

def main():
    while True:
        print("Pilih salah satu:")
        print("1. Generate Serial")
        print("2. Encrypt Kata")
        choice = input("Masukkan pilihan Anda (1/2): ")

        if choice == '1':
            length = int(input("Masukkan panjang serial number yang diinginkan: "))
            serial = generate_random_serial(length)
            print("Serial number acak:", serial)
        elif choice == '2':
            user_input = input("Masukkan kata, kalimat, dan atau angka Anda: ")
            serial = custom_serial_with_jump(user_input)
            print(f"Serial number Random: {serial}")
        else:
            print("Pilihan tidak valid.")

        next_action = input("Tekan 1 untuk membuat lagi atau tekan sembarang tombol untuk keluar: ")
        if next_action != '1':
            print("Terima kasih telah menggunakan Serial Number maker")
            print("Dan Terimakasih juga untuk: ")
            print("Yogi Ario")
            break

if __name__ == "__main__":
    main()
