from pathlib import Path


def l_14_Path():
    file_path = Path("test.txt")
    print([m for m in dir(file_path) if not m.startswith("_")])

    # current dir
    current_dir = Path.cwd()
    print(f"current_dir: {current_dir}")

    # create path
    new_path = Path("usr").joinpath("local", "bin")
    print(f"new_path: {new_path}")

    # check if path exists
    if not new_path.exists():
        print(f"Path {new_path} does not exist, creating it.")
        new_path.mkdir(parents=True, exist_ok=True)
    else:
        print(f"Path {new_path} already exists.")

    # check if path is a file or directory
    if new_path.is_file():
        print(f"{new_path} is a file.")
    elif new_path.is_dir():
        print(f"{new_path} is a directory.")
    else:
        print(f"{new_path} is neither a file nor a directory.")

    # iterate over files in a directory
    for item in current_dir.iterdir():
        if item.is_file():
            print(f"File: {item.name}")
        elif item.is_dir():
            print(f"Directory: {item.name}")

    # resolve path
    resolved_path = new_path.resolve()
    print(f"resolved_path: {resolved_path}")

    # delete file or directory
    if new_path.exists():
        print(f"Deleting path: {new_path}")
        new_path.rmdir()  # Use rmdir for directories, unlink for files
    else:
        print(f"Path {new_path} does not exist, nothing to delete.")
