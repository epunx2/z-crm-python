import os
import requests
import logging

class Zoho:
  def __init__(self):
    self.conn = requests.Session()

  def refresh_access_tokens(refresh_token):
    _client_id_ = os.getenv('CLIENT_ID')
    _client_secret_ = os.getenv('CLIENT_SECRET')

    refresh_url = f'https://accounts.zoho.com/oauth/v2/token?refresh_token={refresh_token}&client_id={_client_id_}&client_secret={_client_secret_}&grant_type=refresh_token'
    try:
      refresh_request = requests.post(refresh_url).json()
      token = refresh_request['access_token']
      logging.info('Zoho access Token received')
      return token
    except Exception as e:
      logging.critical("Zoho access Token not received due to error | {}".format(e))

  def api_call(url, type, payload = None):
    api_url = f'{self.base_url}{url}'
    try:
      match type:
        case 'get':
          response = self.conn.get(api_url,payload)
        case 'post':
          response = self.conn.post(api_url,payload)
        case 'put':
          response = self.conn.put(api_url,payload)
        case 'delete':
          response = self.conn.delete(api_url,payload)
      data = response.body
      logging.info(data)
      logger.info(f"Zoho {type} to {api_url} successful")
      return data
    except Exception as e:
      logging.critical(f"Zoho {type} to {api_url} failed")
      logger.debug(e.response[status])
      logger.debug(e.response[body])
      return 'fail'
