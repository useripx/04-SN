from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
import random
import string

# Menampilkan nama aplikasi dan terima kasih di console saat aplikasi dimulai
print("Serial number maker v1.0")
print("Terimakasih untuk:")
print("Yogi Ario")
print("\n")

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

class SerialNumberApp(App):
    def build(self):
        self.title = 'Serial Number Generator'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text='Pilih salah satu:')
        layout.add_widget(self.label)

        self.length_input = TextInput(hint_text='Masukkan panjang serial number', multiline=False)
        layout.add_widget(self.length_input)

        self.custom_input = TextInput(hint_text='Masukkan serial number custom', multiline=False)
        layout.add_widget(self.custom_input)

        self.random_button = Button(text='Random Serial')
        self.random_button.bind(on_press=self.generate_random)
        layout.add_widget(self.random_button)

        self.custom_button = Button(text='Random')
        self.custom_button.bind(on_press=self.generate_custom)
        layout.add_widget(self.custom_button)

        self.output_label = Label(text='')
        layout.add_widget(self.output_label)

        self.next_action_button = Button(text='Tekan 1 untuk membuat lagi atau tekan sembarang tombol untuk keluar')
        self.next_action_button.bind(on_press=self.next_action)
        layout.add_widget(self.next_action_button)

        return layout

    def generate_random(self, instance):
        try:
            length = int(self.length_input.text)
            serial = generate_random_serial(length)
            self.output_label.text = f"Serial number acak: {serial}"
        except ValueError:
            self.show_popup('Error', 'Masukkan panjang serial number yang valid.')

    def generate_custom(self, instance):
        user_input = self.custom_input.text
        if user_input:
            serial = custom_serial_with_jump(user_input)
            self.output_label.text = f"Serial number Random: {serial}"
        else:
            self.show_popup('Error', 'Masukkan serial number custom.')

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        popup_label = Label(text=message)
        close_button = Button(text='Close')
        popup_layout.add_widget(popup_label)
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.8, 0.5))
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    def next_action(self, instance):
        next_action = self.custom_input.text
        if next_action != '1':
            print("Terima kasih telah menggunakan Serial Number maker")
            print("Dan Terimakasih juga untuk: ")
            print("Yogi Ario")
            App.get_running_app().stop()

if __name__ == '__main__':
    SerialNumberApp().run()
