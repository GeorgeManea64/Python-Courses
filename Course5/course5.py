#Course 5.1: Creating Modules

# from sales import calc_shipping, calc_tax
# import sales

# sales.calc_shipping()

# calc_shipping()
# calc_tax()


#Course 5.2: Compiled Python Files

#Running the Python program will generate a cache folder of your module file which contains binary words in it.


#Course 5.3: Module Search Path

# import sales
# import sys

# print(sys.path)


#Course 5.4: Packages

# from ecommerce.sales import calc_tax, calc_shipping
# from ecommerce import sales 

# ecommerce.sales.calc_tax()
# calc_tax


#Course 5.5: Sub-Packages

# from ecommerce.shopping import sales


#Course 5.6: Intra-package References

#Edits are in the sales.py file


#Course 5.7: The dir Function

# from ecommerce.shopping import sales

# # print(dir(sales))
# print(sales.__name__)
# print(sales.__package__)
# print(sales.__file__)


#Course 5.8: Executing Modules as Scripts

# from ecommerce.shopping import sales