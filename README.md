# csUMDGradeChecker
<h4>
Texts you when your CS grades change!
</h4>

Basically, the CS department at UMD did not notify you when your grades changed, and so I wrote a program to check for me. When
it detects a difference, it texts me to let me know.

Used python with the bs4 (parsing html) and twill (web navigation) libraries.

Still getting it automated on a web server with crontab, but this is proving to be slightly annoying.

<h5>Disclaimer: </h5> Only works with att with these files. You have to go into the
checkCS.py file and change the @att.txt.com extension to whatever your provider is.
