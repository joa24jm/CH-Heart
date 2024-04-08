# Author Johannes Allgaier

# imports
from pathlib import Path

def get_project_root() -> Path:
    return Path(__file__).parent.parent

def main():
    root = get_project_root()
    print(root)


if __name__ == '__main__':
    main()
