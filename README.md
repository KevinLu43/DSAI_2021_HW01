# DSAI_2021_HW01

## 🗜️ Highlight of each phase in app.py.
*   Crawler Phase 
    *    We utilize dataset [台灣電⼒公司_本年度每⽇尖峰備轉容量率](https://data.gov.tw/dataset/25850) to train our model.
    *    The crawler fetchs data from the link upward to get information at 2021/03/22
    *    For fairness, we remove data after deadline of the homework (2021/03/22)
*   Preprocessing Phase
    *    Convert unit of operating reserve from 10MW (萬瓩) to MW.
    *    Encode original data to time series format.
        *    Input: **7 days OR info time series**
        *    Output: **OR info series for next 7 days**
    *    Encoded data is suitable for *MIMO model*.
*   Training Phase
    *   Model: **Support Vector Regression (SVR)** with *Multiple Output* and random noise
    *   Hyperparameter: kernel function 'linear' with epsilon 0.2 (Other configs are default value)
        *    Reference: https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html
    *   Utilize `RMSE` as testing set mertic 
    *   Based on the output result of model and trend of OR last few weeks, we add a random noise on SVR result to make a better fitting.
*   Infernece Phase
    *   Utilize our model to do infernece
    *   Input data from 2021/03/16 to 2021/03/22 with OR info.
    *   Output predicted OR from 2021/03/23 to 2021/03/29
    *   In final, output result to *submission.csv* with assigned format
* We use some Python modules to finish our work
    *   NumPy, Pandas, Scikit-Learn, Logru...etc. 

## :camera_flash: Running my code
*   Virtual Python Environment
    *   If you use `virtualenv`, launch your environment and run `pip install -r requiements.txt`.
    *   If you use `pipenv`, run `pipenv install` after your environment is created.
*   Run app.py to output submission.csv, some log info will show on your screen.
    *   **!!!DO NOT DISABLE TaiPower Data Crawler by input argument, it's for testing only!!!!!**
*   Example with using `pipenv`
```shell
$ pipenv run python app.py
2021-03-22 21:28:53.647 | SUCCESS  | __main__:<module>:17 - DSAI 2021 Spring Homework 01 - Power Operating Reserve Predicter
2021-03-22 21:28:53.647 | SUCCESS  | __main__:<module>:18 -          <--This code is written By Steven HH Chen-->           
2021-03-22 21:28:53.647 | INFO     | __main__:<module>:20 - Reading input arguments...
...
2021-03-22 21:28:53.727 | SUCCESS  | __main__:<module>:87 - <---------------Inference Phase--------------->
2021-03-22 21:28:53.727 | INFO     | __main__:<module>:88 - Utilize model to do inference
[[3079.43010643 3097.42074692 3089.42502867 3113.23175651 3055.8999642
  3129.75828712 3074.91791311]]
2021-03-22 21:28:53.729 | SUCCESS  | __main__:<module>:94 - Output the result of OR for next 7 days...
$ ls -l submission.csv
-rw-rw-r-- 1 netdb-ml netdb-ml   133  三  22 21:28 submission.csv
```
