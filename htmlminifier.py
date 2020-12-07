"""
HTML Minifier (python)

The script minifies HTML code files to a smaller compiled version.

Author : Rishav Das
"""

# Importing the required modules and objects
from requests import post
from os import path
from sys import argv

def main():
	"""
The main function of the script
	"""

	try:
		# Getting the HTML file from the argument given by the user

		fileLocation = argv[1]
	except IndexError:
		# If there are any errors fetching the HTML file location from the argument, then we ask it manually

		fileLocation = input('Enter the HTML file location : ')
	finally:
		# Executing the further process

		if path.isfile(fileLocation):
			# If the user specified HTML file does exists, then we start the further process

			try:
				# Reading the HTML file

				html = open(fileLocation, 'r').read()
				response = post('https://www.willpeavy.com/tools/minifier/', data = {"html" : html})
			except Exception as e:
				# If there are any errors in the process, then we print the error message on the console screen

				print('[ Error : {} ]'.format(e))
			else:
				# If there are no errors in the process, then we execute the further code

				if response.status_code == 200:
					# If the response code states successfull http response

					try:
						# Parsing the HTML response from the server in order to extract the HTML minified which is present within the textarea element

						response = response.text
						response = response.split('<textarea')
						response.pop(0)
						response = "".join(response)
						response = response.split('</html>')[0]
						html = ''
						add = False
						for i,j in enumerate(response):
							if add:
								html += j
							else:
								if j == '<' and response[i+1] == '!':
									add = True
									html += j
								else:
									continue
						html += '</html>'
					except Exception as e:
						# If there are any errors in the process, then we print the error on the console screen

						print('[ Error : Failed to parse the response from the server ]')
					else:
						# If the response has been parsed without any errors, then we proceed to saving the minified HTML code to a file on the local machine's filesystem

						fileLocation = input('Enter the location to save the minified HTML file : ')
						try:
							# Saving the minified HTML code to the user specified file location

							open(fileLocation, 'w+').write(html)
						except Exception as e:
							# If there are errors in saving the minified HTML code to the local machine's filesystem and also with the user provided location, then we print those errors as messages on the console screen

							print('[ Error : {} ]'.format(e))
						else:
							# If there are no errors in saving the minified HTML code to the filesystem of the local machine, then the whole process is complete and we can end the script with printing a success message

							print('[ Success : Request HTML has been minified and saved at {} ]'.format(fileLocation))
				else:
					# If the response from the server states failed or any other http error responses

					print('[ Error : Failed to minify the HTML file, Wrong response from the server ]')

		else:
			# If the user specified HTML file does not exists, then we print the error message on the console screen

			print('[ Error : The specified HTML file {} does not exists ]'.format(fileLocation))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()