"""FASTA clean package for genomic sequence filtering and processing.

Provides utilities for parsing FASTA files, cleaning nucleotide sequences,
calculating quality metrics (GC content, N content),
and filtering sequences based on defined thresholds.
"""

from fastaclean.metrics import (
    clean_sequence,
    gc_content,
    len_sequence,
    n_content,
)
from fastaclean.filter import (
    filter_sequences,
    min_length,
    n_percent,
    validate_sequence,
)

from fastaclean.parser import parse_fasta

__all__ = [
    # Parser
    "parse_fasta",
    # Metrics
    "clean_sequence",
    "len_sequence",
    "gc_content",
    "n_content",
    # Filtering
    "validate_sequence",
    "min_length",
    "n_percent",
    "filter_sequences",
]
