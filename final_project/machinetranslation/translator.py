''' Module providing translation from english to french and vice versa '''
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
translator.set_service_url(url)

def english_to_french(english_text=None):
    ''' A function that traslates text from english to french'''
    #write the code here
    try:
        french_text = translator.translate(english_text, model_id='en-fr').get_result()
    except ApiException:
        return None
    except ValueError:
        return None
    else:
        return french_text['translations'][0]['translation']

def french_to_english(french_text=None):
    ''' A function that translates text from french to english'''
    #write the code here
    try:
        english_text = translator.translate(french_text, model_id='fr-en').get_result()
    except ApiException:
        return None
    except ValueError:
        return None
    else:
        return english_text['translations'][0]['translation']
