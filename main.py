from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger()

def lambda_handler(event, context):

  response = main_fun()
  return response

def main():
  print("Hello World")

if __name__ == '__main__':
    main()
