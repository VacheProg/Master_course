# bacel
# stugel
# avelacnel
# avelacnel sub circuit
# pntrel

import os
import sys

def add_sub_circuit(netlist_object, data):
    pass

def main():
    # Main logic
    pass


def get_pins_for_sub(sub):
    {"pin_name": "", "in":"", "out": }
def get_sub_circuits(file_content):
    subs = {}# key sub anun, value []
    ind = 0
    while ind < len(file_content):
        line = file_content[ind]
        if line.strip().startswith(".SUBCKT"):
            sub_data = []
            sub_name = line.split()[1]
            while (not line.strip().startswith(".END")) and (ind < len(file_content)):
                line = file_content[ind]
                sub_data.append(line)
                ind += 1
            subs[sub_name] = sub_data
        ind += 1
    return subs



def skip_comments(file_content, comment_sign="*"):
    """SKips the coment from file """
    new_content = []
    for line in file_content:
        if not line.strip().startswith(comment_sign):
            new_content.append(line)
    return new_content

skip_comments("asdas", comment_sign="#")

def netlist_parser(file_name) -> dict:
    """parses the netlist file"""
    if not os.path.isfile(file_name):
        print('wrong path')
        return {}
    with open(file_name) as f:
        file_content = f.readlines()
    #1 step remove comments
    file_content = skip_comments(file_content)
    #2 step
    subs = get_sub_circuits(file_content)
    print(subs)

# get args and pass to
netlist_parser("a.txt")