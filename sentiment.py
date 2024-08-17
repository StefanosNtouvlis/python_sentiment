from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr
import tkinter as tk
from PIL import Image, ImageTk

# Function to display the GUI with an image and a message
def display_gui(message, image_path):
    window = tk.Tk()
    window.title("Sentiment Analysis Result")
    window.geometry("500x500")  # Set the window size

    # Load and display the image
    img = Image.open(image_path)
    img = img.resize((400, 400), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality downsampling
    photo = ImageTk.PhotoImage(img)
    label_img = tk.Label(window, image=photo)
    label_img.pack()

    # Display the message
    label_msg = tk.Label(window, text=message, font=("Helvetica", 16))
    label_msg.pack()

    # Add a close button
    close_button = tk.Button(window, text="Close", command=window.destroy, font=("Helvetica", 12))
    close_button.pack()

    window.mainloop()

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Clearing background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for your message...')
    recordedaudio = recognizer.listen(source)
    print('Done recording...')

    try:
        print('Processing message...')
        text = recognizer.recognize_whisper(recordedaudio, language='en')
        print('Your message: {}'.format(text))

        analyser = SentimentIntensityAnalyzer()
        sentiment = analyser.polarity_scores(text)
        print(sentiment)

        neg = sentiment['neg']
        neu = sentiment['neu']
        pos = sentiment['pos']

        if neg > pos and neg > neu:
            display_gui("Your message was rather negative, sir.", "negative.png")
        elif pos > neg and pos > neu:
            display_gui("Your message was quite positive, sir.", "positive.jpeg")
        else:
            display_gui("You were delightfully neutral.", "neutral.png")

    except Exception as ex:
        print("Error: Could not process the audio. Reason:", ex)
