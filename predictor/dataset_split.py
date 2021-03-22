# Python Internal Module Import
from datetime import datetime, timedelta

# Python External Moudule Import
import numpy as np
import pandas as pd
from loguru import logger

# User Module Import

# Dataset splitter - By date
@logger.catch
def split_by_date(data_list, date_threshold):
    
    get_datetime_date = lambda x: datetime.strptime(x, "%Y/%m/%d").date()
    date_filter = get_datetime_date(date_threshold)
    training_set = list()
    testing_set = list()

    for ip_data, op_data in data_list:
        date_base = get_datetime_date(ip_data["日期"].reset_index(drop=True)[6])
        
        # print(f"{date_base} -> {date_base <= date_filter}")
        if date_base <= date_filter:
            training_set.append((ip_data, op_data))
        else:
            testing_set.append((ip_data, op_data))

    logger.debug(f"Input data count: {len(data_list)} => ({len(training_set)},{len(testing_set)}) [training set, testing set]")

    return training_set, testing_set