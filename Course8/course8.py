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

# import PyPDF2 # Importing the PyPDF2 library to work with PDFs.

# with open("first.pdf", "rb") as file: # Opening the PDF file in read-binary mode.
#     reader = PyPDF2.PdfFileReader()
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
    # writer.insertPage(page, 0)
    # writer.insertBlankPage(0, 100, 100)
    # with open("rotated.pdf", "wb") as output:
    #     writer.write(output)

# merger = PyPDF2.PdfFileMerger()
# file_names = ["first.pdf", "second.pdf"]
# for file_name in file_names:
#     merger.append(file_name)
# merger.write("combined.pdf")