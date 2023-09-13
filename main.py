from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class NumberConverter(App):
    def build(self):
        self.title = "Zahlkonverter (Binär, Dezimal, Hexadezimal)"

        root_layout = GridLayout(cols=2, spacing=10, padding=10)

        # Labels und Eingabefelder für die Konvertierung
        root_layout.add_widget(Label(text="Binär:"))
        self.binary_input = TextInput(hint_text="1010")
        self.binary_input.bind(text=self.on_binary_input)
        root_layout.add_widget(self.binary_input)

        root_layout.add_widget(Label(text="Dezimal:"))
        self.decimal_input = TextInput(hint_text="123456789")
        self.decimal_input.bind(text=self.on_decimal_input)
        root_layout.add_widget(self.decimal_input)

        root_layout.add_widget(Label(text="Hexadezimal:"))
        self.hexadecimal_input = TextInput(hint_text="ABCDEF")
        self.hexadecimal_input.bind(text=self.on_hexadecimal_input)
        root_layout.add_widget(self.hexadecimal_input)

        # Ergebnisanzeige
        self.result_label = Label(text="", size_hint=(None, None))
        root_layout.add_widget(self.result_label)

        return root_layout

    def on_binary_input(self, instance, value):
        binary_value = value.strip()
        try:
            decimal_value = int(binary_value, 2)
            hexadecimal_value = hex(decimal_value).upper()[2:]
            self.decimal_input.text = str(decimal_value)
            self.hexadecimal_input.text = hexadecimal_value
            self.result_label.text = f"Dezimal: {decimal_value}\nHexadezimal: {hexadecimal_value}"
        except ValueError:
            self.result_label.text = "Fehler: Ungültige binäre Eingabe."

    def on_decimal_input(self, instance, value):
        decimal_value = value.strip()
        try:
            decimal_value = int(decimal_value)
            binary_value = bin(decimal_value)[2:]
            hexadecimal_value = hex(decimal_value).upper()[2:]
            self.binary_input.text = binary_value
            self.hexadecimal_input.text = hexadecimal_value
            self.result_label.text = f"Binär: {binary_value}\nHexadezimal: {hexadecimal_value}"
        except ValueError:
            self.result_label.text = "Fehler: Ungültige dezimale Eingabe."

    def on_hexadecimal_input(self, instance, value):
        hexadecimal_value = value.strip()
        try:
            decimal_value = int(hexadecimal_value, 16)
            binary_value = bin(decimal_value)[2:]
            self.binary_input.text = binary_value
            self.decimal_input.text = str(decimal_value)
            self.result_label.text = f"Binär: {binary_value}\nDezimal: {decimal_value}"
        except ValueError:
            self.result_label.text = "Fehler: Ungültige hexadezimale Eingabe."

if __name__ == "__main__":
    NumberConverter().run()
