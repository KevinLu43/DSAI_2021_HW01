# Python Internal Module Import
from datetime import date, datetime, timedelta

# Python External Moudule Import
import numpy as np
import pandas as pd
from loguru import logger

# User Module Import

# Encode time series data as MIMO format (Input: 7, Output: 7)
@logger.catch
def mimo_77(input_df_data):
    
    data_group_7d = list()
    final_bind_dataset = list()

    # Group data by 7 days
    for i in range(len(input_df_data.index)):
        row_day = input_df_data["日期"][i]
        parse_period = np.array(datetime.strptime(row_day, "%Y/%m/%d").date(), dtype=np.datetime64) + np.arange(7)
        parse_period = list((lambda x: x.strftime("%Y/%m/%d"))(data.astype(datetime)) for data in parse_period)
        
        extracted_ts_data = input_df_data.loc[input_df_data["日期"].isin(parse_period)]
        if len(extracted_ts_data.index) == 7:
            # print(parse_period)
            data_group_7d.append(extracted_ts_data)
        else:
            break
    
    for i in range(len(data_group_7d)):
        if (i + 7) >= len(data_group_7d):
            break

        encoded_tuple = tuple((data_group_7d[i], data_group_7d[i + 7]))
        final_bind_dataset.append(encoded_tuple)

    logger.debug(f"[Data Count] Original({len(input_df_data.index)}) -> Encoded TS({len(data_group_7d)}) -> Binded For Training({len(final_bind_dataset)})")

    return final_bind_dataset