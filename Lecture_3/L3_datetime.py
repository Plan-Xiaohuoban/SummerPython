import datetime

now = datetime.datetime.now()
print(now)


# class datetime in datetime.py
# from datetime import datetime
# now = datetime.now()
# print(now)

print(now.strftime('%Y----%m----%d--- %H------%M'))
# print(now.strftime('%Y年%m月%d日 %H:%M'))

import locale

locale.setlocale(locale.LC_CTYPE, "chinese")
print(now.strftime("%Y年%m月%d日%H时%M分"))

