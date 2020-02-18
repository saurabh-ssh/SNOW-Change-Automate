# SNOW-Change-Automate
Python script (with selenium) to automate the similar change creation in Service Now Tool. 

This script uses Python with selenium to automate Change creation in Service-Now(SNOW) Tool.
Replace <prod_url> with your production URL "https://<prod_url>.service-now.com".
Replace <your_SNOW_email_address> with your email id you use to login SNOW Tool
Replace <your_SNOW_email_password> with your password.

Currently the script can create one CHANGE per execution, but can be modified to create multiple CHANGE's in one execution(Work in Progress).
The script will take data from SNOW_Variables.py(attached) module to input data into CHANGE fields.
The data to be sent in fields can be changed manually or dynamically (Work in Progress)

Required:
Python-3.8.* (Add to PATH variable)
Selenium (pip install selenium)
Firefox Latest preferable
geckodriver (Also add to PATH variable)

Please reach out to me at hingmiresaurabh@gmail.com if any issue arises. I would love to help.
