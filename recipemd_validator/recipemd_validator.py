import argparse
from typing import Optional, Sequence

from recipemd.data import RecipeParser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Checks that the provided list of *.md files have valid RecipeMD format."""

    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Markdown files to check.')
    args = parser.parse_args(argv)

    rp = RecipeParser()
    exit_code = 0

    for file in args.filenames:
        with open(file, 'r', encoding='UTF-8') as f:
            try:
                rp.parse(f.read())
            except Exception as exc:
                print(f'{file}: Invalid RecipeMD ({exc})')
                exit_code = 1

    return exit_code


if __name__ == '__main__':
    exit(main())
