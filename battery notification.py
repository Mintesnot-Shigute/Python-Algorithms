import psutil
from plyer import notification
import time

def get_battery_status():
    battery = psutil.sensors_battery()
    percent = battery.percent
    power_plugged = battery.power_plugged

    return percent, power_plugged

def show_notification(message):
    notification.notify(
        title='Battery Notification',
        message=message,
        app_name='Battery Monitor',
    )

def battery_notification():
    threshold = 20  # Set your desired threshold here

    while True:
        percent, power_plugged = get_battery_status()

        if percent <= threshold and not power_plugged:
            message = f'Battery level is {percent}%. Connect charger!'
            show_notification(message)

        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    battery_notification()
