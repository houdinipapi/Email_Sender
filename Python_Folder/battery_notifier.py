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
                title="Plugged In",

                # Notification Message
                message="For better battery life, charge up-to 80%",

                # Displaying Time
                timeout=5
            )

        elif percent == 100:
            notification.notify(
                title="Plugged In",
                message="Battery is fully charged. Please plug out the charger.",
                timeout=5
            )
