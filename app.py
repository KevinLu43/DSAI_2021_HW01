# Python Internal Module Import
import argparse
from datetime import datetime

# Python External Moudule Import
import numpy as np
import pandas as pd
from loguru import logger


# User Module Import
from preprocessor import data_io, data_or_transfer, data_ts_encode
from visualizor import original_data_plot
from predictor import dataset_split, svr, knr, random

if __name__ == "__main__":
    logger.success("DSAI 2021 Spring Homework 01 - Power Operating Reserve Predicter")
    logger.success("         <--This code is written By Steven HH Chen-->           ")

    logger.info("Reading input arguments...")
    parser = argparse.ArgumentParser()

    parser.add_argument('--training',
                        default='power_or_info.csv',
                        help='input training data file name')
    parser.add_argument('--output',
                        default='submission.csv',
                        help='output file name')
    parser.add_argument('--no_crawling',
                        action="store_true",
                        help='option for disabling crawler')
    parser.add_argument('--dataset_date_threshold',
                        default='2021/03/22',
                        help='Threshold for deleting data before specific date')
    parser.add_argument('--split_date_threshold',
                        default='2021/03/03',
                        help='Threshold for spliting training and testing data before specific date')
    args = parser.parse_args()
    logger.debug(f"Training data input csv file    -> ./datasets/original/{args.training}")
    logger.debug(f"Model Prediction Outcome Output -> ./output/deploy/{args.output}")
    logger.debug(f"Run TaiPower Data Crawler       -> {not args.no_crawling}")
    logger.critical(f"Dataset Date Threshold          -> {args.dataset_date_threshold}")
    logger.debug(f"Dataset Split Date Threshold    -> {args.split_date_threshold}")

    #--------------------------------------------------------------
    logger.success("<---------------Crawler Phase--------------->")
    logger.critical(f"!!!!!PLEASE NOTE THAT data for training phase only utilizes data before {args.dataset_date_threshold} for fairness!!!!!")
    
    if not args.no_crawling:
        logger.info("Download data from TaiPower Company...")
        data_io.get_TaiPower_or_data()

    logger.info("Read csv data for operating reserve")
    or_data = data_io.read_csv_to_pandas_df(f"datasets/original/{args.training}")

    logger.info(f"Remove data after {args.dataset_date_threshold}")
    time_inrange = lambda x: datetime.strptime(x, "%Y/%m/%d") <= datetime.strptime(args.dataset_date_threshold, "%Y/%m/%d")
    or_data = or_data.loc[or_data["日期"].apply(time_inrange)].reset_index()

    #--------------------------------------------------------------
    logger.success("<---------------Preprocessing Phase--------------->")

    logger.info("Convert unit of OR [萬瓩 -> MW]")
    or_data_MW = data_or_transfer.unit_to_MW(or_data, "備轉容量(萬瓩)", "備轉容量(MW)")

    # logger.info("Plot the distribution of data")
    # original_data_plot.point_distribution(or_data_MW)

    # Encode time series data based on time series dataset
    logger.info("Encoding Time Series Data")
    data_ts_encoded = data_ts_encode.mimo_77(or_data_MW)

    #--------------------------------------------------------------
    logger.success("<---------------Training Phase--------------->")

    # Note: This is internal split for training model
    logger.info("Split training and validation set for model training")
    training_set, testing_set = dataset_split.split_by_date(data_ts_encoded, args.split_date_threshold)

    # 
    logger.info("Train Model")
    model = svr.train(training_set, testing_set)

    # logger.info("Effectiveness verification by testing set")

    #--------------------------------------------------------------
    logger.success("<---------------Inference Phase--------------->")
    logger.info("Utilize model to do inference")
    date_duration = np.array(datetime.strptime("2021/03/16", "%Y/%m/%d").date(), dtype=np.datetime64) + np.arange(7)
    parse_period = list((lambda x: x.strftime("%Y/%m/%d"))(data.astype(datetime)) for data in date_duration)
    inf_res = svr.inference(model, or_data_MW.loc[or_data_MW["日期"].isin(parse_period)])
    print(inf_res)

    logger.success("Output the result of OR for next 7 days...")
    data_io.output_predict_or_data(inf_res[0], args.output, "2021/03/23")
