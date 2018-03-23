#File Duplication Analyzer


    ##Description
        A simple program that reads files from a specified directory and reveal what documents are duplicated

    ## Developed by
        **Tibebeselasie Mehari**  -  **ATR/9941/08**  -  **S.E** (Regular, Section 2)

    ## Implementation details
        It uses "**Pipe and Filter** Architecture":
            +`source`  - the list of files
            +`filter1` - filters them by their extension
            +`filter2` - hashes their content (md5 hash)
            +`filter3` - frequency counter (based on thier hash)
            +`filter4` - filters duplicated files
            +`filter5`(sink) - generates a report

    ## Environment
        Python 3.x (Cross - platform)

    ## 3rd party Dependencies
        None (only built-in packages like os & hashlib are used)


    ## Usage
        `python duplication_checker.py <path> > <report_filename>`

        "`./sample_texts`" is the default path if no path is given through command line arguments

    ## How to Run
        + open up your terminal
        + cd to the dir containing the script
        + enter
            `python duplication_checker.py <path> > <report_filename>`

        Example:
            `python duplication_checker.py 'c:/' > report.txt`
