# Python Internal Module Import
from datetime import datetime, timedelta

# Python External Moudule Import
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from loguru import logger

# User Module Import

def train(train_list, test_list):
    
    model_train = make_pipeline(StandardScaler(), 
                    KNeighborsRegressor(n_neighbors=7, weights='uniform'))
    
    X_train = list()
    Y_train = list()
    X_test = list()
    Y_test = list()
    for x, y in train_list:
        X_train.append(x["備轉容量(MW)"])
        Y_train.append(y["備轉容量(MW)"])

    for x, y in test_list:
        X_test.append(x["備轉容量(MW)"])
        Y_test.append(y["備轉容量(MW)"])

    clf = MultiOutputRegressor(model_train).fit(X_train, Y_train)

    print(MultiOutputRegressor(model_train))

    infres = clf.predict(X_test)

    print(mean_squared_error(Y_test, infres, squared = False))


    '''print(train_list)
    print(test_list)'''

def inference(model, df_input):
    pass