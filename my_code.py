import os

from pkg_a.module_a import things_will_be_done_here


def do_things(data):
    return things_will_be_done_here(data)


def create_dir(path):
    os.makedirs(path, exist_ok=False)
