nama = ["Serial number maker v1.0", "by", "Yogi Ario"]
for i in nama:
  print(i)

import random
import string

def generate_random_serial(length):
  """
  Fungsi untuk generate serial number acak dengan panjang yang ditentukan.

  Args:
    length: Panjang serial number yang diinginkan.

  Returns:
    String: Serial number acak.
  """
  pool = string.ascii_letters + string.digits
  serial = ''.join(random.choice(pool) for _ in range(length))
  return serial

def generate_custom_serial(serial):
  """
  Fungsi untuk generate serial number custom dengan lompatan kelipatan 6.

  Args:
    serial: Serial number yang dimasukkan oleh user.

  Returns:
    String: Serial number custom dengan lompatan kelipatan 6.
  """
  custom_serial = ''
  for i, char in enumerate(serial):
    if char.isalpha():
      new_char = chr(ord(char) + 6)
      if new_char not in string.ascii_letters:
        new_char = chr(ord(char) - 6)
    else:
      new_char = char
    custom_serial += new_char
  return custom_serial

while True:
  # Menampilkan pilihan menu
  print("Pilih jenis serial number:")
  print("1. Random")
  print("2. Custom")

  choice = input("Masukkan pilihan Anda: ")

  if choice == '1':
    # Generate serial number acak
    length = int(input("Masukkan panjang serial number yang diinginkan: "))
    random_serial = generate_random_serial(length)
    print("Serial number acak:", random_serial)

  elif choice == '2':
    # Generate serial number custom
    serial = input("Masukkan serial number yang ingin diubah: ")
    custom_serial = generate_custom_serial(serial)
    print("Serial number custom:", custom_serial)

  else:
    print("Pilihan tidak valid. Silakan masukkan 1 atau 2.")

  # Menawarkan pilihan untuk melanjutkan atau keluar
  next_choice = input("Tekan 1 untuk lanjut membuat atau tekan sembarang tombol untuk keluar: ")
  if next_choice != '1':
            print("Terima kasih telah menggunakan program ini.")
            print("Dan Terimakasih juga untuk: ")
            print("Yogi Ario")
            break