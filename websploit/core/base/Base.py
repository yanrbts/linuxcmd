import cmd
import sys
from websploit.modules import all_modules, module_list
from websploit.core.utils import CPrint
import json, os

class Module(cmd.Cmd):
    parameters = {}
    cp = CPrint()


    def do_execute(self):
        """Execute current module"""
        pass

    def do_back(self, *args):
        """go back one level"""
        return True

    def do_exit(self, line):
        """exit websploit"""
        sys.exit(0)

    def do_set(self, line):
        """set options"""
        try:
            key, value = line.split(' ')
            print(key, value)
            self.parameters.update({key: value})
        except KeyError:
            # print(f"*** Unknown Option! option not has value!")
            self.cp.warning(text="*** Unknown Option! option not has value!")
        except ValueError:
            # print(f"*** Option not has value!")
            # print(f"*** Example : set host 127.0.0.1")
            self.cp.warning(text="*** Option not has value!")
            self.cp.info(text="*** Example : set host 127.0.0.1")

    def do_options(self, line):
        """Show options of current module"""
        print("\n")
        self.cp.green(f"{'Option':20}\t{'Value':20}")
        self.cp.green(f"{'--'*8:<20}\t{'--'*8:<20}")
        for k,v in self.parameters.items():
            self.cp.yellow(f"{k:20}\t{v:<20}")
        print("\n")

    def complete_set(self, text, line, begidx, endidx):
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




