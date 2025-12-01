from pathlib import Path
import shutil
import sys

# Recursive function to copy files from source to destination, sorted by extension
def copy_and_sort_files(source_dir: Path, dest_dir: Path):
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest_dir)  # If item is a directory, recursively process it
            else:
                extension = item.suffix[1:].lower() if item.suffix else "no_extension"
                target_dir = dest_dir / extension # Create target directory path based on file extension
                try:
                    target_dir.mkdir(parents=True, exist_ok=True) # Create extension subdirectory if it doesn't exist
                    shutil.copy2(item, target_dir / item.name)  # Copy file preserving metadata to the target directory
                    print(f"Copied: {item} -> {target_dir / item.name}")
                except PermissionError:
                    print(f"Error: No permission to copy {item}")
    except PermissionError:
        print(f"Error: No permission to access {source_dir}")


def main():
    if len(sys.argv) < 2: #if source directory argument is provided
        print("Usage: python task_01.py <source> [destination]")
        sys.exit(1)

    source = Path(sys.argv[1])
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source.exists() or not source.is_dir():
        print(f"Error: '{source}' is not a valid directory")
        sys.exit(1)

    # Create output directory if it doesn't exist
    output.mkdir(parents=True, exist_ok=True)
    # Start the recursive copy and sort process
    copy_and_sort_files(source, output)
    print("Done!")

if __name__ == "__main__":
    main()
