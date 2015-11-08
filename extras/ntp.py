import ntplib
from time import ctime
import datetime


def obtener_hora_NTP():

    c = ntplib.NTPClient()
    response = c.request('localhost')
    return ctime(response.tx_time)


def hora():
    c = ntplib.NTPClient()
    response = c.request('localhost')
    hora = datetime.datetime.fromtimestamp(response.tx_time)
    hora_final = datetime.datetime(year=hora.year,month=hora.month,day=hora.day,hour=hora.hour,minute=hora.minute,second=hora.second)
    return hora_final

