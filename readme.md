# OpenAI Moderation API Demo

A simple Streamlit web application that demonstrates the OpenAI Moderation API functionality. This tool allows you to test text content for various categories of potentially harmful content.

## Features

- Real-time text moderation using OpenAI's `omni-moderation-latest` model
- Visual representation of category scores with bar charts
- Detailed results table with score breakdown
- Simple and intuitive web interface

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MaximilianRogath/OpenAI-API-Moderation-Demo.git
   cd openai-moderation-demo
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Copy `.env.example` to `.env`
   - Add your OpenAI API key to the `.env` file:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## Usage

1. **Start the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser** and navigate to `http://localhost:8501`

3. **Enter text** in the input field and click "Moderate Text"

4. **View results** including flagged status and category scores

## API Categories

The OpenAI Moderation API checks for the following content categories:

- **harassment** - Content that expresses, incites, or promotes harassing language
- **harassment/threatening** - Harassment content that also includes violence or serious harm
- **hate** - Content that expresses, incites, or promotes hate based on protected characteristics
- **hate/threatening** - Hateful content that also includes violence or serious harm
- **illicit** - Content that gives advice on committing illicit acts
- **illicit/violent** - Illicit content that includes references to violence
- **self-harm** - Content that promotes, encourages, or depicts acts of self-harm
- **self-harm/intent** - Content where the speaker expresses intent to engage in self-harm
- **self-harm/instructions** - Content that gives instructions on how to commit self-harm
- **sexual** - Content meant to arouse sexual excitement
- **sexual/minors** - Sexual content that includes minors
- **violence** - Content that depicts death, violence, or physical injury
- **violence/graphic** - Violent content depicted in graphic detail

## Requirements

- Python 3.7+
- OpenAI API key
- Internet connection

## Disclaimer

This tool is for demonstration purposes only. Always review OpenAI's usage policies and ensure compliance with applicable laws and regulations when implementing content moderation in production applications.
