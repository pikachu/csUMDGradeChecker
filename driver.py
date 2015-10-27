userID = raw_input('username: ')
password = raw_input('password: ')
emailID = raw_input('email: ')
emailPass = raw_input('email password: ')
phoneNumber = raw_input('Phone number: ')

classIDS = []
numClasses = raw_input('How many classes would you like to keep updated with?: ')

for var in xrange(1, int(numClasses)+1):
	classIDS.append(raw_input("Class #" + str(var) + ": "))

classes = open('classes.txt','w')
userInfo = open('user.txt','w')
phoneEmail = str(phoneNumber)+'@txt.att.net'

for item in classIDS:
	classes.write("%s\n" % item)


userInfo.write(userID+" "+password+" "+emailID+" "+emailPass+" "+phoneEmail)

classes.close()
userInfo.close()

import checkCS
