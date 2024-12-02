import os
import zoho_api as Zoho

class ZohoCrmApi(Zoho):
  def __init__(self):
    token = self.refresh_access_tokens(os.getenv('CLIENT_ID'))
    self.headers = {'Authentication': f'Zoho-oauthtoken {token}'}
    return self
