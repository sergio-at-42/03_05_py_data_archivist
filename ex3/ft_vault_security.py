#!/usr/bin/env python3


def secure_archive(file_name: str,
                   action: str = "r",
                   content: str = ""
                   ) -> tuple[bool, str]:
    op_ok: bool = False
    result: str = ""
    try:
        with open(file_name, action) as file:
            if action == "r":
                result = file.read()
                op_ok = True
            elif action == "w":
                file.write(content)
                result = "Content successfully written to file"
                op_ok = True
            else:
                result = "Only 'r' or 'w' actions are allowed"
                op_ok = False
    except Exception as e:
        result = f"{e}"
        op_ok = False
    return (op_ok, result)


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")
    print("Using ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))
    print("")
    print("Using ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive("/boot/efi", "r"))
    print("")
    print("Using ’secure_archive’ to read from a regular file:")
    print(secure_archive("../ancient_fragment.txt", "r"))
    print("")
    print("Using ’secure_archive’ to write previous content to a new file:")
    new_content = secure_archive("../ancient_fragment.txt", "r")[1]
    print(secure_archive("../new_file.txt", "w", new_content))
    print("")
    print("Using ’secure_archive’ with 'h' action:")
    print(secure_archive("../new_file.txt", "h"))
    print("")


if __name__ == "__main__":
    ft_vault_security()
