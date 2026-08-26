.PHONY: install run check

install:
	python3 -m pip install -e .

run:
	PYTHONPATH=src python3 main.py

check:
	PYTHONPATH=src python3 -m unittest discover -s tests -v
