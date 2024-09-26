import os
from tabulate import tabulate
from websploit.core import base

class Main(base.Module):
    """SSH Brute Force"""

    parameters = {
        "host": "127.0.0.1",
        "port": "22",
        "username": "root",
        "password": "root",
        "userfile": "",
        "passfile": ""
    }
    completions = list(parameters.keys())

    def do_ls(self, line):
        data_dict = self.parser_module(self.get_cmd_path("fm.json"))
        table = [(command, description) for command, description in data_dict.items()]
        self.cp.green(tabulate(table, headers=["Command", "Description"], tablefmt="grid"))