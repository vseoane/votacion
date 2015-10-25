import ntplib
from time import ctime


def obtener_hora_NTP():

    c = ntplib.NTPClient();
    response = c.request('uy.pool.ntp.org', version=3) #esta una hora adelantado, hay que averiguar otro de UY o BsAs
    return ctime(response.tx_time)

