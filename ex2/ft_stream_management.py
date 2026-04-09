#!/usr/bin/env python3

import sys
from typing import IO


def file_error_msg(e: Exception, file_name: str) -> str:
    return (f"[STDERR] Error opening file '{file_name}': {e}\n")


def ft_stream_management(argv: list[str]) -> None:
    if len(argv) == 1:
        print(f"Usage: {argv[0].rpartition("/")[2]} <file>")
    else:
        print("=== Cyber Archives Recovery & Preservation ===")
        try:
            print(f"Accessing file '{argv[1]}'")
            archive_file: IO = open(argv[1])
            print("---\n")
            enrg_archive_file: str = archive_file.read()
            print(enrg_archive_file)
            print("\n---")
            archive_file.close()
            print(f"File '{argv[1]}' closed.")
            print("")
        except Exception as e:
            sys.stderr.write(file_error_msg(e, argv[1]))
        else:
            enrg_new_file: str = enrg_archive_file.replace("\n", "#\n") + "#"
            print("Transform data:")
            print("---\n")
            print(enrg_new_file)
            print("\n---")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            new_file_name: str = sys.stdin.readline().strip()
            sys.stdout.write("\n")
            if not new_file_name:
                print("Not saving data.")
            else:
                print(f"Saving data to '{new_file_name}'")
                try:
                    new_file: IO = open(new_file_name, "w")
                    new_file.write(enrg_new_file)
                    new_file.close()
                    print(f"Data saved in file ’{new_file_name}'.")
                except Exception as e:
                    sys.stderr.write(file_error_msg(e, new_file_name))
                    sys.stderr.flush()
                    print(f"Data not saved.")
    print("")


if __name__ == "__main__":
    ft_stream_management(sys.argv)
