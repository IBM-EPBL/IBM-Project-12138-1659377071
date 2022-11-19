import wiotp.sdk.device
import time
import random
import playsound
from datetime import datetime
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
myConfig = {
    "identity": {
        "orgId": "jwl2wf",
        "typeId": "SalmanDevice",
        "deviceId": "SalmanDevice_1"
    },
    "auth": {
        "token": "e3DwTZGGA1Y?0BD*s9"
    }
}


def myCommandCallback(cmd):
    print("Message received from IBM IoT Platform: %s" % cmd.data['command'])
    m = cmd.data['command']
    if (m == "Medicine Taken"):
    print("Medicine Intaken\nThank You!!")
    else:
    print("*****")
    print("Take Your Medicine")
    print("******")


client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
authenticator = IAMAuthenticator(
    'mc6GkVtcmmR8o5UlAk5-jhyvsmieCN8nhJ-Xc7awmRly')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)
text_to_speech.set_service_url(
    'https://api.eu-gb.text-tospeech.watson.cloud.ibm.com/instances/2ff7f2d9-da46-4f46-bbda-fad6e9f83882')
now = datetime.now()
current_time = now.strftime("%H:%M")
print("Current Time =", current_time)
while True:
    with open('z.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'take your respected medicine',
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'
        ).get_result().content)
    client.publishEvent(eventId="test", msgFormat="json",
                        data="z.mp3", qos=0, onPublish=None)
    client.commandCallback = myCommandCallback
client.disconnect()
