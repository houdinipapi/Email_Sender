# Importing modules
from plyer import notification
import psutil

# Returns a tuple
battery = psutil.sensors_battery()
plugged = battery.power_plugged

# Code Description
if __name__ == "__main__":
    if plugged:
        percent = battery.percent

        if percent <= 80:
            notification.notify(
                # Notification Title
            )
