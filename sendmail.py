# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-12-09 15:08:29
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2020-01-23 15:45:24

#!/usr/local/bin/python3

import sys
import smtplib
from email.message import EmailMessage
import smtplib

glb_subject = "a subject "
glb_sender = "sender@email.com"
glb_receiver = "receiver@email.com"

def open_a_file_ronly(file_name):
	try:
		fd = open(file_name, 'r')
		print("-> The file : " + file_name + " , is opened")
		return fd
	except  :
		print("=> an error occured when opening the file : " + file_name)
		return -1

def readContentToSend(fd):
	txt = fd.read()
	print("=>Text that is going to be send\n+----------------------------------+")
	print(txt)
	print("*----------------------------------*")
	return txt

def store_file_in_list(fd):
	lst = []
	line = fd.readline()
	entrynb = 1
	#print(":" + str(entrynb) + "> line juts to test " + str(line))
	while line != "":
		lst.append(int(line))
		line = fd.readline()
		entrynb += 1
		#print(":" + str(entrynb) + "> line juts to test " +  str(line))

	#print("-> the file is stored in memory")
	return lst

def mailListInList(fd):
	lst = []
	line = fd.readline()
	while line != "":
		mail = line.split(';')
		lst.append(mail[0])
		line = fd.readline()
	return lst

def getMailList(filename):
	fd_list = open_a_file_ronly(filename)
	lst_mail = mailListInList(fd_list)

	for i in range (len(lst_mail)):
		print("mail :", i,lst_mail[i])

	return lst_mail

def getMailContentToSend(filename, emailListFileName):
	email = EmailMessage()
	
	#server = smtplib.SMTP()
	#srv = smtplib.SMTP('localhost')

	print("here i am going to open the file and read it ")
	
	fd = open_a_file_ronly(filename)
	content = readContentToSend(fd)
	listMail = getMailList(emailListFileName)

	email.set_content(content)
	email['Subject'] = glb_subject
	email['From'] = glb_sender
	email['To'] = glb_receiver

	#server.send(email)
	#server.quit()


def main(av):
	print("in the main function, all the magic will come")
	#print("av : ", av, len(av))
	if len(av) < 3:
		print("Usage :\n\t$>./sendmail.py file_contentOfTheMail.txt file_AdressMailList.txt")
		return 1
	else :
		#getMailContentToSend("mail_content.txt", "email_list.txt")
		getMailContentToSend(av[1], av[2])
		return 0

#print(sys.argv)
main(sys.argv)