import time
from win10toast import ToastNotifier
import datetime

toast = ToastNotifier()

date_format = "%d-%m-%Y %H:%M:%S"
paiva = datetime.date.today().strftime("%d-%m-%Y")
kello = time.strftime("%H:%M:%S")
aika = paiva + " " + kello

time2  = datetime.datetime.strptime('11-04-2020 15:00:00', date_format)
time1  = datetime.datetime.strptime(aika, date_format)

diff = time2 - time1

days = diff.days

hours = int((diff.seconds) / 3600)

minutes = int(((diff.seconds) / 60) % 60)

seconds = diff.seconds % 60

toast.show_toast("Overwatch League Paris 2020",
                   "{0} päivää, {1} tuntia, {2} minuuttia, {3} sekuntia".format(days, hours, minutes, seconds),
                   icon_path="owl.ico",
                   duration=25)

exit(0)