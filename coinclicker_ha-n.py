


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

class ClickerApp(App):
    def build(self):
        self.coins = 0
        self.click_value = 1
        self.click_upgrade_cost = 10
        self.passive_upgrade_cost = 20
        self.passive_income = 0
        self.passive_upgrade_interval = 1.0
        self.coins_per_second = 0

        # кнопочки надписи
        self.label_coins = Label(text=f"Монетки: {self.coins}")
        self.label_coins_per_second = Label(text=f"Монеток в секунду: {self.coins_per_second}")
        self.button_click = Button(text="НАЖМИ НА МЕНЯ!", on_press=self.click)
        self.button_upgrade_click = Button(text=f"Улучшить силу нажатия ({self.click_upgrade_cost} монеток)", on_press=self.upgrade_click)
        self.button_upgrade_passive = Button(text=f"Купить пассивное улучшение ({self.passive_upgrade_cost} монеток)", on_press=self.buy_passive_upgrade)

        # линии
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(self.label_coins)
        layout.add_widget(self.label_coins_per_second)
        layout.add_widget(self.button_click)
        layout.add_widget(self.button_upgrade_click)
        layout.add_widget(self.button_upgrade_passive)

        
        Clock.schedule_interval(self.update, 1.0)
        Clock.schedule_interval(self.add_passive_income, self.passive_upgrade_interval)

        return layout

    def click(self, instance):
        self.coins += self.click_value
        self.label_coins.text = f"Монетки: {self.coins}"
    #улучшение клика
    def upgrade_click(self, instance):
        if self.coins >= self.click_upgrade_cost:
            self.coins -= self.click_upgrade_cost
            self.click_value *= 2
            self.click_upgrade_cost = int(self.click_upgrade_cost * 1.8)
            self.label_coins.text = f"Монетки: {self.coins}"
            self.button_upgrade_click.text = f"Улучшить силу нажатия ({self.click_upgrade_cost} монеток)"
    #пасивка
    def buy_passive_upgrade(self, instance):
        if self.coins >= self.passive_upgrade_cost:
            self.coins -= self.passive_upgrade_cost
            self.passive_income += 1
            self.passive_upgrade_cost = int(self.passive_upgrade_cost * 1.1)
            self.label_coins.text = f"Монетки: {self.coins}"
            self.button_upgrade_passive.text = f"Купить пассивное улучшение ({self.passive_upgrade_cost} монеток)"
    #монеточки
    def update(self, dt):
        self.coins_per_second = self.passive_income
        self.label_coins_per_second.text = f"Монеток в секунду: {self.coins_per_second}"
        self.coins += self.coins_per_second
        self.label_coins.text = f"Монетки: {self.coins}"
    #увеличение когда куплю пасивку
    def add_passive_income(self, dt):
        self.coins_per_second += self.passive_income

app = ClickerApp()
app.run()