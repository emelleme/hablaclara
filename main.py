import os
import time
import speech_recognition as sr
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Function to translate text using OpenAI's GPT model
def translate_text(text, source_lang="es", target_lang="en"):
    try:
        prompt = f"Translate this from {source_lang} to {target_lang}: {text}"
        response = client.completions.create(model="text-davinci-003",
        prompt=prompt,
        max_tokens=60)
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred during translation: {e}")
        return None

# Function to continuously listen and process audio
def continuous_listen():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        # Adjust for ambient noise and set listening sensitivity
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        while True:
            try:
                print("\nListening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                print("Processing...")

                # Convert speech to text (Spanish)
                spanish_text = recognizer.recognize_google(audio, language="es-ES")
                print(f"Recognized Spanish Text: {spanish_text}")

                # Translate text to English
                translated_text = translate_text(spanish_text)
                if translated_text:
                    print(f"Translated Text: {translated_text}")
                else:
                    print("Translation failed.")

                # Short pause before next listening loop
                time.sleep(1)

            except sr.WaitTimeoutError:
                print("No speech detected, listening again...")
            except sr.UnknownValueError:
                print("Could not understand the audio.")
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
      # Set your OpenAI API key here
    continuous_listen()
