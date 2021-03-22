# Python Internal Module Import

# Python External Moudule Import
import numpy as np
import pandas as pd
from loguru import logger

# User Module Import

# power operating reserve info processing
@logger.catch
def unit_to_MW(input_pd_data, col_name_input, col_name_output):
    or_data_MW = input_pd_data
    or_data_MW[col_name_input] = input_pd_data[col_name_input].apply(lambda x: x * 10)
    or_data_MW = or_data_MW.rename(columns={col_name_input: col_name_output})
    return or_data_MW

# C
@logger.catch
def or_normalize(input_pd_data, col_name_input, col_name_output):
    or_data_normalize = input_pd_data
    min_value = input_pd_data[col_name_input].min()
    or_data_MW[col_name_input] = input_pd_data[col_name_input].apply(lambda x: x - min_value + 900)