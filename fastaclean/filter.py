"""Sequence validation and quality filtering utilities.

Provides functions to validate nucleotide alphabet composition,
check sequence length constraints, evaluate ambiguous base thresholds,
and filter FASTA-style sequence dictionaries based on quality criteria.
"""


from fastaclean import n_content


def validate_sequence(sequence: str) -> bool:
    """Check if a nucleotide sequence contains only valid canonical bases.

    Args:
        sequence (str): Input nucleotide sequence to validate.

    Returns:
        bool: True if all characters in the sequence belong
        to the valid set ('A', 'T', 'C', 'G', 'N') after uppercase conversion;
        False otherwise.
    """
    valid = "ATCGN"
    for c in sequence.upper():
        if c not in valid:
            return False
    return True


def min_length(sequence: str, length: int) -> bool:
    """Verify whether a sequence meets a minimum length threshold.

    Args:
        sequence (str): Input nucleotide sequence.
        length (int): Minimum acceptable sequence length.

    Returns:
        bool: True if the sequence length is greater than
        or equal to the threshold; False otherwise.
    """
    len_seq = len(sequence)
    if len_seq < length:
        return False
    return True


def n_percent(sequence: str, max_n_percent: float) -> bool:
    """Check if the percentage of ambiguous bases is within the allowed limit.

    Args:
        sequence (str): Input nucleotide sequence.
        max_n_percent (float): Maximum permitted percentage of 'N' bases.

    Returns:
        bool: True if the calculated 'N' percentage is less than or equal to
        `max_n_percent`; False otherwise.
    """
    n_percent = n_content(sequence)
    if n_percent > max_n_percent:
        return False
    return True


def filter_sequences(
        result_parse: dict[str, str],
        length: int,
        max_n_percent: float) -> tuple[dict[str, str], dict[str, int]]:
    """Filter a collection of sequences.

    Based on validity, length, and N-content criteria.

    Args:
        result_parse (dict[str, str]): Dictionary mapping sequence
        headers to sequence strings.
        length (int): Minimum required sequence length.
        max_n_percent (float): Maximum allowed percentage of 'N' bases.

    Returns:
        tuple[dict[str, str], dict[str, int]]: A tuple containing:
            - dict[str, str]: Filtered dictionary containing only
            sequences that passed all checks.
            - dict[str, int]: Statistics summary containing counts
            for "initial_seq", "conserved_seq", and "rejected_seq".
    """
    result_filter: dict[str, str] = {}

    stats: dict[str, int] = {
        "initial_seq": 0,
        "conserved_seq": 0,
        "rejected_seq": 0
    }

    for header, sequence in result_parse.items():
        stats["initial_seq"] += 1

        is_valid_seq = validate_sequence(sequence)
        is_valid_len = min_length(sequence, length)
        is_valid_n_percent = n_percent(sequence, max_n_percent)

        if is_valid_seq and is_valid_len and is_valid_n_percent:
            result_filter[header] = sequence
            stats["conserved_seq"] += 1
        else:
            stats["rejected_seq"] += 1

    return result_filter, stats
