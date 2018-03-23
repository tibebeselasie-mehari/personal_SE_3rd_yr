import os, hashlib
from functools import reduce

from print_funcs import *

def read_files(filenames, dir_path, encoding="utf-8"):
    ''' Generator that yields data from filenames as (filename, data) tuple '''    
    for filename in filenames:
        yield filename, open("/".join([dir_path,filename]), 'r', encoding="utf-8").read()

def hash_files(inputs):
    ''' Generator that hashes the content of each files in its inputs '''
    for filename, data in inputs:
        yield filename, data, hashlib.md5(data.encode("utf-8")).hexdigest()

def frequency_filter(inputs):
    ''' a filter that packs filenames that contain the same hash as together and pipe it to the next filter '''

    frequency_table = {}

    for filename, data, hash in inputs:
        try:
            frequency_table[hash]['files'] += [filename]
        except KeyError:
            frequency_table[hash] = {
                'content' : data,
                'files' : [filename]
            }

    return frequency_table

def duplicate_files_filter(inputs):
    ''' Generator that yields filenames that contains the same hash as one '''

    for hash, data in inputs.items():
        if len(data['files']) > 1:
            yield list(data.values())

def filter_files(inputs, extension = ""):
    ''' Filter inputs stream according to a pattern '''
    for item in inputs:
        if item.endswith(extension):
            yield item

def show_report(inputs):
    inputs = list(inputs)

    print_header()
    
    totals_counter = reduce(lambda x, y: len(list(x)[1]) + len(list(y)[1]), inputs)
    
    print_underlined("Overall summary:", indentation=1)

    print_indented("<{:.>4}> file contents".format(len(inputs)), indentation = 2)
    print_indented("<{:.>4}> files are found to be duplicate.".format(totals_counter), indentation = 2, end="\n\n")

    print_underlined("Detailed Results:", end="\n", indentation=1)

    for content, files in inputs:
        print_indented("[+] Content : '", content[:50], end=" ... '\n", indentation = 2)
        print_indented("[+] <%d> files share the above content: "%(len(list(files))), indentation = 2)
        for each_file in files:
            print_indented("\t [+] %s"%each_file, indentation = 3)
        print_line(50, symbol = "-", indentation = 3, top="\n", bottom = "\n")


