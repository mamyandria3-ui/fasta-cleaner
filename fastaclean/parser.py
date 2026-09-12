#!/bin/env python3

def parse_fasta(file_path: str) -> dict[str, str]:
    result: dict[str, str] = {}

    with open(file_path, 'r') as f:
        current_header: str = ""
        current_sequence: str = ""
        for line in f:
            if line.startswith('>'):
                if current_header:
                    result[current_header] = current_sequence
                current_header = line[1:].strip()
                current_sequence = ""
            else:
                current_sequence += line.strip()
        if current_header:
            result[current_header] = current_sequence

    return result
