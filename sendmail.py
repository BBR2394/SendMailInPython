# -*- coding: utf-8 -*-
# @Author: Baptiste
# @Date:   2019-12-09 15:08:29
# @Last Modified by:   Baptiste Bertrand-Rapello
# @Last Modified time: 2019-12-09 15:36:05

#!/usr/local/bin/python3

import sys
import smtplib

from email.message import EmailMessage

def open_a_file_ronly(file_name):
	try:
		fd = open(file_name, 'r')
		print("-> The file is opened")
		return fd
	except  :
		print("=> an error occured when opening the file")
		return -1

def readContentToSend(fd):
	txt = fd.read()
	print("le text\n----------------------------------")
	print(txt)
	print("*-------------------------------*")
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

	for i in lst_mail:
		print("mail : ", i)

	return lst_mail

def getMailContentToSend(filename, emailListFileName):
	print("here i am going to open the file and read it ")
	fd = open_a_file_ronly(filename)
	content = readContentToSend(fd)
	listMail = getMailList(emailListFileName)


def main():
	print("in the main function, all the magic will come")
	getMailContentToSend("mail_content.txt", "email_list.txt")

	return 0

main()