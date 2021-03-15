# DSAI_2021_HW01
 
## :droplet: Source of the dataset
*    The content of power dataset is collected from two different source.

### :sweat_drops: Dataset Source 1
* Go to [TaiPower Company - 過去電力供應資訊](https://www.taipower.com.tw/tc/page.aspx?mid=210)
* Use web developer tool (F12) in Chrome, Select `Network` console, as the picture shown downward
![Image_Network_Console](https://i.imgur.com/c8J4acw.jpg)
* Click calender icon on the page and randomly select a day.
* Then, network console will show a downloaded file - `sys_dem_dump.csv`
    * This file includes all the data shown on the page.
    * Duration: *2020/01/01 ~ 2021/01/31*
* Copy the content shown on the web developer tool, then save to local csv file.

### :sweat_drops: Dataset Source 2
* We download same data from [開放政府資料平台 - 電力資料](https://data.gov.tw/dataset/19995)
    * Duration: *2019/01/01 ~ 2020/10/31*
    * Including label of each field
* After comparing the csv file from TaiPower Official website, the content and field of data is identical for overlapping interval.
    * So, we integrate the content of csv file from two different source.
    * Duration of integrated csv: *2019/01/01 ~ 2021/01/31*
