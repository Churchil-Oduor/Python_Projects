# ROT13
ROT13 was an early and simple encryption scheme that was put in place to encrypt data.

The logic of operation is as follows:

	There are 26 letters in the alphabet with the middle letter being letter N(n for small letters).

	If we were to assign numbers to the letters with A = 1 and continuing to Z = 26, then we can encrypt data by adding 13 to letters whose numerical value is less than 13, i.e letters before N, and if the letter is N or letters after N, then we subtract 13 to the numerical value of the letter.

For instance:

	text		    | B | A | N  | A |  N  | A	
	Numerical Value | 2 | 1 | 13 | 1 | 13  | 1
	Rot13 substitute| 15| 14| 0  | 14| 0   | 14
	Encrypted alph  | O | N | A  | N | A   | N

If we were to encrypt the text -> banana, then we'd get -> onanan as the output.\

There are other encryption schemes which are far from the scope of this repo, whose main agenda is keeping data safe.

# How do I test this?

Place the file containing the code i.e rot13.py in you the directory of your project and you can import it as follows in your files.

	# python code
	from rot13 import rot13

	text = "Hello" # text to be encrypted
	encrypted = rot13(text) # string in text is encripted and stored in variable

print(encrypted) # you can print the encrypted data

# How do I decrypt back to my original data?
To Decrypt the data, run the same operation  as encrypting and this will decrypt the data.

From this we can see why it isn't a really good approach to securing data. It is fairly simple and can be easily cracked...but it is a fun way to get wet with encryption methods.\

Happy Hacking!!