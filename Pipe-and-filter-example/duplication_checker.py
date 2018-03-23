from filters import *

DIR_PATH = './sample_texts/'

def main():
    # Source (files in the current directory)
    source = os.listdir(DIR_PATH)

    # the files are filtered by extension and piped to next filter
    stream1 = filter_files(source, extension=".txt")

    # their data is read and piped to next filter
    stream2 = read_files(stream1, dir_path = DIR_PATH)

    # md5 hash for their content is calculated and piped
    stream3 = hash_files(stream2)
    
    # files with similiar hashes are categorized together and piped
    stream4 = frequency_filter(stream3)

    # only duplicated files and their content gets piped to next filter
    stream5 = duplicate_files_filter(stream4)

    # a report is generated (sink)
    show_report(stream5)

if __name__ == '__main__':
    main()