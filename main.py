import logging
import sys
sys.path.append('helpers')
import helpers.zoho_crm_api as crm_api

def lambda_handler(event, context):
  response = process()
  return response

def process():
  return "Hello World"

def create_zoho_crm_client():
  z_crm_api = crm_api.ZohoCrmApi()
  logging.warning(z_crm_api)
  return z_crm_api

def main():
  response = process()
  return response

if __name__ == '__main__':
    main()
