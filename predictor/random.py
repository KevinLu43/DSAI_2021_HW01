# Python Internal Module Import
import random
from datetime import datetime, timedelta

# Python External Moudule Import
import numpy as np
import pandas as pd
from loguru import logger
from sklearn.metrics import mean_squared_error

# User Module Import


def random_output(middle_val, low_range, high_range):
    
    return np.random.uniform(low=(middle_val - low_range), high=(middle_val + high_range), size=(7,))

def train(train_list, test_list):
    
    # avg_collection = [df["備轉容量(MW)"].mean() for df, _ in test_list]
    
    output_list = [random_output(3050, 100, 100) for _ in range(len(test_list))]

    print(mean_squared_error(output_list, [y["備轉容量(MW)"] for _, y in test_list]))


def inference(model, df_input):
    pass