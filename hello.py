import requests

def get_respnse() -> int:
    return requests.get('http://www.google.com/').status_code
