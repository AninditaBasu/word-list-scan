![license: GPL 3.0](https://img.shields.io/badge/license-GPL%203.0-lightgrey.svg)  ![python 3.7](https://img.shields.io/badge/python-3.7.0-blue.svg)

# word-list-scan

A script that scans all DITA files in a directory for occurrences of an entire list of words and phrases. Markup tags (without the angle brackets) are also reckoned as words.

## Usage scenario

You want to scan all files in a directory for several words, all at once. 

Maybe these words are a list of do-not-use words that your style guide specifies, but you don't have an automated word checker to look for such occurences. Maybe you want to know if you've used certain DITA tags in your files but do not want to run a system search for each tag, one by one. 

This script searches for multiple words at one go, and also phrases and DITA tags. You specify a list of words and phrases, and tell the script which directory it should scan. The script runs the checks and gives you a report that you can read and act upon.

## Documentation

See [Anin's Documentation Tools](https://doc-tools.readthedocs.io/en/latest/).
 
## Limitations

It is assumed that all DITA topic files have the `.dita` extension. If your files use the `.xml` extension, this script will not work in its present form.

## Acknowledgments

The code was converted from .py to .exe through [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe).

## Licensing

The script is under [GPL 3](https://opensource.org/licenses/GPL-3.0), which is a copyleft licence. You are free to use and distribute this code as-is. You are also free to modify and distribute this code provided you distribute such modified code in its entirety under the same licence as this one, that is GPL 3.
