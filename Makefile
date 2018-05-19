example:
	venv/bin/python main.py

clean:
	rm -f data/*.txt

venv:
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt

test: venv
	venv/bin/python -m pytest
