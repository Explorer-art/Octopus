# -*- coding:utf-8 -*-
#!usr/bin/python
import os
import sys
import itertools
import argparse
import hashlib

parser = argparse.ArgumentParser()

parser.add_argument("min", help="Minimal lenght password.", type=int)
parser.add_argument("max", help="Maximum lenght password.", type=int)
parser.add_argument("-m", "--mode", help="Modes of operation of the program.")
parser.add_argument("-t", "--type", help="Type generating passwords.")
parser.add_argument("-i", "--instruction", help="Instruction generating a passwords.")
parser.add_argument("-f", "--file", help="Save passwords in file.")
parser.add_argument("-bh", "--bhash", help="Hash.")

args = parser.parse_args()

minimal_lenght = args.min
maximal_lenght = args.max
mode = args.mode
type_1 = args.type
instruction_generating = args.instruction
save_in_file = args.file
hash_bruteforce = args.bhash

if mode == "G":
	if type_1 == "N":
		print("Octopus v 1.2 by Truzme_\n")

		if save_in_file is not None:
			check_1 = os.path.isdir("Passwords")

			if check_1 == False:
				os.mkdir("Passwords")
			print("Generating..")

			file_1 = open("Passwords/" + save_in_file, "w")

			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("1234567890", repeat=r):
					a += 1
					file_1.write(''.join(i) + "\n")
				r += 1
			file_1.close()
			print("")
			print("Saving..")
			print("Done!")
			print("")
			print("Number of combinations: " + str(a))
		if save_in_file is None:
			print("Generating..")
			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				print(r)
				for i in itertools.product("1234567890", repeat=r):
					a += 1
					print(''.join(i))
				r += 1
			print("")
			print("Done!")
			print("")
			print("Number of combinations: " + str(a))

	if type_1 == "NL":
		print("Octopus v 1.2 by Truzme_\n")

		if save_in_file is not None:
			check_1 = os.path.isdir("Passwords")

			if check_1 == False:
				os.mkdir("Passwords")
			print("Generating..")

			file_2 = open("Passwords/" + save_in_file, "w")

			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					file_2.write(''.join(i) + "\n")
				r += 1
			file_2.close()
			print("")
			print("Saving..")
			print("Done!")
			print("Number of combinations: " + str(a))
		elif save_in_file is None:
			print("Generating..")
			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					print(''.join(i))
				r += 1
				print("")
				print("Done!")
			print("Number of combinations: " + str(a))

	if type_1 == "NLS":
		print("Octopus v 1.2 by Truzme_\n")

		if save_in_file is not None:
			check_1 = os.path.isdir("Passwords")

			if check_1 == False:
				os.mkdir("Passwords")
			print("Generating..")

			file_3 = open("Passwords/" + save_in_file, "w")

			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					file_3.write(''.join(i) + "\n")
				r += 1
			file_3.close()
			print("")
			print("Saving..")
			print("Done!")
			print("Number of combinations: " + str(a))
		elif save_in_file is None:
			print("Generating..")
			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					print(''.join(i))
				r += 1
			prin("")
			print("1")
			print("Number of combinations: " + str(a))
	if type_1 == "I":
		print("Octopus v 1.2 by Truzme_\n")

		if instruction_generating is None:
			print("Error! Instructions are not given.")
			sys.exit()

		if save_in_file is not None:
			check_1 = os.path.isdir("Passwords")

			if check_1 == False:
				os.mkdir("Passwords")
			print("Generating..")

			file_4 = open("Passwords/" + save_in_file, "w")

			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product(instruction_genereting, repeat=r):
					a += 1
					file_4.write(''.join(i) + "\n")
				r += 1
			file_4.close()
			print("")
			print("Saving..")
			print("Done!")
			print("Number of combinations: " + str(a))
		elif save_in_file is None:
			print("Generating..")
			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product(instruction_generating, repeat=r):
					a += 1
					print(''.join(i))
				r += 1
			print("")
			print("Done!")
			print("Number of combinations: " + str(a))
elif mode == "B":
	try:
		if type_1 == "MD5":
			print("Bruteforce..")
			with open(save_in_file, "r", encoding="utf-8", errors="ignore") as file_5:
				for password in file_5:
					bruteforce = hashlib.md5(password.encode().strip()).hexdigest()

					if bruteforce == hash_bruteforce:
						print("Done!")
						print("Password: " + password)
						file_5.close()
		if type_1 == "SHA1":
			print("Bruteforce..")
			with open(save_in_file, "r", encoding="utf-8", errors="ignore") as file_5:
				for password in file_5:
					bruteforce = hashlib.sha1(password.encode().strip()).hexdigest()

					if bruteforce == hash_bruteforce:
						print("Done!")
						print("Password: " + password)
						file_5.close()
		if type_1 == "SHA224":
			print("Bruteforce..")
			with open(save_in_file, "r", encoding="utf-8", errors="ignore") as file_5:
				for password in file_5:
					bruteforce = hashlib.sha224(password.encode().strip()).hexdigest()

					if bruteforce == hash_bruteforce:
						print("Done!")
						print("Password: " + password)
						file_5.close()
		if type_1 == "SHA256":
			print("Bruteforce..")
			with open(save_in_file, "r", encoding="utf-8", errors="ignore") as file_5:
				for password in file_5:
					bruteforce = hashlib.sha256(password.encode().strip()).hexdigest()

					if bruteforce == hash_bruteforce:
						print("Done!")
						print("Password: " + password)
						file_5.close()
		if type_1 == "SHA384":
			print("Bruteforce..")
			with open(save_in_file, "r", encoding="utf-8", errors="ignore") as file_5:
				for password in file_5:
					bruteforce = hashlib.sha384(password.encode().strip()).hexdigest()

					if bruteforce == hash_bruteforce:
						print("Done!")
						print("Password: " + password)
						file_5.close()
		if type_1 == "SHA512":
			print("Bruteforce..")
			with open(save_in_file, "r", encoding="utf-8", errors="ignore") as file_5:
				for password in file_5:
					bruteforce = hashlib.sha512(password.encode().strip()).hexdigest()

					if bruteforce == hash_bruteforce:
						print("Done!")
						print("Password: " + password)
						file_5.close()
	except:
		print("Error! File not found.")
		sys.exit()

elif mode is None:
	if type_1 == "N":
		print("Octopus v 1.2 by Truzme_\n")

		if save_in_file is not None:
			check_1 = os.path.isdir("Passwords")

			if check_1 == False:
				os.mkdir("Passwords")
			print("Generating..")

			file_1 = open("Passwords/" + file_name, "w")

			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("1234567890", repeat=r):
					a += 1
					file_1.write(''.join(i) + "\n")
				r += 1
			file_1.close()
			print("")
			print("Saving..")
			print("Done!")
			print("")
			print("Number of combinations: " + str(a))
		if save_in_file is None:
			print("Generating..")
			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				print(r)
				for i in itertools.product("1234567890", repeat=r):
					a += 1
					print(''.join(i))
				r += 1
			print("")
			print("Done!")
			print("")
			print("Number of combinations: " + str(a))

	if type_1 == "NL":
		print("Octopus v 1.2 by Truzme_\n")

		if save_in_file is not None:
			check_1 = os.path.isdir("Passwords")

			if check_1 == False:
				os.mkdir("Passwords")
			print("Generating..")

			file_2 = open("Passwords/" + save_in_file, "w")

			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					file_2.write(''.join(i) + "\n")
				r += 1
			file_2.close()
			print("")
			print("Saving..")
			print("Done!")
			print("Number of combinations: " + str(a))
		elif save_in_file is None:
			print("Generating..")
			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					print(''.join(i))
				r += 1
				print("")
				print("Done!")
			print("Number of combinations: " + str(a))

	if type_1 == "NLS":
		print("Octopus v 1.2 by Truzme_\n")

		if save_in_file is not None:
			check_1 = os.path.isdir("Passwords")

			if check_1 == False:
				os.mkdir("Passwords")
			print("Generating..")

			file_3 = open("Passwords/" + save_in_file, "w")

			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					file_3.write(''.join(i) + "\n")
				r += 1
			file_3.close()
			print("")
			print("Saving..")
			print("Done!")
			print("Number of combinations: " + str(a))
		elif save_in_file is None:
			print("Generating..")
			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					print(''.join(i))
				r += 1
			prin("")
			print("Done!")
			print("Number of combinations: " + str(a))
	elif type_1 is None:
		print("Octopus v 1.2 by Truzme_\n")

		if save_in_file is not None:
			check_1 = os.path.isdir("Passwords")

			if check_1 == False:
				os.mkdir("Passwords")
			print("Generating..")

			file_2 = open("Passwords/" + save_in_file, "w")

			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					file_2.write(''.join(i) + "\n")
				r += 1
			file_2.close()
			print("")
			print("Saving..")
			print("Done!")
			print("Number of combinations: " + str(a))
		elif save_in_file is None:
			print("Generating..")
			a = 0

			r = minimal_lenght

			while r <= maximal_lenght:
				for i in itertools.product("abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890", repeat=r):
					a += 1
					print(''.join(i))
				r += 1
				print("")
				print("Done!")
			print("Number of combinations: " + str(a))
