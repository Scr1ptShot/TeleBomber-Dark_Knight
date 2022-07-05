import time
import os
import sys

os.system("pip3 install telethon termcolor")

if sys.platform == "win32":
	os.system("cls")

elif sys.platform == "linux":
	os.system("clear")

from termcolor import colored, cprint
from telethon import TelegramClient, events, sync

def Start_Saved_Session():
	global client, acc, id_count
	id_count = []
	hash_count = []
	mark_count = []
	if os.path.exists("Data.txt"):
		with open("Data.txt", "r", encoding = "utf8") as file:
			for line in file:
				try:
					id, hash, sign = line.split(":")
					id_count.append(id)
					hash_count.append(hash)
					mark_count.append(sign)

					if len(id_count) > 0:
						if len(id_count) >= 1:
							print("Choose account.")
							x = 0
							while x < len(id_count):
								print(f"[{x}]:{mark_count[x]}")
								x += 1
							acc = int(input(">> "))
							app_id = id_count[acc]
							app_hash = hash_count[acc]

				except Exception:
					print("Something went wrong.")
					quit()

		try:
			client = TelegramClient(f'telegram_session_{str(acc)}', app_id, app_hash)
			client.start()
			print("Logged in!")
			time.sleep(2)

		except Exception as e:
			print(colored(f"[-]Except: {e}[-]", "red"))
			quit()

def Start_New_Session():
	global client, y
	count = []
	print("Enter app id")
	time.sleep(1)
	app_id = int(input(">> "))
	time.sleep(1)
	print("Enter hash app")
	time.sleep(1)
	hash_app = input(">> ")
	time.sleep(1)
	print("Enter a mark of this account")
	mark = input(">> ")

	with open("Data.txt", "a+", encoding = "utf8") as file:
		file.write(f"{app_id}:{hash_app}:{mark}")
		for line in file:
			x = line.split(":")
			id_count.append(x)
			count.append(x)

	len_count = len(count)
	number_session = str(y)

	client = TelegramClient(f'telegram_session_{number_session}', app_id, hash_app)
	client.start()

def banner():
	if sys.platform == "win32":
		os.system("cls")

	elif sys.platform == "linux":
		os.system("clear")

	logo = print("""

██████╗░░█████╗░██████╗░██╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝
██║░░██║███████║██████╔╝█████═╝░
██║░░██║██╔══██║██╔══██╗██╔═██╗░
██████╔╝██║░░██║██║░░██║██║░╚██╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

██╗░░██╗███╗░░██╗██╗░██████╗░██╗░░██╗████████╗
██║░██╔╝████╗░██║██║██╔════╝░██║░░██║╚══██╔══╝
█████═╝░██╔██╗██║██║██║░░██╗░███████║░░░██║░░░
██╔═██╗░██║╚████║██║██║░░╚██╗██╔══██║░░░██║░░░
██║░╚██╗██║░╚███║██║╚██████╔╝██║░░██║░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
""")

	time.sleep(2)

	print("[1]: Message bomber \n[2]: Image bomber (only PNG) \n[99]: quit")
	choose = input(">> ")

	if choose == '1':
		Mes()

	elif choose == '2':
		Img()

	elif choose == '99':
		quit()

def Mes():

	user_id = input(str("Enter user's nickname: "))
	message_user = input(str("Input message: "))
	x = input("Enter count of messages (only integer): ")
	y = 0
	delay = input("Enter delay (sec): ")

	while y < int(x):
		time.sleep(float(delay))
		client.send_message(user_id, message_user)
		print(colored("Sent to " + user_id, "green"))
		y = y + 1

	print(colored(user_id + " was bombed!", "red"))
	time.sleep(2)
	banner()

def Img():

	user_id = input(str("Enter user's nickname: "))
	message_image = input(str("Input path to image: "))

	if os.path.exists(message_image):
		print(colored("Found!", "green"))
		time.sleep(1)

	else:
		print("No image exists")
		Img()

	x = input("Enter count of messages (only integer): ")
	y = 0
	delay = input("Enter delay (sec): ")

	while y < int(x):
		time.sleep(float(delay))
		client.send_file(user_id, message_image)
		print(colored("Sent to " + user_id, "green"))
		y = y + 1

	print(colored(user_id + " was bombed!", "red"))
	time.sleep(2)
	banner()

def main():

	print("Do you wanna start new session?(y/n)")
	new_session = input(">> ")

	if new_session == "y" or new_session == "Y" or new_session == "yes" or new_session == "Yes":
		Start_New_Session()

	else:
		Start_Saved_Session()

	banner()

time.sleep(2)

main()
