import pyttsx3

def test_tts():
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Set speaking speed
        engine.setProperty('volume', 1.0)  # Set volume
        engine.say("This is a test of the text-to-speech functionality.")
        engine.runAndWait()
    except Exception as e:
        print(f"Error: {e}")

test_tts()
