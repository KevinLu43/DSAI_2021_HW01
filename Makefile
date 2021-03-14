OUTPUT_FILE = "submission.csv"

run:
	pipenv run python app.py --output $(OUTPUT_FILE)