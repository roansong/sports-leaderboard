example:
	venv/bin/python main.py

test:
	pytest

clean:
	rm -f data/*.txt

rmvenv:
	rm -rf venv

venv: rmvenv
	python3 -m venv venv
	venv/bin/pip install -r requirements.txt
