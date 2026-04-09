#!/usr/bin/env python3

import sys
from typing import IO


def ft_ancient_text(argv: list[str]) -> None:
    if len(argv) == 1:
        print(f"Usage: {argv[0].rpartition("/")[2]} <file>")
    else:
        print("=== Cyber Archives Recovery ===")
        try:
            print(f"Accessing file '{argv[1]}'")
            archive_file: IO = open(argv[1])
            print("---\n")
            print(archive_file.read())
            print("\n---")
            archive_file.close()
            print(f"File '{argv[1]} closed.'")
        except Exception as e:
            print(f"Error opening file '{argv[1]}': {e}")
    print("")


if __name__ == "__main__":
    ft_ancient_text(sys.argv)
