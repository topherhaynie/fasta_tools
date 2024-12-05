"""Module to read a fasta file."""

from pathlib import Path


def read_fasta(_input_path: Path) -> list[tuple[str, str]]:
    """Helper to read a fasta file.

    Args:
        _input_path (Path): The input Path.

    Returns:
        sequences: (list( (sequence_name (str), sequence (str) ) )): generates a list of identifier, sequence pairs.

    """
    sequences = []
    with _input_path.open() as f:
        lines = f.readlines()
        seq = ""
        identifier = ""
        for line in lines:
            if line.strip().startswith(">"):
                if identifier and seq:
                    sequences.append((identifier, seq))
                identifier = line.strip().lstrip(">")
                seq = ""
                continue
            seq += line.strip()
        if identifier and seq:
            sequences.append((identifier, seq))
    return sequences
