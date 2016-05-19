# word-list-scan

A script that scans all DITA files in a directory for occurrences of an entire list of words and phrases. Markup tags are also reckoned as words.

## Prerequisite

Download and install Python 2.7.5. Later versions of Python should also work.

## Steps

1. Download this repository as a `.zip` file and extract the contents to any directory.
2. Open the `wordlist.txt` file in a notepad. It contains some example words. Delete them, and enter the words and phrases to be searched for. Each word or phrase should be on a new line. Do not enter a new line after the last item in this file. Save the file and close it.
3. Double-click `wordListScan.py`. When prompted, enter the full path of the directory to be scanned, for example, `c:\documentation\myProduct\`. Do not forget to enter the trailing `\` for the directory. The script will scan all of the subfolders of the specified directory.
4. When the checking is complete, you see a message on the console: `Press any key to exit.` Press any key.
5. Go to the directory where the script resides. You see a file called `wordListScan.html`. This is the report file for you to read and act upon.
 
## Limitations

It is assumed that all DITA topic files have the `.dita` extension. If your files use the `.xml` extension, this script will not work in its present form.

## Bugs and enhancements

Use GitHub's issue tracking feature.

## Licensing

The script is under [GPL 3](https://opensource.org/licenses/GPL-3.0), which is a copyleft licence. You are free to use and distribute this code as-is. You are also free to modify and distribute this code provided you distribute such modified code in its entirety under the same licence as this one, that is GPL 3.
