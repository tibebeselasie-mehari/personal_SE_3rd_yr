TOTAL_WIDTH = 100

def print_line(length = TOTAL_WIDTH, symbol = "=", indentation = 0, top = "", bottom = ""):
    print(top, end="")
    print_indented(symbol * length, indentation=indentation)
    print(bottom, end="")

def print_indented(*args, indentation=1, **kwargs):
    print("\t" * indentation, *args, **kwargs)

def print_underlined(text, indentation=0, symbol = "=", end=""):
    print("\t"*indentation, text)
    print("\t"*indentation, symbol * len(text), end="\n"+end)

def print_header():
    print()
    print_line(TOTAL_WIDTH)
    print((" {:#^%d}"%TOTAL_WIDTH).format(" File Duplication Detector (FDD) - REPORT "))
    print_line(TOTAL_WIDTH)
    print()
