# Speech-to-Text Sentiment Analyzer

This project is a **Speech-to-Text Sentiment Analyzer** that captures audio input from the microphone, converts it to text using the Whisper speech recognition model, and then analyzes the sentiment of the transcribed text using the VADER Sentiment Analysis tool. The sentiment is categorized as **POSITIVE**, **NEGATIVE**, or **NEUTRAL** based on the analysis.

## Features

- **Real-time Audio Capture**: Captures audio directly from your microphone.
- **Speech Recognition**: Converts speech to text using the Whisper model.
- **Sentiment Analysis**: Analyzes the sentiment of the transcribed text using VADER.
- **Classification**: Outputs whether the sentiment is POSITIVE, NEGATIVE, or NEUTRAL.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/speech-to-text-sentiment-analyzer.git
    cd speech-to-text-sentiment-analyzer
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Ensure you have a working microphone setup.**

## Usage

1. **Run the script:**

    ```bash
    python sentiment.py
    ```

2. **Interact with the program:**
   - Speak into your microphone when prompted.
   - The script will process your speech, convert it to text, and analyze the sentiment.

3. **View the output:**
   - The text and sentiment analysis results will be printed to the console.

## Example Output

```bash
Clearing background noise...
Waiting for your message...
Done recording...
Printing message...
Your message: This project is amazing!
{'neg': 0.0, 'neu': 0.28, 'pos': 0.72, 'compound': 0.8476}
POSITIVE
