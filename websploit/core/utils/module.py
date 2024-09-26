import re
import os
import importlib
import string
import random
import websploit.modules as wsf_module

MODULES_DIR = wsf_module.__path__[0]

def get_modules(modules_directory: str = MODULES_DIR) -> list:
    """
    Returns list of all exploits modules

    :param str modules_directory: path to modules directory
    :return list: list of found modules
    """

    modules = []
    for root, dirs, files in os.walk(modules_directory):
        _, package, root = root.rpartition("websploit/modules".replace("/", os.sep))
        root = root.replace(os.sep, ".")
        files = filter(lambda x: not x.startswith("__") and x.endswith(".py"), files)
        modules.extend(map(lambda x: ".".join((root, os.path.splitext(x)[0])), files))
    
    return modules

def import_exploit(path: str):
    """ 
    Imports exploit module

    :param str path: absolute path to exploit e.g. routersploit.modules.exploits.asus_auth_bypass
    :return: exploit module or error
    """

    try:
        module = importlib.import_module(path)
        if hasattr(module, "Main"):
            return getattr(module, "Main")
        else:
            raise ImportError("No module named '{}'".format(path))
    except (ImportError, AttributeError, KeyError) as err:
        print(Exception(err))

def iter_modules(modules_directory: str = MODULES_DIR) -> list:
    """ Iterates over valid modules

    :param str modules_directory: path to modules directory
    :return list: list of found modules
    """

    modules = index_modules(modules_directory)
    modules = map(lambda x: "".join(["websploit.modules.", x]), modules)
    for path in modules:
        yield import_exploit(path)

def pythonize_path(path: str) -> str:
    """ Replaces argument to valid python dotted notation.

    ex. foo/bar/baz -> foo.bar.baz

    :param str path: path to pythonize
    :return str: pythonized path
    """

    return path.replace("/", ".")


def humanize_path(path: str) -> str:
    """
    Replace python dotted path to directory-like one.

    ex. foo.bar.baz -> foo/bar/baz

    :param str path: path to humanize
    :return str: humanized path
    """

    return path.replace(".", "/")
