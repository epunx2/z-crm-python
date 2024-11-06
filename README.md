# Zoho CRM Python Library
This is a Python library for using the Zoho API's. This will house all the code for the Zoho API's. This includes OAuth2 authentication, Zoho CRM, Zoho Books, Zoho Desk, Zoho Analytics

### What it does ###
1. Has classes for the different Zoho apps
2. Has a module for OAuth2 authentication that is inherited by the Zoho classes
3. Has some samples for using the Zoho classes
4. Has examples for using with AWS Lambda
5. Has examples for using with Google Cloud Run functions
6. Has directions for deploying to AWS and Google for both GitHub and BitBucket

## How do I get set up? ##

### Mac ###
1. Install Python with brew
   ```bash
   $ brew search python
   $ brew install python3.13
   ```
2. Install virtual environment tool:
    ```bash
    $ brew install venv
    ```
3. Setup virtual environment:
    ```bash
    $ python3.13 -m venv env
    $ source env/bin/activate
    ```
4. Clone repo:
    ```bash
    $ git clone https://github.com/epunx2/z-crm-python.git
  '''
5. Install packages
    ```bash
    $ pip install package-name
    ```
6. Generate requirements.txt
    ```bash
    $ pip freeze > requirements.txt
    ```
