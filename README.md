# Dyno Assistant

This project is a voice-controlled virtual assistant named Dyno, capable of performing various tasks such as telling the time and date, sending emails, fetching information from Wikipedia, and more.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use Dyno, you need to install the necessary dependencies. You can install them using pip:

```bash
pip install pyttsx3 SpeechRecognition wikipedia smtplib webbrowser psutil pyjokes pyautogui
```

## Features

- **Time and Date**: Tells the current time and date.
- **Email**: Sends emails to specified addresses.
- **Wikipedia**: Fetches summaries from Wikipedia.
- **System Status**: Provides CPU usage and battery status.
- **Jokes**: Tells jokes using the `pyjokes` library.
- **Screenshots**: Takes and saves screenshots.
- **Web Browsing**: Opens web pages and performs searches in browsers.
- **Media Control**: Plays music and videos from local directories.
- **Notes**: Takes and reads notes.
- **Reminders**: Sets and recalls reminders.
- **News**: Reads top headlines from the news.
- **Location**: Finds locations on Google Maps.
- **Calculations**: Performs calculations using WolframAlpha.
- **System Commands**: Logs out, restarts, or shuts down the system.
- **Custom Greetings**: Greets the user and provides a brief introduction.

## Usage

Run the script using Python:

```bash
python dyno_assistant.py
```

Upon running, Dyno will greet you and await your commands. You can interact with Dyno using voice commands. Here are some example commands:

- "What time is it?"
- "Tell me the date."
- "Search Wikipedia for Python programming."
- "Send an email."
- "Tell me a joke."
- "Take a screenshot."
- "Play music."
- "Write a note."
- "Show notes."
- "What's the news?"
- "Where is New York?"
- "Calculate 5 plus 7."
- "Log out."
- "Restart."
- "Shut down."

## Dependencies

- `pyttsx3`
- `SpeechRecognition`
- `wikipedia`
- `smtplib`
- `webbrowser`
- `psutil`
- `pyjokes`
- `pyautogui`
- `wolframalpha`

You can install all dependencies using the following command:

```bash
pip install pyttsx3 SpeechRecognition wikipedia psutil pyjokes pyautogui wolframalpha
```

## Configuration

To configure the email functionality, you need to replace the placeholders in the `sendEmail` function with your actual email and password.

```python
server.login("your_email@gmail.com", "your_password")
```

Additionally, replace the WolframAlpha App ID with your own in the `wolframalphaID` variable.

```python
wolframalphaID = 'YOUR_WOLFRAMALPHA_APP_ID'
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Make sure to follow the existing code style and include appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
