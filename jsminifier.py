"""
JavaScript Minifier (python)

The script for minifying the javascript codes to a oneliner thing.

Author : Rishav Das
"""

# Importing the required modules and functions
from requests import post
from json import loads
from os import path
from sys import argv

def main():
	"""
The main function of the script
	"""

	try:
		# Getting the JS file location from the user entered argument while calling the script (program)

		fileLocation = argv[1]
	except IndexError:
		# If the user did not mentioned the JS file location via the arguments, then we ask for the file location manually

		fileLocation = input('Enter the javascript file location : ')
	finally:
		# After getting the javascript file location from the user in any either way, we continue to do the process

		if path.isfile(fileLocation):
			# If the user mentioned file exists, then we proceed further to read the JS code from the file and sending it to the server

			try:
				source = open(fileLocation,'r').read()
				response = post('https://www.minifier.org/minify.php', data = {"source" : source, "type" : "js"})
			except Exception as e:
				print('[ Error : {} ]'.format(e))
			else:
				# If there are no errors in the process of sending the HTTP post requests to the server, then we proceed further parsing the response in order to extract the minified javascript code

				if response.status_code == 200:
					# If the response from the server states no HTTP error (i.e., 200 HTTP code)

					# Extracting the minified javascript code
					try:
						response = loads(response.text)['minified']
					except Exception as e:
						# If there are any errors in the process of the extraction of the minfied javascript code, then we will print the error message on the console screen

						print('[ Error : {} ]'.format(e))
					else:
						# If there are no errors in the process, then we proceed further for saving the minified code to the user specified location in the local machine's filesystem

						# Asking the user for the location to save the file
						fileLocation = input('Enter the location to save the minified javascript : ')
						try:
							open(fileLocation, 'w+').write(response)
						except Exception as e:
							# If there are any errors in the process of the saving the minified javascript code to the local machine's filesystem, then we print the error message on the console screen

							print('[ Error : {} ]'.format(e))
						else:
							# If there are no errors in the saving of the file, then we have completed the entire work. We print a success message on the console screen

							print('[ Success : Request javascript has been minified and saved at {} ]'.format(fileLocation))
				else:
					# If the response from the server states error HTTP response

					print('[ Error : Failed to minify the javascript file, Wrong response from the server ]')
					input(response.text)
		else:
			# If the user specified HTML file does not exists on the filesystem of the local machine

			print('[ Error : Specified javascript file does not exists ]')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()