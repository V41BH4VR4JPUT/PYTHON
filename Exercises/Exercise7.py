# Drink Water Notification

import time
from plyer import notification 

def remind_water():
    notification.notify(
        title="Drink Water",
        message="Please drink water now.",
        timeout=10
    )
    time.sleep(60*60)

if __name__ == "__main__":
    remind_water()