.PHONY: install run run-normal run-failure check

install:
	python3 -m pip install -e .

run: run-normal run-failure

run-normal:
	PYTHONPATH=src python3 main.py normal

run-failure:
	PYTHONPATH=src python3 main.py failure

check:
	PYTHONPATH=src python3 -m unittest discover -s tests -v
