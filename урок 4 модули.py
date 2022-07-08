"""import requests
import pprint
from requests import get, utils


URL = 'http://www.cbr.ru/scripts/XML_daily.asp'
rp = requests.get(URL)
print(type(rp))
encodings = utils.get_encoding_from_headers(rp.headers)
content = rp.content.decode(encoding=encodings)
pprint.pprint(content)
rec={content['Valute']['USD']['Value']}
print(rec)
"""

