#Course 6.1: Working with Paths

# from pathlib import Path

# # Path(r"C:\Program Files\Microsoft")
# # Path() # The current working directory is used as the default path when you create a Path object without any arguments.
# path = Path("Course5/ecommerce/__init__.py")
# # # Path() / Path("ecommerce")
# # Path() / "ecommerce" / "__init__.py"
# # Path.home() # The home directory of the current user is used as the default path when you create a Path object without any arguments.
# path.exists() # Checks if the path exists
# path.is_file() # Checks if the path is a file
# path.is_dir() # Checks if the path is a directory
# print(path.name)
# print(path.stem) # The stem is the name of the file without the extension.
# print(path.suffix) # The suffix is the file extension, including the dot.
# print(path.parent) # The parent is the directory that contains the file.

# # path = path.with_name("file.txt") # The with_name() method is used to change the name of the file in the path.
# path = path.with_suffix(".text") # The with_suffix() method is used to change the file extension in the path.
# # print(path.absolute()) # The absolute() method is used to get the absolute path of the file.
# print(path)


#Course 6.2: Working with Directories

# from pathlib import Path

# path = Path("Course5/ecommerce")
# # # path.exists() # Checks if the path exists
# # # path.mkdir() # Creates a directory at the specified path.
# # # path.rmdir() # Removes the directory at the specified path.
# path.rename("ecommerce2") # Renames the directory at the specified path.

# print(path.iterdir()) # The iterdir() method is used to iterate over the files and directories in the specified path.
# paths = [p for p in path.iterdir() if p.is_dir()] # The is_dir() method is used to check if the path is a directory.
# py_files = [p for p in path.rglob("*.py")] # The glob() method is used to find all the files in the specified path that match the specified pattern.
# # # The rglob() method is used to find all the files in the specified path and its subdirectories that match the specified pattern.
# print(py_files)
# #     # print(p) 
# # # PosixPath('ecommerce/__init__.py') is an example of the output of the iterdir() method. It is a Path object that represents the file __init__.py in the ecommerce directory.


# #Course 6.3: Working with Files

# from pathlib import Path
# from time import ctime # The ctime() function is used to convert a time expressed in seconds since the epoch to a string representing local time.
# import shutil # The shutil module is used to perform high-level file operations, such as copying and moving files.


# source = Path("Course6/ecommerce/__init__.py") # source is a Path object that represents the file __init__.py in the ecommerce directory.
# target = Path() / "__init__.py" # target is a Path object that represents the file __init__.py in the current working directory.

# shutil.copy(source, target)
# target.write_text(source.read_text())


# path.exists()
# path.rename("init.txt")
# path.unlink() # The unlink() method is used to delete the file at the specified path.
# print(path.stat()) # The stat() method is used to get the metadata of the file at the specified path, such as its size, creation time, and modification time.
# print(ctime(path.stat().st_ctime)) # The st_ctime attribute of the stat() method is used to get the creation time of the file at the specified path, expressed in seconds since the epoch.

# file = open("__Init__.py", "r") # The open() function is used to open a file at the specified path in the specified mode. The "r" mode is used to open the file for reading.
# with open("__Init__.py", "r") as file: # The with statement is used to ensure that the file is properly closed after it is used.
#     ...

# path.read.bytes() # The read_bytes() method is used to read the contents of the file at the specified path as bytes.
# print(path.read_text()) # The read_text() method is used to read the contents of the file at the specified path as a string.
# path.write_text("...") # The write_text() method is used to write the specified string to the file at the specified path.
# path.write_bytes() # The write_bytes() method is used to write the specified bytes to the file at the specified path.


#Course 6.4: Working with Zip Files

# from pathlib import Path
# from zipfile import ZipFile # The ZipFile class is used to create, read, write, append, and list a ZIP file.

# zip = Zipfile("files.zip", "w") # The "w" mode is used to create a new ZIP file or overwrite an existing one.
# with ZipFile("files.zip", "w") as zip:
#     for path in Path("Course6/ecommerce").rglob("*.*"):
#         zip.write(path) # The write() method is used to add a file to the ZIP file.
# zip.close()

# with ZipFile("files.zip") as zip:
#     print(zip.namelist()) # The namelist() method is used to get a list of the names of the files in the ZIP file.
#     info = zip.getinfo("Course6/ecommerce/__init__.py") # The getinfo() method is used to get the metadata of the specified file in the ZIP file, such as its size and compressed size.
#     print(info.file_size) # The file_size attribute of the getinfo() method is used to get the size of the specified file in the ZIP file, expressed in bytes.
#     print(info.compress_size) # The compress_size attribute of the getinfo() method is used to get the compressed size of the specified file in the ZIP file, expressed in bytes.
#     zip.extractall("extract") # The extractall() method is used to extract all the files in the ZIP file to the specified directory. If the directory does not exist, it will be created.


#Course 6.5: Working with CSV Files

# CSV files stands for Comma-Separated Values files.
# import csv $ The csv module is used to read and write CSV files.

# file = open("data.csv", "w")
# with open("data.csv", "w") as file:
# with open("data.csv") as file:
    # file.close()
    # writer = csv.writer(file) # The csv.writer() function is used to create a writer object that can be used to write data to a CSV file.
    # reader = csv.reader(file) # The csv.reader() function is used to create a reader object that can be used to read data from a CSV file.
    # print(list(reader)) # The list() function is used to convert the reader object to a list of rows, where each row is a list of values.
    # for row in reader:
    #     print(row)
    # writer.writerow(["transaction_id", "product_id", "price"]) # The writerow() method is used to write a single row of data to the CSV file.
    # writer.writerow([1000, 1, 5])
    # writer.writerow([1001, 2, 15])


#Course 6.6 Working with JSON Files

# JSON stands for Javascript Object Notation.

# import json # The json module is used to read and write JSON files.
# from pathlib import Path

# movies = [
#     {"id": 1, "title": "Terminator", "year": 1984},
#     {"id": 2, "title": "Kindergarten Cop", "year": 1990},
# ]

# data = json.dumps(movies) # The json.dumps() function is used to convert a Python object to a JSON string.
# Path("movies.json").write_text(data)
# data = Path("movies.json").read_text() # The read_text() method is used to read the contents of the file at the specified path as a string.
# movies = json.loads(data) # The json.loads() function is used to convert a JSON string to a Python object.
# print(movies[0] ["title"]) 


#Course 6.7: Working with a SQLite Database

# import sqlite3
# import json
# from pathlib import Path

# movies = json.loads(Path("movies.json").read_text())
# print(movies)

# connection = sqlite3.connect("db.sqlite3")
# with sqlite3.connect("db.sqlite3") as conn:
    # command = "INSERT INTO Movies VALUES(?, ?, ?)"
    # command = "SELECT* FROM Movies"
    # cursor = conn.execute(command)
    # for row in cursor:
    #     print(row)
    # movies = cursor.fetchall()
    # print(movies)
    # for movie in movies:
    #     conn.execute(command, tuple(movie.values()))
    # conn.commit()


#Course 6.8: Working with Timestamps

# import time

# print(time.time())
# def send_emails():
#     for i in range(10000):
#         pass

# start = time.time()
# send_emails()
# end = time.time()
# duration = end - start
# print(duration)


#Course 6.9: Working with DateTimes

# from datetime import datetime
# import time

# dt1 = datetime(2018, 1, 1)
# dt2 = datetime.now()
# dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
# dt =datetime.fromtimestamp(time.time())
# print(dt)

# print(f"{dt.year}/{dt.month}")
# print(dt.strftime("%Y/%m"))

# print(dt2 > dt1)


#Course 6.10: Working with Time Deltas

# from datetime import datetime, timedelta

# dt1 = datetime(2018, 1, 1) + timedelta(days=1, seconds=1000)
# print(dt1)
# dt2 = datetime.now()

# duration = dt2 - dt1
# print(duration)
# print("days", duration.days)
# print("seconds", duration.seconds)
# print("total_seconds", duration.total_seconds())


#Course 6.11: Generating Random Values

# import random
# import string

# print(random.random())
# print(random.randint(1, 10))
# print(random.choice([1, 2, 3, 4]))
# print(random.choices([1, 2, 3, 4], k=2))
# print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

# print(string.ascii_letters)
# print(string.digits)

# numbers = [1, 2, 3, 4]
# random.shuffle(numbers)
# print(numbers)


#Course 6.12: Opening the Browser

# import webbrowser

# print("Deployment completed")
# webbrowser.open("http://www.google.com")


#Course 6.13: Sending Emails

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# import smtplib

# message = MIMEMultipart()
# message["from"] = "George Manea"
# message["to"] = "textuser@cleancode.com"
# message["subject"] = "This is a test"
# message.attach(MIMEText("Body"))
# message.attach(MIMEImage(Path("george.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("textuser@cleancode.com", "todayskyisblue1234")
#     smtp.send_message(message)
#     print("Sent...")


#Course 6.14: Templates

# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.image import MIMEImage
# from pathlib import Path
# from string import Template
# import smtplib

# Template(Path("template.html").read_text())
# template.substitute(name="George")

# message = MIMEMultipart()
# message["from"] = "George Manea"
# message["to"] = "textuser@cleancode.com"
# message["subject"] = "This is a test"
# message.attach(MIMEText("Body", "plain"))
# body = template.substitute({"name": "John"})
# body = template.substitute(name="John")
# message.attach(MIMEText("html"))
# message.attach(MIMEImage(Path("george.png").read_bytes()))

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("textuser@cleancode.com", "todayskyisblue1234")
#     smtp.send_message(message)
#     print("Sent...")


#Course 6.15: Command-line Arguments

# import sys

# # print(sys.argv)
# if len(sys.argv) == 1:
#     print("USAGE: python Course6/course6.py <password>")
# else:
#     password = sys.argv[1]
#     print("Password", password)


#Course 6.16: Running External Programs

# import subprocess

# try:
#     completed = subprocess.run(["false"], 
#                             capture_output=True,
#                             text=True)
#     print("args", completed.args)
#     print("returncode", completed.returncode)
#     print("stderr", completed.stderr)
#     print("stdout", completed.stdout)
#     if completed.returncode != 0:
#         print(completed.stderr)
# except subprocess.CalledProcessError as ex:
#     print(ex)
# print(type(result))
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen