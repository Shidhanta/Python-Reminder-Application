import time 
from plyer import notification 

def notification_declaration(t, m):
    while(True):    
        notification.notify(
        title=t,
        message = m,
        #app_icon = "D:\\Classwork\\Second Semester\\Programs\\Python\\Notification System\\laptop_fire.jpg"
        timeout = 15
        )
        time.sleep(60*60)
