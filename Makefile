.PHONY: install run check

install:
	python -m pip install -e .

run:
	python main.py

check:
	python -m unittest discover -s tests -v
