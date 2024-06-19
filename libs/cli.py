"""
Contains the logic for the CLI interface
"""

import argparse
import sys
from .version import cmd_version
import os

argparser = argparse.ArgumentParser(description="The stupidest content tracker", exit_on_error=False)
argsubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsubparsers.required = True
argsp = argsubparsers.add_parser("version", help="Prints version info")


def main(argv=sys.argv[1:]) -> None:
    """
    The logic for the CLI interface
    """
    args: argparse.Namespace = argparser.parse_args(argv)
    match args.command:
        case "add":
            cmd_add(args)
        case "cat-file":
            cmd_cat_file(args)
        case "check-ignore":
            cmd_check_ignore(args)
        case "checkout":
            cmd_checkout(args)
        case "commit":
            cmd_commit(args)
        case "hash-object":
            cmd_hash_object(args)
        case "init":
            cmd_init(args)
        case "log":
            cmd_log(args)
        case "ls-files":
            cmd_ls_files(args)
        case "ls-tree":
            cmd_ls_tree(args)
        case "rev-parse":
            cmd_rev_parse(args)
        case "rm":
            cmd_rm(args)
        case "show-ref":
            cmd_show_ref(args)
        case "status":
            cmd_status(args)
        case "tag":
            cmd_tag(args)
        case "version":
            cmd_version(args)
        case _:
            print("Bad command.")