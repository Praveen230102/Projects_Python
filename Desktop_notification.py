# import math
# import random
from plyer import notification

def water_notification():
    notification.notify(
        title = "Please drink water",
        message = "Water is very important for proper functioning of organs, So drink water every hour .....",
        timeout = 5
        )

water_notification()
