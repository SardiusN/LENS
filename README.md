\# LENS - Logical Exploration and Navigation System



LENS is an AI-powered virtual assistant developed as part of our Artificial Intelligence Lab assignment.



The main idea behind LENS is to help users think through questions rather than simply provide ready-made answers. It focuses on breaking down questions, examining assumptions, exploring different perspectives, and arriving at well-reasoned conclusions.



\## Features



\- \*\*AI-powered responses:\*\* Uses the Groq API to generate responses to user questions.

\- \*\*Critical thinking:\*\* Examines assumptions, considers different perspectives, and presents counterarguments where relevant.

\- \*\*Conversational interaction:\*\* Maintains conversation context so users can ask follow-up questions.

\- \*\*Voice input:\*\* Allows users to ask questions using their microphone. Speech is converted into text using Faster-Whisper.

\- \*\*Text-to-speech:\*\* Can read AI-generated responses aloud.

\- \*\*Simple interface:\*\* Built using Streamlit with a clean, dark-themed design.



\## Technologies Used



\- Python

\- Streamlit

\- Groq API

\- Faster-Whisper

\- pyttsx3

\- Python-dotenv



\## Project Structure



```text

LENS/

│

├── app.py

├── config.py

├── requirements.txt

├── .env.example

├── .gitignore

├── README.md

│

├── core/

│   ├── \_\_init\_\_.py

│   ├── groq\_client.py

│   ├── assistant.py

│   └── prompts.py

│

├── voice/

│   ├── \_\_init\_\_.py

│   ├── speech\_to\_text.py

│   └── text\_to\_speech.py

│

├── utils/

│   └── session.py

│

└── assets/

&#x20;   └── styles.css

```



\## Installation and Setup



\### 1. Clone the repository



```bash

git clone https://github.com/YOUR\_USERNAME/LENS.git

cd LENS

```



\### 2. Create a virtual environment



```bash

python -m venv venv

```



Activate it on Windows:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



\### 3. Install the required dependencies



```bash

pip install -r requirements.txt

```



\### 4. Configure the API key



Create a file named `.env` in the project's root directory.



Add your Groq API key:



```env

GROQ\_API\_KEY=your\_groq\_api\_key\_here

```



You can obtain an API key from \[Groq Console](https://console.groq.com/).



\### 5. Run the application



```bash

streamlit run app.py

```



The application will open in your default browser.



\## How It Works



LENS uses a system prompt to guide the AI's behaviour and response style.



When a user submits a question, the application sends it along with the relevant conversation history to the Groq API. The model generates a response based on the instructions defined for LENS.



For questions that require deeper exploration, LENS follows a structured approach:



1\. Understanding the question

2\. Breaking it down

3\. Examining assumptions

4\. Exploring different perspectives

5\. Considering counterarguments and limitations

6\. Arriving at a reasoned conclusion



Voice input is handled using Faster-Whisper, while pyttsx3 is used to convert generated responses into speech.



\## Limitations



\- An active internet connection is required for AI response generation.

\- A valid Groq API key is required.

\- Conversation history is maintained within the current application session and is not permanently stored.

\- Speech recognition and text-to-speech performance may depend on the system and available resources.



\## Author



Developed by Sardius(2025KUAD3030)

As an Artificial Intelligence Lab assignment.

