import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

print("Say something...")

with sr.Microphone() as source:
    audio = r.listen(source)  # Listen for user speech

try:
    text = r.recognize_google(audio)     # Convert speech to text
    print("You said: " + text)           # Display the recognized text
    # Send recognized text to image generation function/module here
except sr.UnknownValueError:
    print("Sorry, could not understand audio.")
except sr.RequestError as e:
    print(f"Could not request results; {e}")