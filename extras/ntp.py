import ntplib
from time import ctime


def obtener_hora_NTP():

    c = ntplib.NTPClient();
    response = c.request('localhost') #esta una hora adelantado, hay que averiguar otro de UY o BsAs
    return ctime(response.tx_time)

