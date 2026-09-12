PYTHON=python3
SCRIPT=scripts/fetch_sample.sh
RAW_DIR=data/raw
CLEAN_DIR=data/cleaned
FLAKE=flake8
MYPY=mypy

.PHONY: all fetch run test clean help lint

all: help

fetch:
	@chmod +x $(SCRIPT)
	@bash $(SCRIPT)

run:
	$(PYTHON) main.py --input $(RAW_DIR)/sample.fasta --output $(CLEAN_DIR)/sample_clean.fasta

test:
	$(PYTHON) -m unittest discover tests

clean:
	@rm -rf $(RAW_DIR)/*
	@rm -rf $(CLEAN_DIR)/*
	@find . -type d -name "__pycache__" -exec rm -rf {} +

lint:
	$(FLAKE) --exclude=.venv, data,.git,__pycache__ .
	$(MYPY) --strict--exclude "(.venv|data|\.git|__pycache__)" .

help:
	@echo "Commandes disponibles pour fasta-clean"
	@echo " make fetch - Telecharge le genome reference d'E.coli"
	@echo " make run - Execute le parser Python"
	@echo " make test - Lance la suite des tests unitaires"
	@echo " make clean - Supprime les donnees telechargees et generees"
	@echo " verifie le style et le typage du code"
