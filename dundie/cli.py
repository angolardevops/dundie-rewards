import argparse

from .core import load


def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Reawards CLI",
        epilog="Use this tool to manage rewards points for Dunder Mifflin employees.",
    )
    parser.add_argument(
        "subcommand",
        choices=["add", "load", "show", "send"],
        help="Command to execute",
        default='help'
    )
    parser.add_argument(
        "filepath", type=str, help="Path to the data file", default=None
    )
    # parser.add_argument("--to", type=str, help="Recipient of the points")
    # parser.add_argument("--point", type=int, help="Points to award")
    args = parser.parse_args()

    print(*globals()[args.subcommand](args.filepath))
