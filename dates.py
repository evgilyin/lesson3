#Напечатайте в консоль даты: вчера, сегодня, месяц назад
from datetime import datetime, timedelta
dt_now = datetime.now().strftime('%d/%m/%Y')
delta1 = timedelta(days=1)
delta30 = timedelta(days=30)

#Сегодня:
print(dt_now)

#Вчера:
print((datetime.now() - delta1).strftime('%d/%m/%Y'))

#Месяц назад
print((datetime.now() - delta30).strftime('%d/%m/%Y'))


#Превратите строку "01/01/17 12:10:03.234567" в объект datetime
date_string = "01/01/17 12:10:03.234567"
date_dt = datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
print(date_dt)