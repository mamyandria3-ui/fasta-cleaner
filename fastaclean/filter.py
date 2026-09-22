#!/usr/bin/env python3


from fastaclean.metrics import n_content


def validate_sequence(sequence: str) -> bool:
    valid = "ATCGN"
    for c in sequence.upper():
        if c not in valid:
            return False
    return True


def min_length(sequence: str,  length: int) -> bool:
    len_seq = len(sequence)
    if len_seq < length:
        return False
    return True


def n_percent(sequence: str, max_n_percent: float) -> bool:
    n_percent = n_content(sequence)
    if n_percent > max_n_percent:
        return False
    return True


def filter_sequences(
        result_parse: dict[str, str],
        length: int,
        max_n_percent: float) -> tuple[dict[str, str], dict[str, int]]:

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
