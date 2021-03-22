# Python Internal Module Import
import os
import argparse

# Python External Moudule Import
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from loguru import logger

# User Module Import

def point_distribution(input_pd_data):


    plt.figure()
    input_pd_data[["日期", "備轉容量(MW)"]].plot(style='x')
    plt.legend(loc='best')
    if not os.path.isdir("./output"):
        os.mkdir("./output")
    plt.savefig('./output/point_distribution_result.jpg')
