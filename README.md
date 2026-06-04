# Voice Assistance Using Python With Gemini

I am creating voice assistance with integration of Google's Gemini and Python's Library.

## 📋 Overview

This project provides a voice assistant that leverages Google's Gemini API to process and respond to voice inputs. The assistant can understand natural language voice commands and provide intelligent responses powered by Google's advanced AI model.

## ✨ Features

- **Voice Input Processing**: Accept and process voice commands from users
- **Google Gemini Integration**: Uses Google's Gemini API for intelligent responses
- **Multiple API Support**: Adaptations for both OpenAI and Google Gemini APIs
- **Python-based**: Built with Python for simplicity and flexibility
- **Natural Language Understanding**: Process complex voice commands naturally

## 🔑 API Setup

### Google Gemini API
- Get your API key from: https://aistudio.google.com/
- Free tier available for development and testing
- Recommended for this project

### OpenAI API
- Get your API key from: https://platform.openai.com/api-keys
- Alternative implementation also provided in this project

## 🚀 Installation

1. Clone the repository
```bash
git clone https://github.com/orignlkartik1/Voice-Assistance-Using-Python-With-Gemini.git
cd Voice-Assistance-Using-Python-With-Gemini
```

2. Install required dependencies
```bash
pip install -r requirements.txt
```

3. Set up your API keys
   - For Gemini: Set `GEMINI_API_KEY` environment variable
   - For OpenAI: Set `OPENAI_API_KEY` environment variable

## 📝 Usage

### Using Google Gemini API
```python
# Example usage with Gemini
python voice_assistant_gemini.py
```

### Using OpenAI API
```python
# Example usage with OpenAI
python voice_assistant_openai.py
```

## 📦 Requirements

- Python 3.7+
- google-generativeai
- openai
- SpeechRecognition
- pyttsx3 (or similar text-to-speech library)

## 🛠️ Technologies Used

- **Python**: Core language
- **Google Gemini API**: AI model for intelligent responses
- **OpenAI API**: Alternative AI implementation
- **SpeechRecognition**: Voice input processing
- **Text-to-Speech**: Voice output generation

## 📄 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest improvements and new features
- Submit pull requests with enhancements

## 📞 Support

For issues, questions, or suggestions, please open an issue on the GitHub repository.

---

**Note**: Both Gemini and OpenAI API adaptations are provided in this project. Please read the code comments carefully to understand the implementation of each API approach.
