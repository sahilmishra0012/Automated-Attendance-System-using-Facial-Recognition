import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('pool.ntp.org')
    time=ctime(response.tx_time)
    print(time[-4:])
    print(time[-13:-5])

if __name__ == '__main__':
    print_time()