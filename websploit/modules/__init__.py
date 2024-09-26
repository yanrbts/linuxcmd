import os
import pkgutil
from websploit.core.utils import CPrint
from websploit.core.utils.module import get_modules, import_exploit, humanize_path
cp = CPrint()

# __all__ = list(module for _, module, _ in pkgutil.iter_modules([os.path.dirname(__file__)]))


def all_modules():
    """print available modules in nice way"""
    cp.green(f"{'Modules':<20}\t{'Description':<20}")
    cp.green(f"{'--'*10}\t{'--'*13}")
    for module in get_modules():
        try:
            # current_module = globals()[module].Main()
            module = module[1:]
            current_module = import_exploit("websploit.modules.{}".format(module))()
            cp.yellow(f"{humanize_path(module):<20}\t{current_module.__doc__}")
        except AttributeError:
            print(f"*** Module `{module}` not has `Main` class!")
    print("\n")


def module_list():
    modules = []
    for module in get_modules():
        try:
            module = module[1:]
            modules.append(humanize_path(module))
        except AttributeError:
            print(f"*** Module `{module}` not has `Main` class!")

    return modules
