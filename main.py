#!/usr/bin/env python3


import argparse
import json
from fastaclean.parser import parse_fasta
from fastaclean.filter import filter_sequences


def parse_arguments() -> argparse.Namespace:
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
    with open(path, "w", encoding="utf-8") as file:
        for header, seq in clean.items():
            if not header.startswith(">"):
                header = f">{header}"
            file.write(f"{header}\n")
            file.write(f"{seq}\n")


def write_report(path: str, stats: dict[str, int]) -> None:
    with open(path, "w", encoding="utf-8") as file:
        json.dump(stats, file, indent=4)


if __name__ == "__main__":
    args = parse_arguments()
    input_path = args.input
    output_path = args.output
    report_path = args.report
    min_length = args.min_length
    max_n_percent = args.max_n_percent

    result_parse = parse_fasta(input_path)
    result_filter = filter_sequences(result_parse,
                                     min_length,
                                     max_n_percent)

    clean, stats = result_filter
    write_clean_fasta(output_path, clean)
    write_report(report_path, stats)
