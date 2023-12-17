
# HablaClara - Speak and Translate

Welcome to **HablaClara**, a real-time speech-to-text translation app that bridges language barriers by translating spoken Spanish into written English. Inspired by the vibrant culture of the Dominican Republic, HablaClara is designed to be fun, user-friendly, and efficient.

## Features

-   **Real-time Translation**: Converts spoken Spanish into written English in real-time.
-   **Continuous Listening**: Keeps listening and translating continuously.
-   **Cultural Charm**: Inspired by the lively and colorful Dominican culture.

## Getting Started

### Prerequisites

-   Python 3.x
-   Linux environment (Tested on Chromebook's Linux Beta)
-   Internet connection
-   Microphone

### Installation

1.  Clone the repository or download the source code.
2.  Install required dependencies:
    
    Copy code
    
    `pip install -r requirements.txt` 
    

### Usage

1.  Set your OpenAI API key as an environment variable:
    
    arduinoCopy code
    
    `export OPENAI_API_KEY='your_api_key_here'` 
    
2.  Run the app:
    
    cssCopy code
    
    `python main.py` 
    
3.  Speak in Spanish and watch the app translate your speech into English text in real-time.

## Troubleshooting

-   **PyAudio Installation Issue**: If you encounter "Failed to build PyAudio" error, install `portaudio19-dev` before installing PyAudio:
    
    arduinoCopy code
    
    `sudo apt-get install portaudio19-dev python-pyaudio python3-pyaudio
    pip install pyaudio` 
    
-   **OpenAI API Changes**: If you get an error related to `openai.Completion`, ensure you're using the latest OpenAI API version and update your translation function according to the new API structure.

## Contributing

Feel free to fork the repository, make improvements, and open pull requests. We appreciate your contributions to make HablaClara even better!

## License

This project is licensed under the MIT License - see the [LICENSE.md](/LICENSE.md) file for details.

----------

This README provides a concise yet comprehensive overview of your app, ensuring users have all the information they need to get started. Feel free to modify or expand it as necessary!
