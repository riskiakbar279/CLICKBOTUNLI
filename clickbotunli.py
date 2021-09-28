#bin/python
#edited riskiakbar279
import asyncio
import logging
import re
import time
import os
import sys
import requests

logging.basicConfig(level=logging.ERROR)

from telethon.tl.types import UpdateShortMessage,ReplyInlineMarkup,KeyboardButtonUrl
from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
from datetime import datetime
from colorama import Fore, init as color_ama
from bs4 import BeautifulSoup

color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

api_id = 1706449
api_hash = '22e61379be9640e6123482e5002937f3'


print(Fore.MAGENTA + ' code by : riskiakbar279\n' + Fore.RESET)
print(Fore.RED + '  website : riskiakbar279.rf.gd' + Fore.RESET)

print('\n menuyul  work.\n')

print(' Options: \n')
option = ["Zcash_click_bot"]

for number, letter in enumerate(option):
    print(	"	", number, letter)

ask = int(input ("	\n	Which bot do you want to run?" + Fore.RED + " (Number only)" + Fore.RESET + ":" ))
answer = (option[ask])
url_channel = answer

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

def get_response(url, method='GET'):
	response = requests.request(method, url, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win32; x86) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}, timeout=15)
	text_response = response.text
	status_code = response.status_code
	return[status_code, text_response]
		
async def main():
	print(Fore.GREEN + url_channel + Fore.RESET + " selected.\n")
	print('		DogeClick Bot Channel Actions Menu.\n')
	# Bot options
	print(' Options: \n')
	action = ["visit"] #Bot option list
                                                             
	# Print bot options list with numberings
	for number, letter in enumerate(action):
		print(	"	", number, letter)

#login
user = raw_input("Username pembuat: ")

import getpass

sandi = getpass.getpass()

if sandi == 'update-terus' and user == 'riskis7':

    print "Anda Telah Login"

else:

    print "Username atau Password Anda Salah"

	# Ask user to select bot
	ask_action = int(input ("	\n	What bot's action do you want to perform?" + Fore.RED + " (Number only)" + Fore.RESET + ":" ))
	answer = (action[ask_action])
	bot_action = answer
	if answer == action[0]:
		print(action[0] + " performed")
				# Check if phone number is not specified
		if len(sys.argv) < 2:
			print('Usage: python start.py phone_number')
			print('-> Input number in international format (example: +62)\n')
			e = input('Press any key to exit...')
			exit(1)
			

		phone_number = sys.argv[1]
		
		if not os.path.exists("session"):
			os.mkdir("session")
	   
		# Connect to client
		client = TelegramClient('session/' + phone_number, api_id, api_hash)
		await client.start(phone_number)
		me = await client.get_me()
		ads_channel = "@digicoinindoo"
		await client(JoinChannelRequest(ads_channel))
		ads_group = "bcset"
		await client(JoinChannelRequest(ads_group))
		print('Current account:' + Fore.CYAN + f'{me.first_name}({me.username})\n' + Fore.RESET)
		print_msg_time(Fore.YELLOW + 'Sending /visit command'+ Fore.RESET)
		
		# Start command /visit
		await client.send_message(url_channel, 'visit')
		
		# Start visiting the ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def visit_ads(event):
		
		
			original_update = event.original_update
			if type(original_update)is not UpdateShortMessage:
				if hasattr(original_update.message,'reply_markup') and type(original_update.message.reply_markup) is ReplyInlineMarkup:
					url = event.original_update.message.reply_markup.rows[0].buttons[0].url
					#url = event.message.reply_markup.rows[0].buttons[0].url
				
					if url is not None:
						print_msg_time('Visiting website...')

						# Parse the html of url
						(status_code, text_response) = get_response(url)
						parse_data = BeautifulSoup(text_response, 'html.parser')
						captcha = parse_data.find('div', {'class':'g-recaptcha'})
						
						# Captcha detected
						if captcha is not None:
							print_msg_time(Fore.RED + 'Captcha detected!'+ Fore.RED +' Skipping ads...\n')
										
							# Clicks the skip
							await client(GetBotCallbackAnswerRequest(
								peer=url_channel,
								msg_id=event.message.id,
								data=event.message.reply_markup.rows[1].buttons[1].data
							))		
			
		# Print earned money
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def wait_hours(event):
			message = event.raw_text
			if 'You earned' in message:	
				print_msg_time(Fore.GREEN + f'{message}' + Fore.RESET)
		

			# Print earned money
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def manual_skip(event):
			message = event.raw_text
			if 'Skipping task...' in message:	
				print_msg_time(Fore.YELLOW + f'{message}' + Fore.RESET)
		# No longer valid
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_valid(event):
			message = event.raw_text
			if 'Sorry, that task is no longer valid' in message:	
				print_msg_time(Fore.RED + 'Sorry, that task is no longer valid.' + Fore.RESET)
				print_msg_time(Fore.YELLOW + 'Sending visit' + Fore.RESET)
				await client.send_message(url_channel, 'visit')
		# No more ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_ads(event):
			message = event.raw_text
			if 'no new ads available' in message:	
				print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)
				e = input('Press any key to exit...')
				exit(1)
	elif answer == action[1]:
		print(action[1] + " performed")
				# Check if phone number is not specified
		if len(sys.argv) < 2:
			print('Usage: python start.py')
			print('-> Input number in international format (example: +62)\n')
			e = input('Press any key to exit...')
			exit(1)
			
		phone_number = sys.argv[1]
		
		if not os.path.exists("session"):
			os.mkdir("session")
	                                  
		print('Current account:' + Fore.CYAN + f'{me.first_name}({me.username})\n' + Fore.RESET)
		print_msg_time('Sending /bots command')
		
		
			
		
		# Print earned amount
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def earned_amount(event):
			message = event.raw_text
			if 'You earned' in message:	
				print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
				
		# No more ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_ads(event):
			message = event.raw_text
			if 'no new ads available' in message:	
				print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)
				e = input('Press any key to exit...')
				exit(1)
	elif answer == action[2]:
		print(action[2] + " performed")
				# Check if phone number is not specified
		if len(sys.argv) < 2:
			print('Usage: python start.py phone_number')
			print('-> Input number in international format (example: +62)\n')
			e = input('Press any key to exit...')
			exit(1)
			
		phone_number = sys.argv[1]
		
		if not os.path.exists("session"):
			os.mkdir("session")
	   
		
		# Print waiting hours
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def wait_hours(event):
			message = event.raw_text
			if 'You must stay' in message:	
				waiting_hours = re.search(r'at least (.*?) to earn', message).group(1)
				print_msg_time(Fore.GREEN + f'Success! Please wait {waiting_hours} to earn reward\n' + Fore.RESET)
				
		# No more ads
		@client.on(events.NewMessage(chats=url_channel, incoming=True))
		async def no_ads(event):
			message = event.raw_text
			if 'no new ads available' in message:	
				print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)
				e = input('Press any key to exit...')
				(1)
	else:
		print("ulang..")
		exit

	
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())
