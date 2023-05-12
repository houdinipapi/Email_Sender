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

        else:
            notification.notify(
                title="Plugged In",
                message="Please remove the charger. For better battery life, charge up-to 80%.",
                timeout=5
            )

    # Not Plugged in
    else:
        percent = battery.percent

        if percent <= 20:
            notification.notify(
                title="Battery Reminder",
                message="Your battery is running low. Plug in the charger.",
                timeout=5
            )

        elif percent <= 50:
            notification.notify(
                title="Battery Reminder",
                message=f"Battery is {percent}%.",
                timeout=5
            )

        elif percent == 100:
            notification.notify(
                title="Battery Reminder",
                message="Fully Charged.",
                timeout=5
            )

        else:
            notification.notify(
                title="Battery Reminder",
                message=f"Battery is {percent}%.",
                timeout=5
            )
