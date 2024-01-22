def copy_file(command: str) -> None:
    _, source_file, copied_file = command.split()

    if source_file != copied_file:
        with (
            open(source_file) as read_file,
            open(copied_file, "w") as write_file,
        ):
            write_file.write(read_file.read())


if __name__ == "__main__":
    copy_file("cp test.txt new_test.txt")
