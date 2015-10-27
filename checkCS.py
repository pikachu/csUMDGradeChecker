#importing everything
from twill.commands import *
import smtplib
from bs4 import BeautifulSoup

#openng the text file with all the user info and putting it
#into an array
userInfo = open('user.txt','r')
info = userInfo.read().split(' ')

#go to the first page and submite everything
go('https://grades.cs.umd.edu/classWeb/login.cgi')
fv("1", "user", info[0])
fv("1", "password", info[1])
fv("1", "submit", "login")
submit('0')

#use beautiful soup to get the first couple pieces of info
soup = BeautifulSoup(show(), 'html.parser')
linkArr = soup.find_all('a')
numberOfClasses = len(linkArr) - 7

#create the dictionary holding the links
classes = dict()
for var in linkArr[-numberOfClasses:]:
	classes[var.get_text().split(' ')[0][4:]]=(var.get('href'))
#class[132]=link to get to that page, for example

#now to open the classes the user actually wants to keep track of
#classIDS stores the arrays of all the files you care about
with open('classes.txt') as my_file:
	classIDS = my_file.readlines()

#this is the array to store the grades from the website
allGrades = []


for classNumber in classIDS:
	#this just removes the \n character
	go(classes[classNumber.split('\n')[0]])
	#gets the grade
	soup2 = BeautifulSoup(show(), 'html.parser')
	grade = soup2.find_all('tr')[-1].get_text()[5:][:6]
	allGrades.append(grade)
	#goes back
	back()

#getting old grades and making the file writable
old = open('old.txt','r')
oldGrade = old.read()
old.close()
#making the format of the grade arrays the same
oldGradeArr = oldGrade.split(' ')

#checking if there is a difference
count = 0;
for num in allGrades:
	#if there is a difference in grades
	if (num != oldGradeArr[count]):
		oldGradeToSend = oldGradeArr[count]
		print("Sending message")
		server = smtplib.SMTP( "smtp.gmail.com", 25 )
		server.starttls()
		server.login( info[2], info[3] )
		server.sendmail( info[2], info[4], 'Your CS grades have changed!')
		newString = ''
		oldWriteable = open('old.txt','w')
		for eachGrade in allGrades:
			newString = newString + eachGrade + " "
		oldWriteable.write(newString)
		break
	else:
		print('no difference in grade yet.')
		count = count + 1;