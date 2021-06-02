#Author Dominic Gantert
#domgantert@gmail.com
#
# This app will take fileA and remove any row where the first column has a value
# that exists in fileB then output the rows that pass the condition into a third
# file. It will also print the rows to stdout using print()..
#
#Args;
#1- fileA A comma delimitered file with two columns(id, value)
#2- fileB A file containing ids with one id per row.
#3- The name of the output file including the extension
#
#Usage
#python app.py fileA.csv fileB fileC.csv
#
#
#Notes
#This solution is system and filename agnostic when compared to iterating over sys.stdin
#for line in sys.stdin:
#    sys.stdout.write(line)
#
import sys

input_filename = sys.argv[1]
exceptions_filename = sys.argv[2]
output_filename = sys.argv[3]

# For us in Ipython notebooks
# input_filename = 'fileA.csv'
# exceptions_filename = 'fileB'
# output_filename = 'fileC.csv'


#FileB is fully loaded into memory given it is only 10,000 lines.
with open(exceptions_filename) as fileB:
    contentB = fileB.read()
    listB = contentB.split('\n')
    #Any duplicates in fileB are removed to increase efficiency in the next step.
    listB = list(set(listB))


#FileA is loaded into memory one line at a time.
fileA = open(input_filename, 'r')
with open(output_filename, 'w') as fileC:

    while fileA:
        line = fileA.readline()
        listA = line.split(',')

        if listA[0] not in listB:
            fileC.writelines((line))
            print((line))

        if line == "":
            break

fileA.close()

