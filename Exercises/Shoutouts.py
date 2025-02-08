# Using pywin32 to send a shoutout to the user

import win32com.client
def pronounce_names(names_list):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    for name in names_list:
        message = f"Hello {name}, welcome to the Python world!"
        print(message)
        speaker.Speak(message)

Names_list_toShoutout = ["Vaibhav" , "Vaishanvi" , "toto"]


pronounce_names(Names_list_toShoutout)