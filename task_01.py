from pathlib import Path
import shutil
import sys

def copy_and_sort_files(source_dir: Path, dest_dir: Path):
    try:
        for item in source_dir.iterdir():
            if item.is_dir():
                copy_and_sort_files(item, dest_dir)  # If item is a directory, recursively process it
            else:
                extension = item.suffix[1:].lower() if item.suffix else "no_extension" # Collect info in correct format
                target_dir = dest_dir / extension # Create target directory path based on file extension
                try:
                    target_dir.mkdir(parents=True, exist_ok=True) # Create extension subdirectory if it doesn't exist
                    shutil.copy2(item, target_dir / item.name)  # Copy file to the target directory
                    print(f"Copied: {item} -> {target_dir / item.name}") # Provide info about action to user
                except PermissionError: # Handle errors
                    print(f"Error: No permission to copy {item}")
    except PermissionError:
        print(f"Error: No permission to access {source_dir}")


def main():
    if len(sys.argv) < 2: # if source is provided
        print("Usage: python task_01.py <source> [destination]")
        sys.exit(1)

    source = Path(sys.argv[1])
    output = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("dist")

    if not source.exists() or not source.is_dir(): # Handle errors
        print(f"Error: '{source}' is not a valid directory")
        sys.exit(1)

    output.mkdir(parents=True, exist_ok=True) # Create output directory if it doesn't exist
    copy_and_sort_files(source, output)
    print("Done!")

if __name__ == "__main__":
    main()
