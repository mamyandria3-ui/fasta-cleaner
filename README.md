*Built as part of my bioinformatics learning journey — my first project in the field.*

# FASTACLEAN

**FASTACLEAN** is a command-line tool (CLI) for cleaning, validating, and analyzing **FASTA** files. It ingests a raw file, checks the validity of nucleotide sequences, computes statistics (length, GC content), filters out unwanted sequences, and exports a clean FASTA file along with a summary report.

```
 ███████╗ █████╗ ███████╗████████╗ █████╗  ██████╗██╗     ███████╗ █████╗ ███╗   ██╗
 ██╔════╝██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║     ██╔════╝██╔══██╗████╗  ██║
 █████╗  ███████║███████╗   ██║   ███████║██║     ██║     █████╗  ███████║██╔██╗ ██║
 ██╔══╝  ██╔══██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██║██║╚██╗██║
 ██║     ██║  ██║███████║   ██║   ██║  ██║╚██████╗███████╗███████╗██║  ██║██║ ╚████║
 ╚═╝     ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
```

---

## Description

FASTACLEAN was built to automate a common bioinformatics task: preparing a raw FASTA dataset before downstream analysis. The full pipeline performs the following steps:

- **Ingestion & Validation** — Reads a raw `.fasta` file and checks that every sequence contains only valid nucleotides (`A`, `T`, `C`, `G`, `N`).
- **Analysis & Metrics** — Computes the length of each sequence and its GC content (proportion of guanine and cytosine).
- **Filtering** — Excludes sequences that:
  - fall below a user-defined minimum length;
  - contain a percentage of unknown nucleotides (`N`) above a user-defined tolerance.
- **Export** — Generates a cleaned `.fasta` file and a JSON summary report (`report.json`) with statistics and filtering results.

### Why not Biopython?

This project intentionally does not rely on [Biopython](https://biopython.org/). The goal was educational: implementing FASTA parsing, nucleotide validation, GC-content calculation, and sequence filtering from scratch, using only the Python standard library, in order to actually understand the underlying logic rather than calling a library that does it for you.

### Project structure

```
fasta-clean/
├── data/
│   ├── raw/                 # Raw FASTA files
│   ├── cleaned/             # Filtered FASTA files
│   └── report/              # JSON report
├── scripts/
│   └── fetch_sample.sh      # Shell script to download a sample dataset
├── fastaclean/
│   ├── __init__.py
│   ├── parser.py            # FASTA file reading and validation
│   ├── metrics.py           # Statistical calculations (GC content, length)
│   └── filter.py            # Sequence filtering logic
├── main.py                  # CLI entry point (argparse)
├── tests/
│   ├── test_parser.py       # Unit tests for FASTA parser
│   ├── test_metrics.py      # Unit tests for metrics and statistics
│   └── test_filter.py       # Unit tests for filtering rules
├── Makefile                 # Automation (setup, run, test, clean, lint)
└── README.md                # Full documentation
```

---

## Instructions

### Requirements

- Python 3.10.12 (or later)
- `flake8` and `mypy` (for linting, optional)
- `curl` and `gunzip` (only needed for `make fetch`)

### Installation

Clone the repository and move into the project root:

```bash
git clone https://github.com/mamyandria3-ui/fasta-cleaner.git fasta-clean
cd fasta-clean
```

### Available commands (Makefile)

| Command       | Description                                                    |
|---------------|------------------------------------------------------------------|
| `make fetch`  | Downloads a sample FASTA dataset into `data/raw/`                 |
| `make run`    | Runs the cleaning pipeline and generates a JSON report            |
| `make test`   | Runs the unit tests (`unittest`)                                   |
| `make lint`   | Checks code style and static typing (`flake8`, `mypy`)             |
| `make clean`  | Removes downloaded/generated data and the Python cache             |
| `make help`   | Displays help and the list of available commands                   |

### Example usage

```bash
# 1. Download a sample FASTA file
make fetch

# 2. Run the cleaning pipeline
make run
```

After `make run`, you get:

- The cleaned FASTA file: `data/cleaned/clean.fasta`
- The execution report: `data/report/report.json`

The sample dataset used by `make fetch` is the *Saccharomyces cerevisiae* reference genome (S288C / RefSeq `GCF_000146045.2`), downloaded from the NCBI FTP server.

The program can also be called directly, with custom parameters:

```bash
python3 main.py --input data/raw/sample.fasta \
                 --output data/cleaned/clean.fasta \
                 --report data/report/report.json \
                 --min-length 50 \
                 --max-n-percent 5.0
```

Before running the script directly wit `./main.py`, you must first download the required test dataset by executing the dedicated Shell script:


```bash
chmod +x fetch_sample.sh
./fetch_sample.sh
```

#### CLI options

| Option                  | Short | Type    | Default | Description                                  |
|--------------------------|-------|---------|---------|-----------------------------------------------|
| `--input`                | `-i`  | `str`   | —       | Path to the raw input FASTA file (required)    |
| `--output`               | `-o`  | `str`   | —       | Path to the output filtered FASTA file (required) |
| `--report`               | `-r`  | `str`   | —       | Path to the output JSON report (required)      |
| `--min-length`           | `-m`  | `int`   | `0`     | Minimum sequence length to keep                |
| `--max-n-percent`        | `-n`  | `float` | `100.0` | Maximum tolerated percentage of `N` bases      |

### Running the tests

```bash
make test
```

---

## Resources

- [FASTA format — Wikipedia](https://en.wikipedia.org/wiki/FASTA_format)
- [Python `argparse` documentation](https://docs.python.org/3/library/argparse.html)
- [flake8 — Style guide enforcement](https://flake8.pycqa.org/)
- [mypy — Static typing for Python](https://mypy-lang.org/)
- [NCBI genome assembly GCF_000146045.2 (S. cerevisiae)](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/)

## AI Usage

AI assistance was used during the development of this project, specifically to:

- better understand the FASTA file format and its conventions;
- learn how to use Python's argparse module;
- write clearer docstrings;
- draft and refine this README.

---
