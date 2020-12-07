"""
CSS Minifier (python)

The script for minifying the CSS Script files on the website / web application's frontend.

Author : Rishav Das
"""

# Importing the required modules
from requests import post
from os import path
from sys import platform, argv

def main():
	"""
The main function of this script
	"""

	# Asking the user for the CSS file location if not mentioned via arguments
	try:
		fileLocation = argv[1]
	except:
		fileLocation = input('Enter the CSS file location : ')
	finally:
		# If everything goes fine and we recieve the CSS file location in any of the either ways, then we continue the process

		if path.isfile(fileLocation):
			# If the user specified css file exists on the local machine, then we continue

			try:
				css = open(fileLocation, 'r').read()
				response = post('https://cssminifier.org', data = {"css": css})
			except Exception as e:
				# If there are any errors in the process, then we print the error

				print('[ Error : {} ]'.format(e))
			else:
				# If there are no errors in the process, then we execute further

				if response.status_code == 200:
					# If the response code indicates proper transmission of the data, then we proceed further

					try:
						# Extracting the minified CSS code
						response = response.text
						response = response.split('<textarea name="modified" id="modified" class="form-control" autocomplete="off" rows="12">')[1]
						response = response.split('</textarea>')[0]
					except:
						# If there are any errors in the process of the extraction of the minified CSS code, then we raise the error as a console screen message

						print('[ Error : Failed to extract the minified CSS code from the response')
					else:
						# If there are no errors in the process, then we proceed to ask the user for the saving location of the CSS file

						fileLocation = input('Enter the location for saving the minified CSS file : ')
						try:
							open(fileLocation, 'w+').write(response)
						except Exception as e:
							# If there are any errors in the process of the saving the minified CSS code, then we print the error message on the console screen

							print('[ Error : {} ]'.format(e))
						else:
							# If there are no errors in the saving the minified CSS file process, then we end up with printing the success message on the console screen

							print('[ Success : Request CSS has been minified and saved at {} ]'.format(fileLocation))
				else:
					# If the response code indicates failure, then we print the error message on the console screen

					print('[ Error : Failed to minify the CSS file, Wrong response from the server ]')
		else:
			# If the user specified file does not exists then we raise an error

			print('[ Error : Specified CSS file does not exists ]')

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		quit()
