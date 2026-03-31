#Course 7.1: Pip

# To install a package using pip, you can use the following command in your terminal:
# pip install package_name
# For example, to install the requests library, you would run:
# pip install requests
# Once you have installed the package, you can import it in your Python code and use its functionality. For example:

# import requests

# response = requests.get("http://www.google.com")
# print(response)


#Course 7.2: Virtual Environments

# A virtual environment is a self-contained directory that contains a Python installation and its own set of packages. It allows you to manage dependencies for different projects without conflicts. To create a virtual environment, you can use the following command in your terminal:
# python -m venv myenv
# This will create a virtual environment named "myenv". To activate the virtual environment, you
# can use the following command:
# On Windows:
# source myenv/bin/activate
# Once the virtual environment is activated, you can install packages using pip, and they will be isolated from the global Python installation. To deactivate the virtual environment, you can use the following command:
# deactivate


#Course 7.3 Pipenv

# Pipenv is a tool that combines pip and virtualenv to manage dependencies for Python projects. It provides a simple way to create and manage virtual environments, as well as to specify and install project dependencies. To use Pipenv, you can follow these steps:
# 1. Install Pipenv using pip:
# pip install pipenv
# 2. Navigate to your project directory and create a Pipenv environment:
# pipenv install
# This will create a Pipenv environment and a Pipfile to manage your dependencies. You can then install packages using pipenv:
# pipenv install package_name
# For example, to install the requests library, you would run:
# pipenv install requests
# Once you have installed the packages, you can run your Python code within the Pipenv environment using:
# pipenv run python your_script.py
# To deactivate the Pipenv environment, you can simply exit the terminal or use:
# exit


#Course 7.4: Virtual Environments with VSCode

import requests

response = requests.get("http://www.google.com")
print(response)