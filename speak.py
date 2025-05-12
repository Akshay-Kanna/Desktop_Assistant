import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")

while(1):
    print("Enter the word you want to speak:")
    s = input()
    speaker.speak(s)