#!/usr/bin/env python3
"""Command-line interface (CLI) for Fastaclean.

This module provides the main entry point for reading, filtering, and writing
FASTA sequence files. It parses command-line arguments, delegates sequence
parsing and filtering to internal modules, and exports filtered FASTA files
along with execution statistics in JSON format.
"""

import argparse
import json
import sys
import os
from fastaclean import filter_sequences
from fastaclean import parse_fasta


RESET = "\033[0m"
GREEN = "\033[32m"
CYAN = "\033[36m"


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments for Fastaclean workflow execution.

    Returns:
        argparse.Namespace: Object containing parsed CLI arguments:
            - input (str): Path to the raw input FASTA file.
            - output (str): Path for the output filtered FASTA file.
            - report (str): Path for the JSON summary report.
            - min_length (int): Minimum sequence length threshold (default: 0).
            - max_n_percent (float): Maximum allowed percentage of 'N' bases
                (default: 100.0).
    """
    parser = argparse.ArgumentParser(
        description="Fastaclean: nettoyage et filtrage de fichiers FASTA."
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="Chemin vers le fichier FASTA brut"
    )

    parser.add_argument(
        "-o", "--output",
        type=str,
        required=True,
        help="Chemin vers le fichier FASTA de sortie"
    )

    parser.add_argument(
        "-r", "--report",
        type=str,
        required=True,
        help="Chemin vers le fichier de sortie du rapport"
    )

    parser.add_argument(
        "-m", "--min-length",
        type=int,
        default=0,
        help="Longueur minimale d'une sequence"
    )

    parser.add_argument(
        "-n", "--max-n-percent",
        type=float,
        default=100.0,
        help="Pourcentage maximal de N tolere"
    )

    return parser.parse_args()


def write_clean_fasta(path: str, clean: dict[str, str]) -> None:
    """Write cleaned and filtered sequences to a destination FASTA file.

    Args:
        path (str): Destination file path for the output FASTA file.
        clean (dict[str, str]): Dictionary mapping
            sequence headers to sequence strings.
    """
    parent_dir = os.path.dirname(path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        for header, seq in clean.items():
            if not header.startswith(">"):
                header = f">{header}"
            file.write(f"{header}\n")
            file.write(f"{seq}\n")


def write_report(path: str, stats: dict[str, int]) -> None:
    """Write processing statistics to a JSON summary report file.

    Args:
        path (str): Destination file path for the JSON summary report.
        stats (dict[str, int]): Dictionary containing
            sequence execution metrics
    """
    parent_dir = os.path.dirname(path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(stats, file, indent=4)


if __name__ == "__main__":
    args = parse_arguments()
    input_path = args.input
    output_path = args.output
    report_path = args.report
    min_length = args.min_length
    max_n_percent = args.max_n_percent

    try:
        result_parse = parse_fasta(input_path)
        clean, stats = filter_sequences(
            result_parse,
            min_length,
            max_n_percent
        )
        write_clean_fasta(output_path, clean)
        write_report(report_path, stats)

    except FileNotFoundError as e:
        print(f"Error: Specified file not found: {e}", file=sys.stderr)
        sys.exit(1)
    except PermissionError as e:
        print(f"Error: Permission denied: {e}", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid argument or format error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)
    else:
        print()
        print(f"{GREEN} Cleaning completed successfully !{RESET}")
        print(f"{CYAN} Cleaned FASTA file: {RESET} data/cleaned/clean.fasta")
        print(f"{CYAN} Execution report: {RESET} data/report/report.json")
        print()
