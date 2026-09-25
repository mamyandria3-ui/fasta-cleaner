"""Sequence processing and quality metric utilities for genomic data.

This module provides basic tools to clean raw nucleotide sequences (DNA/RNA)
and compute key metrics such as sequence length, GC content percentage, and
unknown/ambiguous base (N) ratio.
"""


def clean_sequence(sequence: str) -> str:
    """Clean sequence by removing whitespace and converting to uppercase.

    Args:
        sequence (str): Input nucleotide sequence to be cleaned.

    Returns:
        str: Cleaned sequence without spaces
        or newline characters, converted to uppercase.
        Returns an empty string if the input sequence is empty or invalid.
    """
    if not sequence:
        return ""
    seq = (
        sequence.replace(" ", "")
        .replace("\n", "")
        .replace("\r", "")
        .upper()
    )
    return seq


def len_sequence(sequence: str) -> int:
    """Calculate the actual nucleotide length of a sequence after cleaning.

    Args:
        sequence (str): Input nucleotide sequence.

    Returns:
        int: The total count of nucleotides in the cleaned sequence.
    """
    seq = clean_sequence(sequence)
    return len(seq)


def gc_content(sequence: str) -> float:
    """Calculate the GC content percentage of a nucleotide sequence.

    Args:
        sequence (str): Input nucleotide sequence (DNA/RNA).

    Returns:
        float: The percentage of Guanine (G) and Cytosine (C)
        bases relative to the total sequence length,
        rounded to 2 decimal places. Returns 0.0 if the sequence is empty.
    """
    seq = clean_sequence(sequence)
    if not seq:
        return 0.0
    gc_quantity = seq.count('C') + seq.count('G')
    gc = (gc_quantity / len(seq)) * 100
    return round(gc, 2)


def n_content(sequence: str) -> float:
    """Calculate the percentage of ambiguous or unknown bases in a sequence.

    Args:
        sequence (str): Input nucleotide sequence.

    Returns:
        float: The percentage of 'N' bases relative
        to the total sequence length, rounded to 2 decimal places.
        Returns 0.0 if the sequence is empty.
    """
    seq = clean_sequence(sequence)
    if not seq:
        return 0.0
    n_quantity = seq.count('N')
    n = (n_quantity / len(seq)) * 100
    return round(n, 2)
