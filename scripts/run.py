import datetime
import bhavcopy_reader as br
import redis_wrapper as rw

def main():
    now = str(datetime.date.today())
    day, month, year = (list(now.split('-'))[::-1])
    print(day, month, year)
    day = '31'
    
    year = year[2:]

    bhavcopy_url = 'http://www.bseindia.com/download/BhavCopy/Equity/EQ{}{}{}_CSV.ZIP'.format(day, month, year)
    print(bhavcopy_url)

    date_key = day + month + year
    values = br.get_bhav_copy(bhavcopy_url)
    if len(values) > 0:
        rw.save_data('lastdate', date_key)

    headers = []
    CODE    = 0
    NAME    = 0
    OPEN    = 0
    HIGH    = 0
    LOW     = 0
    CLOSE   = 0
    TYPE    = 0

    for index, data in enumerate(values):
        data = data.decode("utf-8")
        data = data.split(",")
        if index == 0:
            headers = data
            CODE    = headers.index('SC_CODE')
            NAME    = headers.index('SC_NAME')
            OPEN    = headers.index('OPEN')
            HIGH    = headers.index('HIGH')
            LOW     = headers.index('LOW')
            CLOSE   = headers.index('CLOSE')
            TYPE    = headers.index('SC_TYPE')
        else:
            if data[TYPE] == "Q":
                code        = data[CODE]
                name        = data[NAME]
                open_price  = data[OPEN]
                high_price  = data[HIGH]
                low_price   = data[LOW]
                close_price = data[CLOSE]

                key         = date_key + ':' + code
                tmp_name    = rw.get_data(code)
                if tmp_name != "":
                    name        = tmp_name if tmp_name != "" else name
                    value_set   = [name, open_price, high_price, low_price, close_price]

                    rw.save_data(key, value_set)

main()
