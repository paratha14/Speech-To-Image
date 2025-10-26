# Speech-To-Image Generator

A powerful application that converts spoken descriptions into engineering-style blueprints using speech recognition and AI image generation. Speak your ideas, and watch them transform into technical drawings!

## Features

- **Speech Recognition**: Captures and transcribes your voice in real-time
- **Audio Signal Analysis**: Visualizes your speech through:
  - Time-domain waveform
  - Frequency spectrum (FFT)
  - Spectrogram
- **AI Blueprint Generation**: Transforms your spoken description into engineering-style blueprints using Stable Diffusion
- **Interactive Web Interface**: User-friendly Streamlit dashboard

## Prerequisites

- Python 3.8 or higher
- A working microphone
- Hugging Face account (free)
- Internet connection

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/paratha14/Speech-To-Image.git
cd Speech-To-Image
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Setting Up Hugging Face Token

### Step 1: Create a Hugging Face Account

1. Go to [https://huggingface.co/join](https://huggingface.co/join)
2. Sign up for a free account
3. Verify your email address

### Step 2: Generate an Access Token

1. Log in to your Hugging Face account
2. Click on your profile picture in the top-right corner
3. Go to **Settings** → **Access Tokens**
4. Click on **New token**
5. Give your token a name (e.g., "Speech-To-Image")
6. Select **Read** access (sufficient for this project)
7. Click **Generate token**
8. **Copy the token immediately** (you won't be able to see it again)

### Step 3: Create the .env File

1. In the root directory of the project (`Speech-To-Image`), create a file named `.env`

**Windows (PowerShell):**
```powershell
New-Item -Path .env -ItemType File
```

**macOS/Linux:**
```bash
touch .env
```

2. Open the `.env` file in a text editor and add your token:

```plaintext
HUGGINGFACE_TOKEN=hf_your_token_here
```

Replace `hf_your_token_here` with the actual token you copied from Hugging Face.

3. Save the file

**Important Notes:**
- Never share your `.env` file or commit it to GitHub
- Add `.env` to your `.gitignore` file to prevent accidental uploads
- The token should start with `hf_`

## Running the Application

### Start the Streamlit Server

**Option 1: Using PowerShell/Command Prompt**
```powershell
streamlit run speech.py
```

**Option 2: Using Python Module**
```powershell
python -m streamlit run speech.py
```

The application will automatically open in your default web browser at `http://localhost:8501`

### Stop the Server

Press `Ctrl + C` in the terminal to stop the Streamlit server.

## How to Use

1. **Start the Application**: Run the Streamlit server as described above
2. **Click "Tap to Speak"**: The application will start listening through your microphone
3. **Speak Your Description**: Clearly describe what you want to design
   - Example: "a modern bridge design"
   - Example: "a two-story house with a garage"
   - Example: "a futuristic car"
4. **View Audio Analysis**: See the visualization of your speech signal
5. **Wait for Blueprint**: The AI will generate an engineering-style blueprint
6. **Download or View**: Your generated blueprint will be displayed on the screen

## Troubleshooting

### "HUGGINGFACE_TOKEN not found" Error
- Verify that your `.env` file exists in the project root directory
- Check that the token is correctly formatted: `HUGGINGFACE_TOKEN=hf_...`
- Ensure there are no extra spaces or quotes around the token

### Streamlit Command Not Found
- Make sure your virtual environment is activated
- Try reinstalling streamlit: `pip install --upgrade streamlit`
- Use the full path: `python -m streamlit run speech.py`

### Image Generation is Slow
- First-time usage downloads the Stable Diffusion model (~6GB)
- Subsequent generations will be faster
- Generation time depends on your internet speed and API response time

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

**paratha14**

## Acknowledgments

### Team Members

This project was developed by:
- **Pratham Mohan**
- **Aayushmaan Saksena**
- **Durgesh Yadav**
---

**Note**: This application requires an active internet connection for both speech recognition (Google API) and image generation (Hugging Face API).
