"""FASTA parsing module.

Provides utility functions to read and
parse FASTA format files into structured Python dictionaries.
"""


from pathlib import Path


def parse_fasta(file_path: str) -> dict[str, str]:
    """Read a FASTA file and extracts header-sequence pairs into a dictionary.

    Args:
        file_path (Union[str, Path]): Path to the input FASTA file.

    Returns:
        Dict[str, str]: A dictionary mapping header labels (keys) to
            their corresponding raw nucleotide sequences (values).

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError("FASTA file not found.")

    result: dict[str, str] = {}

    with path.open("r", encoding="utf-8") as file:
        current_header: str = ""
        current_sequence: list[str] = []

        for line in file:
            stripped_line = line.strip()
            if not stripped_line:
                continue

            if stripped_line.startswith('>'):
                if current_header:
                    result[current_header] = "".join(current_sequence)
                current_header = stripped_line[1:].strip()
                current_sequence = []
            else:
                current_sequence.append(stripped_line)

        if current_header:
            result[current_header] = "".join(current_sequence)

    return result
