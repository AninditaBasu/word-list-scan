#
#
# wordListScan.py
# Copyright (C) 2015  Anindita Basu
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/gpl-3.0.txt.
#
#
import re
import os
#
# Open a file called "wordListScan.html" to write the findings to.
#
reportfile = open("wordListScan.html", "w")
reportfile.write("<html>")
reportfile.write("<head>")
reportfile.write("<title>Search report</title>")
reportfile.write("<style>h1{color:#A52A2A;}")
reportfile.write('p{font-family:"Trebuchet MS", Arial, Verdana, serif; font-size:16px;line-height:120%;}')
reportfile.write('li{font-family:"Trebuchet MS", Arial, Verdana, serif; font-size:16px;line-height:200%;}')
reportfile.write('</style>')
reportfile.write("</head>")
reportfile.write("<body>")
reportfile.write("<h1>Search report</h1>")
#
fname = 'wordlist.txt'
#
# The name of the word list file is hardcoded. Users can change the contents of file.
#
wordlist = []
#
# Define a list to write the list of words in the wordlist.txt file to.
#
print ("\n")
print ('Reading the word list ...\n')
reportfile.write("<p>Words and phrases searched for:</p>")
reportfile.write("<ul>")
#
fwordlist = open(fname, 'r')
for word in fwordlist:
    word = word.rstrip()
    wordlist.append(word)
    reportfile.write('<li>')
    reportfile.write(word)
    reportfile.write('</li>')
    print (word)
fwordlist.close()
reportfile.write("</ul>")
print (wordlist) #checking
#
# Count the number of words in the list and display the count.
#
x = len(wordlist)
print ('\nNo. of words and phrases to search for: ', x)
reportfile.write("<p>Number of search terms: ")
a = str(x)
reportfile.write(a)
reportfile.write("</p>")
#
# Get the directory that contains the DITA files.
# Print it to the report file.
#
print ("\nSpecify the full path of the directory to be scanned, for example, C:\jazz_repo\prodA\\\n")
print ("Do not forget the trailing slash\n")
#
workspace = input("Enter the full path of directory to be scanned: ")
#
reportfile.write('<p>Directory scanned: <a href = "file:///')
reportfile.write(workspace)
reportfile.write('" target = "_blank">')
reportfile.write(workspace)
reportfile.write("</a></p>")
reportfile.write("<hr/>")
#
# start a counter for the number of subfolders in the directory
#
counter = 0
#
# Print out the subfolders. Also, count them and print out the count.
#
print ('\nReading the directory ...\n')
#
try:
    for foldername in os.listdir(workspace):
        counter += 1
        print (foldername)
except:
    print ('The directory could not be found.\n')
    exit()
print ('\nThe program will scan ', counter, 'folders in the', workspace, 'directory.\n')
#
# Start a counter for the number of dita files in the directory
#
# If file is a dita file, create the full file path. Then, pick up the wordlist.
# For each word in the list, open the file, search for occurrence, add to wordcounter if found,
# print the filename only if searched word exists in the file, and then close the file.
#
counter = 0  # to count the number of files in all of the subfolders.
filelist = []
for (dirname, dirs, files) in os.walk(workspace):
    for filename in files:
        if filename.endswith('.dita'):
            counter = counter + 1
            thefile = os.path.join(dirname, filename)
            filelist.append(thefile)
#
for word in wordlist:
    print (word)
    reportfile.write('<p><span style="color:red">')
    reportfile.write(word)
    reportfile.write("</span>")
    reportfile.write(" occurs in:</p>")
    reportfile.write("<ul>")
    for thefile in filelist:
        handle = open(thefile, 'r', encoding='ISO-8859-2')
        filecontents = handle.read()
        if word in filecontents:
            print (word, 'occurs in', thefile)
            reportfile.write("<li>")
            reportfile.write(thefile)
            reportfile.write("</li>")
        handle.close()
    reportfile.write("</ul><hr/>")
print ('\nFinished checking', counter, 'DITA files.\n')
reportfile.write("<p>Finished checking ")
a = str(counter)
reportfile.write(a)
reportfile.write(" DITA files.</p>")
#
# print a completion message
#
print ('==============finished printing word occurrences==============\n')
#
#
# Write the closing HTML tags in the report file.
#
reportfile.write("</body>")
reportfile.write("</html>")
reportfile.close()
#
# Wait for user input so that a person gets enough time to read whatever's been printed on the console
# and then close the program
#
print ("The program will now end.")
input("Press any key to close.")
exit()
