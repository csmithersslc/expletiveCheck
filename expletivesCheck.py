# This is a program that will read from a text file and determine if there are any expletives
#one solution uses an import of the urllib and the other which uses a list
import urllib

#If so, it will let the user know

#First open and read the file
def read_text():
	dogs = open ("C:\Users\Christina\Desktop\Udacity Full Stack ND\Python\swearFilter\dogsList.txt")
	contents_of_file = dogs.read()
	#print what the file says
	print(contents_of_file)
	#close the file when done
	dogs.close()
	check_expletive(contents_of_file)
	check_profanity(contents_of_file)

#Now it's time to look for profane language to avoid embarassing situations

#this is my solution
def check_expletive(contents_of_file):
#First here is a list of common expletives 

	words = {'shit', 'bitch', 'ass', 'cunt', 'dago'}

#now we must see if any of the text in the txt file match something in the list

	if "shit" in contents_of_file:
		print "Expletive detected!  Something that starts with 's'.  Better double-check..."

	elif "bitch" in contents_of_file:
		print "Expletive detected!  Something that starts with 'b'. Better double-check..."

	elif "ass" in contents_of_file:
		print "Expletive detected! Something that starts with 'a'. Better double-check..."

	elif "cunt" in contents_of_file:
		print "Expletive detected! Something that starts with 'c'. Better double-check..."

	elif "dago" in contents_of_file:
		print "Expletive detected! Something that starts with 'd'. Better double-check..."
	else:
		print "Looks good!  No bad words."


#this is the solution which uses an online detector
def check_profanity(text_to_check):
	#connect to the website to check a word
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" +text_to_check)
	output = connection.read()
	#this will print what the site says
	print(output)
	#closes the connection
	connection.close()

read_text()




