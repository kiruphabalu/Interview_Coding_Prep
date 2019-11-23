
import os
import re

# Regex used to match relevant loglines (in this case, a specific IP address)
line_regex = re.compile(r".*fwd=\"12.34.56.78\".*$")

# Output file, where the matched loglines will be copied to
output_filename = os.path.normpath("output/parsed_lines.log")
# Overwrites the file, ensure we're starting out with a blank file
with open(output_filename, "w") as out_file:
    out_file.write("")

# Open output file in 'append' mode
with open(output_filename, "a") as out_file:
    # Open input file in 'read' mode
    with open("test_log.log", "r") as in_file:
        # Loop over each log line
        for line in in_file:
            # If log line matches our regex, print to console, and output file
            if (line_regex.search(line)):
                print line
                out_file.write(line)



# With class and functions
import re
import time
from time import strftime

def main():
    log_file_path = r"C:\ios logs\sfbios.log"
    export_file_path = r"C:\ios logs\filtered"

    time_now = str(strftime("%Y-%m-%d %H-%M-%S", time.localtime()))

    file = "\\" + "Parser Output " + time_now + ".txt"
    export_file = export_file_path + file

    regex = '(<property name="(.*?)">(.*?)<\/property>)'

    parseData(log_file_path, export_file, regex, read_line=True)



def parseData(log_file_path, export_file, regex, read_line=True):
    with open(log_file_path, "r") as file:
        match_list = []
        if read_line == True:
            for line in file:
                for match in re.finditer(regex, line, re.S):
                    match_text = match.group()
                    match_list.append(match_text)
                    print match_text
        else:
            data = file.read()
            for match in re.finditer(regex, data, re.S):
                match_text = match.group();
                match_list.append(match_text)
    file.close()

    with open(export_file, "w+") as file:
        file.write("EXPORTED DATA:\n")
        match_list_clean = list(set(match_list))
        for item in xrange(0, len(match_list_clean)):
            print match_list_clean[item]
            file.write(match_list_clean[item] + "\n")
    file.close()

if __name__ == '__main__':
    main()
