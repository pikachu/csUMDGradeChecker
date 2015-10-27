# csUMDGradeChecker
<h4>
Texts you when your CS grades change!
</h4>

Basically, the CS department at UMD did not notify you when your grades changed, and so I wrote a program to check for me. When
it detects a difference, it texts me to let me know.

Used python with the bs4 (parsing html) and twill (web navigation) libraries.

Still getting it automated on a web server with crontab, but this is proving to be slightly annoying.

<h3>driver.py</h3>
When someone runs this file, it asks for their username and password to the UMD
CS grade server, how many courses they are taking, and course codes (CMSC132 
becomes 132). This information is saved in user.txt (obviously not on here) and
classes.txt.

<h3>checkCS.py</h3>
This goes through the html of the grades.cs.umd.edu page and logs you in with
twill. Beautiful Soup then looks for the grades part, and then finds the links
of every single class you inputted in the driver. It stores your grades in the
old.txt file, and then compares the current grades to that file. If there is a
difference, it updates the old.txt and sends you a text message.

<h5>Disclaimer: </h5> Only works with att with these files. You have to go into the
checkCS.py file and change the @att.txt.com extension to whatever your provider is.
