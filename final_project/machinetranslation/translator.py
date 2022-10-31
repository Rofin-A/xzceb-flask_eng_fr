"""Translate text using IBM Watson LanguageTranslatorV3"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version = '2018-05-01',
    authenticator = authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """This method translates the provided english text to french"""
    #write the code here
    if english_text is not None: #invoke tranlation only if not null
        translation= language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text=translation['translations'][0]['translation']
    else:
        french_text = None
    return french_text

def french_to_english(french_text):
    """This method translates the provided French text to English"""
    #write the code here
    if french_text is not None: #invoke tranlation only if not null
        translation= language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text=translation['translations'][0]['translation']
    else:
        english_text= None
    return english_text