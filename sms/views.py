from django.shortcuts import render
from twilio.rest import Client
from sms_trail import settings
import speech_recognition as sr


def home(request):
    return render(request, 'index.html', {})

def sms(request):

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(to='+917206755167', from_='#', body='hey there , This is Gourav Here')

    print(message.sid)

    return render(request, 'thankyou.html')

def speech(request):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say something..............')
        r.adjust_for_ambient_noise(source, duration=1)
        r.dynamic_energy_threshold = True
        audio = r.listen(source)
        print('time up')

    try:
        print('text: ' + r.recognize_google(audio))
        value = r.recognize_google(audio)

        if str is bytes:
            result = u"{}".format(value).encode("utf-8")

        else:
            result = "{}".format(value)

        with open("outputs.txt", "a") as f:
            f.write(result)
    except:
        print('not recognise')

