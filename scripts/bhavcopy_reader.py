import requests
from zipfile import ZipFile
from io import BytesIO

def get_bhav_copy(file_url):
    values = []
    response = requests.get(file_url)
    if response.status_code == 200:
        zf = ZipFile(BytesIO(response.content))
        file_name = zf.namelist()[0]
        with zf.open(file_name) as zf_file:
            values = zf_file.readlines()

    return values




