PYTHON=python3
SCRIPT=scripts/fetch_sample.sh
RAW_DIR=data/raw
CLEAN_DIR=data/cleaned
REPORT_DIR=data/report
FLAKE=flake8
MYPY=mypy

CYAN := \033[1;36m
GREEN := \033[1;32m
YELLOW := \033[1;33m
BLUE := \033[1;34m
BOLD := \033[1m
RESET := \033[0m

.PHONY: all fetch run test clean help lint

all: banner help

banner:
	@echo "${CYAN}"
	@cat banner.txt 2>/dev/null || echo " FASTACLEAN"
	@echo "${RESET}"

fetch:
	@chmod +x $(SCRIPT)
	@bash $(SCRIPT)

run: fetch
	@mkdir -p data/cleaned/
	@mkdir -p data/report/
	@$(PYTHON) main.py --input $(RAW_DIR)/sample.fasta --output $(CLEAN_DIR)/clean.fasta --report $(REPORT_DIR)/report.json
	@echo ""
	@echo " ${GREEN} Cleaning completed successfully!${RESET}"
	@echo " ${CYAN} Cleaned FASTA file: ${RESET} data/cleaned/clean.fasta"
	@echo " ${CYAN} Execution report: ${RESET} data/report/report.json"
	@echo ""

test:
	@$(PYTHON) -m unittest discover tests

clean:
	@rm -rf $(RAW_DIR)
	@rm -rf $(CLEAN_DIR)
	@rm -rf $(REPORT_DIR)
	@find . -type d \( -name "__pycache__" -o -name ".mypy_cache" \) -exec rm -rf {} +
	@echo "${YELLOW} All downloaded, generated outputs and cache directories have been removed. ${RESET}"

lint:
	@$(FLAKE) --exclude=.venv,data,.git,__pycache__ .
	@$(MYPY) --strict --exclude "(.venv|data|\.git|__pycache__)" .

help:
	@echo ""
	@echo "${BOLD} FASTACLEAN — CLI Helper${RESET}\n"
	@echo ""
	@printf "  ${GREEN}%-12s${RESET} %s\n" "make fetch" "Download sample genome dataset"
	@printf "  ${GREEN}%-12s${RESET} %s\n" "make run"   "Execute cleaning pipeline & generate a JSON report"
	@printf "  ${GREEN}%-12s${RESET} %s\n" "make test"  "Run unit tests (unittest)"
	@printf "  ${GREEN}%-12s${RESET} %s\n" "make lint"  "Check code style & static typing (flake8 & mypy)"
	@printf "  ${GREEN}%-12s${RESET} %s\n" "make clean" "Deletes the downloaded, cleaned data, the report and Python cache"
	@echo ""
