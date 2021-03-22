# Python Internal Module Import
from datetime import datetime, timedelta

# Python External Moudule Import
import numpy as np
import pandas as pd
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
from loguru import logger

# User Module Import
@logger.catch
def train(train_list, test_list):

    model_train = make_pipeline(StandardScaler(), SVR(epsilon=0.2, kernel='linear', coef0=0.0))
    # model_all = make_pipeline(StandardScaler(), SVR(C=1.0, epsilon=0.2))

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

    infres = clf.predict(X_test)

    for i in range(len(infres)):
       infres[i] = infres[i] + np.random.uniform(low=0.0, high=50.0, size=(7,))

    clf_all = MultiOutputRegressor(model_train).fit(X_train + X_test, Y_train + Y_test)

    logger.debug(f"Model: SVR, Testing Set RMSE -> {mean_squared_error(Y_test, infres, squared = False)}")

    # infres = clf_all.predict(X_test)
    # logger.debug(f"Model: SVR, Testing Set RMSE -> {mean_squared_error(Y_test, infres, squared = False)}")

    return clf_all

@logger.catch
def inference(model, df_input):
    return model.predict([df_input["備轉容量(MW)"]]) + np.random.uniform(low=0.0, high=50.0, size=(7,))