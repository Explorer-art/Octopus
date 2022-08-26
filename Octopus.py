# -*- coding:utf-8 -*-
#!usr/bin/python
import os
import sys
import itertools
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("min", help="Minimal lenght password.", type=int)
parser.add_argument("max", help="Maximum lenght password.", type=int)
parser.add_argument("mode", help="Mode generating passwords.")
parser.add_argument("-save", help="Save passwords in file.")

args = parser.parse_args()

minimal_lenght = args.min
maximal_lenght = args.max
mode = args.mode
save_in_file = args.save

if mode == "N":
	print("Octopus v 1.0 by Truzme_\n")

	if save_in_file == "s":
		check_1 = os.path.isdir("Passwords")

		if check_1 == False:
			os.mkdir("Passwords")
		file_name = input("Enter file name: ")
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

if mode == "NL":
	print("Octopus v 1.0 by Truzme_\n")

	if save_in_file == "s":
		check_1 = os.path.isdir("Passwords")

		if check_1 == False:
			os.mkdir("Passwords")
		file_name = input("Enter file name: ")
		print("Generating..")

		file_2 = open("Passwords/" + file_name, "w")

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

if mode == "NLS":
	print("Octopus v 1.0 by Truzme_\n")

	if save_in_file == "s":
		check_1 = os.path.isdir("Passwords")

		if check_1 == False:
			os.mkdir("Passwords")
		file_name = input("Enter file name: ")
		print("Generating..")

		file_3 = open("Passwords/" + file_name, "w")

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