# Импортируем необходимые модули из Kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Определяем класс главного экрана нашего приложения
class MyButtonApp(App):
    def build(self):
        # Создаем вертикальный макет для размещения виджетов
        layout = BoxLayout(orientation='vertical')

        # Создаем кнопку с текстом
        button = Button(text='Привет, мир!',
                        on_press=self.on_button_click) # Привязываем функцию к событию нажатия

        # Добавляем кнопку в макет
        layout.add_widget(button)

        return layout

    # Функция, которая будет вызвана при нажатии кнопки
    def on_button_click(self, instance):
        print("Кнопка нажата!")
        instance.text = 'Нажато!' # Изменяем текст кнопки

# Запускаем приложение
if __name__ == '__main__':
    MyButtonApp().run()
