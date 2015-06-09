# word-list-scan
A script that scans all DITA files in a directory, recursively, for occurences of an entire list of words and phrases.

To run the script, you need Python 2.7.5. Download and install Python from www.python.org.

Usage instructions
1. Download the script to any folder on your computer.
2. Open the wordlist.txt file in Notepad and enter the words and phrases to be searched for. Each word or phrase should be on a new line. Do not enter a new line after the last item in this file. Save and close the file.
3. Double-click the script. When prompted, enter the full path of the directory to be scanned, for example, c:\documentation\. Do not forget to enter teh trailing \ for the directory.
4. When the checking is complete, you see a message on the console: "Press any key to exit." Press any key.
5. Go to the folder where you saved the script. You see a file called .... This is the report file for you to read and act upon.
 
Limitations
The script assumes that all DITA topic files have the .dita extension. If your files use the .xml files, this script will not work.
