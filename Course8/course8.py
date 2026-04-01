#Course 8.1: Searching for Businesses

# import requests

# url = "insert API link" # The API link to get data from the API.
# api_key = "insert API key" # The API key to access the API.
# headers {
#     "Authorization": "Bearer " + api_key
# }

# params = {
#     "location": "insert location", # The location to search for businesses.
# }
# response = requests.get(url, headers=headers, params) # A request from and API to get data from the API.
# print(response.text) 


#Course 8.2: Sending Text Messages

# from twilio.rest import Client # Importing the Twilio library to send text messages.

# account_sid = "insert account SID" # The account SID to access the Twilio API.
# auth_token = "insert auth token" # The auth token to access the Twilio API.

# client = Client(account_sid, auth_token) # A client to access the Twilio API.

# call = client.messages.create(
#     to="insert phone number", # The phone number to send the text message to.
#     from_="insert Twilio phone number", # The Twilio phone number to send the text message from.
#     body="This is our first message" # The message to send in the text message.
# )


#Course 8.3: Web Scraping

# import requests
# from bs4 import BeautifulSoup

# response = requests.get("insert URL") # A request to get data from a website.
# soup = BeautifulSoup(response.text, "html.parser") # A BeautifulSoup object to parse the HTML of the website.

# questions = soup.select(".question-summary") # A list of all the elements with the class "question-summary" in the HTML of the website.
# print(questions[0].select(".question-hyperlink"))


#Course 8.4: Browser Automation

# from selenium import webdriver # Importing the Selenium library to automate the browser.

# browser =webdriver.Firefox() # A Firefox web driver to automate the browser.
# browser.get("https://github.com") # A request to get the Google homepage.

# signin_link = browser.find_element_by_link_text("Sign in") # Finding the "Sign in" link on the GitHub homepage.
# signin_link.click() # Clicking the "Sign in" link to go to the sign in page.

# username_box = browser.find_element_by_id("login_field") # Finding the username input box on the sign in page.
# username_box.send_keys("insert username") # Typing the username into the username input box.
# password_box = browser.find_element_by_id("password") # Finding the password input box on the sign in page.
# password_box.send_keys("insert password") # Typing the password into the password input box.
# password_box.submit() # Submitting the form to sign in to GitHub.

# assert "Your profile" in browser.page_source # Asserting that the "Your profile" text is in the HTML of the page to confirm that we are signed in to GitHub.

# profile_link = browser.find_element_by_class_name("avatar") # Finding the profile link on the GitHub homepage.
# link_label = profile_link.get_attribute("innerHTML")
# assert "insert username" in link_label # Asserting that the username is in the inner HTML of the profile link to confirm that we are signed in to GitHub.

# browser.quit() # Closing the browser.


#Course 8.5: Working with PDFs

import PyPDF2 # Importing the PyPDF2 library to work with PDFs.

# PyPDF2.PdfFileReader() # A PDF file reader to read the PDF file.
# PyPDF2.PdfFileWriter() # A PDF file writer to write to a PDF file.
# PyPDF2.PdfFileMerger() # A PDF file merger to merge multiple PDF files into one PDF file.
# with open("Course8/first.pdf", "rb") as file:
#     reader = PyPDF2.PdfReader(file) # A PDF file reader to read the "first.pdf" file.
#     print(reader.numPages)
#     page = reader.getPage(0) # Getting the first page of the PDF file.
#     page.rotateClockwise(90) # Rotating the page 90 degrees clockwise.
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
#     with open("rotated.pdf", "wb") as output:
#         writer.write(output) # Writing the rotated page to a new PDF file called "rotated.pdf".

# merger = PyPDF2.pdfFileMerger() # A PDF file merger to merge multiple PDF files into one PDF file.
# file_names = ["first.pdf", "second.pdf"]
# for file_name in file_names:
#     merger.append(file_name) # Appending each PDF file to the merger.
# merger.write("combined.pdf")


#Course 8.6: Working with Excel Spreadsheets

# import openpyxl # Importing the openpyxl library to work with Excel spreadsheets.
# wb = openpyxl.load_workbook("Course8/transactions.xlsx") # Loading the "spreadsheet.xlsx" file into a workbook object.
# print(wb.sheetnames) # Printing the names of the sheets in the workbook.

# sheet = wb["Sheet1"]

# wb.create_sheet("Sheet2", 0) # Creating a new sheet called "Sheet2" in the workbook.
# wb.remove_sheet(sheet) # Removing the "Sheet1" sheet from the workbook.

# cell = sheet["a1"]
# print(cell.value)
# print(cell.row) # cell.row is the row number of the cell.
# print(cell.column) # cell.column is the column number of the cell.
# print(cell.coordinate) # cell.coordinate is the coordinate of the cell (e.g. "A1").
# cell = sheet.cell(row = 1, column = 1)
# print(sheet.max_row) # sheet.max_row is the maximum row number in the sheet.
# print(sheet.max_column) # sheet.max_column is the maximum column number in the sheet.
# for row in range(1, "sheet.max.row" + 1):
#     for column in range(1, sheet.max_column + 1):
#         cell = sheet.cell(row, column)
#         print(cell.value) # Printing the value of each cell in the sheet.

# column = sheet["a"] # sheet["a"] is a list of all the cells in column A of the sheet.
# cells = sheet["a:c"] # sheet["a:c"] is a list of all the cells in columns A, B, and C of the sheet.
# sheet["a1:c3"] # sheet["a1:c3"] is a list of all the cells in the range A1 to C3 of the sheet.
# print(cells)

# sheet.append([1, 2, 3]) # Appending a new row with the values 1, 2, and 3 to the sheet.
# sheet.insert_rows(1) # Inserting a new row at the top of the sheet.
# sheet.insert_cols(1) # Inserting a new column at the left of the sheet.
# sheet.delete_rows(1) # Deleting the first row of the sheet.
# wb.save("transactions.xlsx") # Saving the changes to the "spreadsheet.xlsx" file.  


#Course 8.7: Command Query Separation Principle

# import openpyxl

# wb = openpyxl.load_workbook("Course8/transactions.xlsx")
# # wb.create_sheet("")
# sheet = wb["Sheet1"]
# for row in range(1, 10): 
#     cell = sheet.cell(row, 1) 
#     print(cell.value) # Printing the value of the first column of each row in the sheet.
# sheet.append([1, 2, 3]) # Appending a new row with the values 1, 2, and 3 to the sheet.
# wb.save("transactions2.xlsx") # Saving the changes to a new file called "transactions2.xlsx" to avoid overwriting the original file.


#course 8.8: NumPy

import numpy as np # Importing the NumPy library to work with arrays.

# array = np.array([[1, 2, 3], [4, 5, 6]]) # Creating a NumPy array from a list of numbers.
# print(array)
# # print(type(array)) # Printing the type of the array to confirm that it is a NumPy array.
# print(array.shape) # Printing the shape of the array to confirm that it is a 2D array with 2 rows and 3 columns.

# array = np.zeros((3, 4), dtype=int) # Creating a 3x4 array filled with zeros.
# array = np.ones((3, 4), dtype=int) # Creating a 3x4 array filled with zeros.
# array = np.full((3, 4), 5, dtype=int) # Creating a 3x4 array filled with zeros.
# array = np.random.random((3, 4)) # Creating a 3x4 array filled with zeros.
# print(array)
# print(array[0, 0]) # Printing the value of the first element in the array.
# print(array > 0.2) # Printing a boolean array where each element is True if the corresponding element in the original array is greater than 0.2 and False otherwise.
# print(array[array > 0.2]) # Printing the values of the original array that are greater than 0.2.
# print(np.sum(array)) # Printing the sum of all the elements in the array.
# print(np.floor(array)) # Printing the floor of each element in the array.
# print(np.round(array)) # Printing the rounded value of each element in the array.

# first = np.array([1, 2, 3]) # Creating a NumPy array from a list of numbers.
# second = np.array([1, 2, 3]) # Creating a NumPy array from a list of numbers.
# print(first + second) # Adding the two arrays together element-wise.
# print(first + 2) # Adding 2 to each element in the array.

# dimensions_inch = np.array([1, 2, 3]) # Creating a NumPy array from a list of numbers.
# dimensions_cm = dimensions_inch * 2.54 # Converting the dimensions from inches to centimeters by multiplying each element in the array by 2.54.
# print(dimensions_cm) # Printing the dimensions in centimeters.

# dimensions_inch = [1, 2, 3] # Creating a list of numbers.
# dimensions_cm = [x * 2.54 for x in dimensions_inch] # Using a list comprehension to create a new list with the same values as the original list.

# NumPy arrays is my favorite part of this course.