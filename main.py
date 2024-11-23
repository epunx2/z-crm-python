# from dotenv import load_dotenv
import logging

# load_dotenv()

logger = logging.getLogger()

def lambda_handler(event, context):
  response = process()
  return response

def process():
  return "Hello World"

def main():
  response = process()
  return response

if __name__ == '__main__':
    main()
