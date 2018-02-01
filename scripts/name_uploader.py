import csv
import redis_wrapper as rw


def main():
    with open('Equities_Master_List_Kite.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            bse_code = row['BSE.Code']
            company_name = row['Name']
            company_name = company_name.upper()
            rw.save_data(company_name, bse_code)
            rw.save_data(bse_code, company_name)


main()
