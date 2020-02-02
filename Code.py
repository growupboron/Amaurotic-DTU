import logging
import os

from flask import Flask
from flask_ask import Ask, request, session, question, statement
import RPi.GPIO as GPIO


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

@ask.launch
def launch():
    speech_text = 'Welcome to Amaurotic. Your very own personal braille reader.'
    #os.system("python Code.py")
    return question(speech_text).reprompt(speech_text).simple_card(speech_text)

@ask.intent('BookIntent')
def Object_Intent():
    os.system("python list_files.py")
    f=open('/home/pi/Desktop/Amaurotic-DTU/book/book_list.txt','r')
    message=f.read()
    return statement(message)
    f.close()
    

@ask.intent('NavIntent',mapping= {'destination':'destination'})
def Nav_Intent(destination):
    dest=destination
    os.system("python navi_test.py")
    f=open('dir.txt','r')
    message=f.read()
    return statement(message)
    f.close()

 
        
    
 
@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can say hello to me!'
    return question(speech_text).reprompt(speech_text).simple_card('HelloWorld', speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True)

os.system("python ms_visionapi.py")
