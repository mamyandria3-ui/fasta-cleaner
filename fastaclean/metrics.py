#!/usr/bin/env python3


def clean_sequence(sequence: str) -> str:
    if not sequence:
        return ""
    seq = sequence.replace(" ","").replace("\n", "").replace("\r","").upper()
    return seq

def len_sequence(sequence: str) -> int:
    seq = clean_sequence(sequence)
    return len(seq)

def gc_content(sequence: str) -> float:
    seq = clean_sequence(sequence)
    if not seq:
        return 0.0
    gc_quantity = seq.count('C') + seq.count('G')
    gc = (gc_quantity / len(seq)) * 100
    return round(gc, 2)

def n_content(sequence: str) -> float:
    seq = clean_sequence(sequence)
    if not seq:
        return 0.0
    n_quantity = seq.count('N')
    n = (n_quantity / len(seq)) * 100
    return round(n, 2)
