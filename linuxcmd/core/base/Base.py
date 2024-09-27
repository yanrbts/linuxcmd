import cmd
import sys
from linuxcmd.modules import all_modules, module_list
from linuxcmd.core.utils import CPrint
import json, os
import subprocess
from tabulate import tabulate

class Module(cmd.Cmd):
    parameters = {}
    data_dict = {}
    completions = []
    cp = CPrint()

    def do_back(self, *args):
        """go back one level"""
        return True

    def do_exit(self, line):
        """exit linuxcmd"""
        sys.exit(0)

    def do_info(self, line):
        """View command help"""

        try:
            result = subprocess.run([line, "--help"], capture_output=True, text=True)

            if result.returncode == 0:
                print("\n")
                self.cp.green(result.stdout)
            else:
                self.cp.error(text=result.stderr)
        except Exception as e:
            self.cp.error(text="*** Unknown Option! option not has value!")
    
    def do_list(self, line):
        """List all commands for this module"""

        self.data_dict = self.parser_module(self.get_cmd_path(self.parameters["filename"]))
        self.completions = list(self.data_dict.keys())
        table = [(command, description) for command, description in self.data_dict.items()]
        self.cp.green(tabulate(table, headers=["Command", "Description"], tablefmt="fancy_grid"))

    def complete_info(self, text, line, begidx, endidx):
        mline = line.partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in self.completions if s.startswith(mline)]

    def parser_module(self, file: str) -> dict:
        with open(file, 'r', encoding='utf-8') as f:
            data_dict = json.load(f)
        return data_dict
    
    def get_cmd_path(self, filename: str) -> str:
        from pathlib import Path
        package_path = Path(__file__).parent.parent.parent

        current_directory = os.path.dirname(__file__)
        parent_directory = os.path.dirname(current_directory)
        sibling_directory = os.path.join(parent_directory, package_path / 'cmds')
        cmd_path = os.path.join(sibling_directory, filename)
        return cmd_path




