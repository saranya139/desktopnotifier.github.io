from plyer import notification
import time

def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\saran\\Downloads\\Desktop icon.ico",
        timeout = 10,
    )
if __name__ == '__main__':
    while True:
        notifyMe("Heyy! Beware it's  corona time!ππ", "It's time to wash your handsποΈ"'\n''Did you wore your mask?π·''\n'"Keep social distance")
        time.sleep(60)