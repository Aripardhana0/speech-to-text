# Text-to-Speech Program

This repository contains a simple Python program that demonstrates text-to-speech conversion using the `gTTS` (Google Text-to-Speech) library. The program takes a predefined text and converts it into an audio file, which is then played.

## Requirements

- Python 3.x
- `gTTS` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/text-to-speech.git
    cd text-to-speech
    ```

2. Install the `gTTS` library:
    ```sh
    pip install gtts
    ```

## Usage

1. Create and run the Python script:

    ```python
    from gtts import gTTS
    import os

    # Providing the text
    input_text = "Hello, I am the first program. In this program, you will convert the text within this program into speech. In the second program, you will convert the text from a .txt file into speech."

    # Setting the language
    language = "en"

    # Passing the text to the gTTS engine
    voice = gTTS(text=input_text, lang=language, slow=False)

    # Creating and saving the audio file
    voice.save("first.mp3")

    # Playing the file
    os.system("start first.mp3")
    ```

2. Run the script:
    ```sh
    python script_name.py
    ```

    Replace `script_name.py` with the name of your Python script file.

## Example

The provided example script demonstrates how to convert a hardcoded text into speech and save it as an `MP3` file, which is then played automatically. You can modify the `input_text` variable to change the text that will be converted into speech.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
