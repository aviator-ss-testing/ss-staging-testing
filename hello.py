"""A simple greeting script.

This module provides a basic greeting functionality that can be customized
via command-line arguments.
"""

import argparse


def greet(name="World"):
    """Generate a greeting message.

    Args:
        name (str, optional): The name to greet. Defaults to "World".

    Returns:
        str: A greeting message in the format "Hello, {name}!"
    """
    return f"Hello, {name}!"


def main():
    """Main function to handle command-line argument parsing and execution."""
    parser = argparse.ArgumentParser(description="A simple greeting script.")
    parser.add_argument(
        "--name",
        type=str,
        default="World",
        help="Name to greet (default: World)"
    )

    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
