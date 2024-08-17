from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Clearing background noise...")
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print('Waiting for your message...')
    recordedaudio = recognizer.listen(source)
    print('Done recording...')

    try:
        print('Printing message...')
        text = recognizer.recognize_whisper(recordedaudio, language='en')
        print('Your message: {}'.format(text))

        Sentence = [text]
        analyser = SentimentIntensityAnalyzer()
        for i in Sentence:
            v = analyser.polarity_scores(i)
            print(v)
        
        neg = v['neg']
        neu = v['neu']
        pos = v['pos']

        if neg > pos and neg > neu:
            print("Your message was rather negative sir")
        elif pos > neg and pos > neu:
            print("Your message was quite positive sir")
        else:
            print("Your were delightfully neutral")

    except Exception as ex:
        print("Error: Could not process the audio. Reason:", ex)
