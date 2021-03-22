OUTPUT_FILE = "submission.csv"

run:
	pipenv run python app.py --output $(OUTPUT_FILE)

download_or_data:
	curl "http://data.taipower.com.tw/opendata/apply/file/d006002/%E6%9C%AC%E5%B9%B4%E5%BA%A6%E6%AF%8F%E6%97%A5%E5%B0%96%E5%B3%B0%E5%82%99%E8%BD%89%E5%AE%B9%E9%87%8F%E7%8E%87.csv" --output datasets/original/power_or_info.csv