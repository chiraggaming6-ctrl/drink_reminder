import time
from plyer import notification



while True:
     print("drink some water!")
     notification.notify(title ="please drink water",
                         message = "you need o drink some water.",
                         timeout = 5
                         )
     
     time.sleep(60*60)
     

