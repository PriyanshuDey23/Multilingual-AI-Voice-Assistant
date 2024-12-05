
# Multilingual-AI-Voice-Assistant

A robust multilingual AI voice assistant designed for seamless language processing, voice interaction, and translation. This application leverages cutting-edge technologies to deliver accurate and efficient multilingual support.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
- [Tech Stack](#tech-stack)
- [License](#license)

---

## Overview
The **Multilingual-AI-Voice-Assistant** provides language translation, voice interaction, and processing capabilities using advanced tools like Google APIs and Gemini AI. With a user-friendly interface powered by Streamlit, the application ensures smooth interaction and adaptability for diverse use cases.

---

## Features
- **Multilingual Support**: Process and translate multiple languages with precision.
- **Speech-to-Text (s2t)**: Convert speech input into text effortlessly.
- **Text-to-Speech (t2s)**: Generate speech output from text inputs.
- **Streamlit UI**: Easy-to-use and interactive interface.
- **API Integration**: Utilizes Google API for enhanced translation and language support.

---

## Setup Instructions

### Step 1: Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/PriyanshuDey23/Multilingual-AI-Voice-Assistant.git

```

### Step 2: Create a Conda Environment
Set up a virtual environment to manage dependencies:
```bash
conda create -n llmapp python=3.10 -y

conda activate llmapp
```

### Step 3: Install Dependencies
Install all required Python libraries:
```bash
pip install -r requirements.txt
```

### Step 4: Configure API Keys
Create a `.env` file in the root directory to store your API credentials:
```ini
GOOGLE_API_KEY="your_google_api_key"
```

### Step 5: Run the Application
Start the Streamlit application:
```bash
streamlit run app.py
```

Access the application in your browser at:
```bash
http://localhost:8501
```

---

## Tech Stack
- **Python**: Core programming language.
- **Google API**: Integration for language translation and processing.
- **Streamlit**: Framework for creating the web interface.
- **Gemini AI**: Advanced language model for processing.
- **Speech-to-Text (s2t)**: Converts spoken input to text.
- **Text-to-Speech (t2s)**: Converts text input to speech output.

---

## License
This project is licensed under the [MIT License](LICENSE).

---

### Contributing
We welcome contributions to improve the **Multilingual-AI-Voice-Assistant**! Feel free to fork the repository and submit pull requests. For significant changes, please open an issue first to discuss your proposed modifications.
