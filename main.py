import pyautogui as pg
import time


class WhatsApp():
    def __init__(self,num,text):
        self.num = num
        self.text = text

    def send_message(self):
        """Отправка заготовленных смс сообщений"""
        time.sleep(5)
        for s in range(0,int(self.num)):
            pg.write(self.text)
            pg.press('Enter')
    print('Успешно!')

if __name__ == '__main__':
    WA = WhatsApp(10,'=)')
    WA.send_message()