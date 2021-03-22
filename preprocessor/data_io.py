# Python Internal Module Import
from datetime import datetime, timedelta

# Python External Moudule Import
import requests
import numpy as np
import pandas as pd
from loguru import logger

# User Module Import

# Read dataset
@logger.catch
def read_csv_to_pandas_df(filename):
    return pd.read_csv(filename, low_memory=False)

# Download Dataset from TaiPower Company
@logger.catch
def get_TaiPower_or_data():
    url = "http://data.taipower.com.tw/opendata/apply/file/d006002/本年度每日尖峰備轉容量率.csv"
    filename = "power_or_info.csv"

    req = requests.get(url, allow_redirects=True)

    open(f"./datasets/{filename}", 'wb').write(req.content)


@logger.catch
def output_predict_or_data(predict_result, filename_output, date_base):

    assert(len(predict_result) == 7)
    date = datetime.strptime(date_base, "%Y/%m/%d")

    file = open(filename_output, "w")
    file.write("date,operating_reserve(MW)\r\n")

    for i in range(7):
        write_str = date.strftime("%Y%m%d") + f",{int(predict_result[i])}\r\n"
        file.write(write_str)
        date = date + timedelta(days=1)

    file.close()

if __name__ == "__main__":
    pass
