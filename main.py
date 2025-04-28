from kivy.core.window import Window
Window.icon = "plus.png"
Window.title = "ADD IT"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class AdditionApp(App):
    def build(self):
        # Create the main layout (vertical stacking)
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        # Title Label
        title_label = Label(
            text="Addition App",
            font_size=28,
            size_hint=(1, 0.15)
        )
        main_layout.add_widget(title_label)

        # Input Layout (horizontal stacking for input fields)
        input_layout = BoxLayout(orientation="horizontal", spacing=10)

        self.num1 = TextInput(
            hint_text="Enter first number",
            font_size=18,
            input_filter="float",
            size_hint=(0.5, 0.1),
            multiline=False
        )
        self.num2 = TextInput(
            hint_text="Enter second number",
            font_size=18,
            input_filter="float",
            size_hint=(0.5, 0.1),
            multiline=False
        )
        input_layout.add_widget(self.num1)
        input_layout.add_widget(self.num2)

        main_layout.add_widget(input_layout)  # Add input layout to main layout

        # Add Button
        self.add_button = Button(
            text="Add Numbers",
            font_size=20,
            size_hint=(1, 0.15)
        )
        self.add_button.bind(on_press=self.calculate_sum)
        main_layout.add_widget(self.add_button)

        # Result Label
        self.result_label = Label(
            text="Result: ",
            font_size=24,
            size_hint=(1, 0.15)
        )
        main_layout.add_widget(self.result_label)

        return main_layout  # Return the structured layout

    def calculate_sum(self, instance):
        try:
            num1 = float(self.num1.text)
            num2 = float(self.num2.text)
            result = num1 + num2
            self.result_label.text = f"Result: {result}"
        except ValueError:
            self.result_label.text = "Invalid input! Enter numbers only."


# Run the app
if __name__ == "__main__":
    AdditionApp().run()

