__author__ = 'anindita basu'
import re
import os

fname = 'wordlist.txt'
wordlist = []
fwordlist = open(fname)
for word in fwordlist:
    word = word.rstrip()
    wordlist.append(word)
    print word
fwordlist.close()
print '==============list of words read=============='

x = len(wordlist)
print 'No. of words and phrases to search for: ', x

workspace = raw_input("Enter the directory to be scanned: ")

counter = 0
try:
    for foldername in os.listdir(workspace):
        counter += 1
        print foldername
except:
    print 'The directory could not be found'
    exit()
print 'The directory has ', counter, 'folders'

counter = 0
for (dirname, dirs, files) in os.walk(workspace):
    for filename in files:
        if filename.endswith('.dita'):
            counter = counter + 1
            #print filename
            thefile = os.path.join(dirname, filename)
            wcount = 0
            for word in wordlist:
                handle = open(thefile)
                for line in handle:
                    line = line.rstrip()
                    if re.search(word, line):
                        wcount += 1
            if wcount >= 1:
                print "In", thefile, word, 'occurs', wcount, 'times'
            wcount = 0
            handle.close()
print 'The directory has', counter, 'DITA files'

raw_input('==============finished printing word occurrences==============')

raw_input("press any key to close")
exit()
Enter file contents here
