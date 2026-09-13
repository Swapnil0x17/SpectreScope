# 🔊 SpectreScope CLI

### 🎧 Audio Spectrogram & Signal Analysis Tool

**Analyze • Visualize • Investigate**

SpectreScope CLI is a Python-based audio analysis tool designed for cybersecurity students, CTF players, digital forensics enthusiasts, and audio signal analysis learners.

It allows users to select an audio file from their computer, analyze its frequency content, generate a spectrogram, and save the visualization as a PNG image.

The tool is useful for exploring audio clues in authorized CTF challenges and learning how audio signals can be represented visually.

---

## ✨ Features

* 🎵 Audio file selection through a graphical file picker.
* 📊 Audio spectrogram generation using Short-Time Fourier Transform (STFT).
* 🌈 Frequency visualization with a color-coded spectrogram.
* ⏱️ Audio duration and sample rate information.
* 💾 Automatic PNG export of the generated spectrogram.
* 🔍 Visual inspection of unusual frequency patterns.
* 🖥️ Terminal-based execution with a simple analysis workflow.

## 🛠️ Technologies Used

| Technology | Purpose                                   |
| ---------- | ----------------------------------------- |
| Python     | Main programming language                 |
| Librosa    | Audio loading and signal processing       |
| NumPy      | Numerical operations and array processing |
| Matplotlib | Spectrogram visualization and PNG export  |
| Tkinter    | Audio file selection dialog               |

---

## 📦 Requirements

Before running the tool, make sure you have:

* Python 3.9 or newer.
* pip, Python's package installer.
* FFmpeg, if you want to process audio extracted from supported video formats.

---

## 🚀 Installation

### 1. Clone the repository

Open your terminal or PowerShell:

```bash
git clone https://github.com/Swapnil0x17/SpectreScope.git
```

Navigate into the repository:

```bash
cd SpectreScope
```

### 2. Create a virtual environment

A virtual environment keeps the project's Python dependencies separate from other Python projects.

**Windows — PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Windows — Command Prompt**

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

Install the Python libraries required by the script:

```bash
python -m pip install librosa numpy matplotlib
```

Tkinter is usually included with standard Python installations on Windows. On Linux, you may need to install it separately through your distribution's package manager.

For example, on Ubuntu or Debian:

```bash
sudo apt install python3-tk
```

If you plan to process video files, install FFmpeg using your operating system's package manager.

---

## 🖥️ Usage

### Run the tool

Replace `audio_analyzer.py` with the actual filename of your Python script.

```bash
python audio_analyzer.py
```

### Step 1 — Select an audio file

A file-selection window will appear.

Choose an audio file from your computer.

### Step 2 — Audio processing

The program loads the selected file and extracts the audio signal.

It displays basic information, including:

* Audio duration.
* Sample rate.

### Step 3 — Generate the spectrogram

The program calculates the Short-Time Fourier Transform (STFT) and converts the signal magnitude into decibel values.

It then generates a spectrogram showing frequency content over time.

### Step 4 — Save the output

The spectrogram is saved automatically as:

```text
spectrogram_output.png
```

The output image is saved in the program's current working directory.

The generated image is also displayed in a Matplotlib window.

---

## 📂 Supported File Types

The script's file picker is configured for the following formats:

| Category | Extensions                                                                                                |
| -------- | --------------------------------------------------------------------------------------------------------- |
| Audio    | WAV, MP3, FLAC, OGG, M4A, AAC                                                                             |
| Video    | MP4, MKV, AVI, WebM                                                                                       |
| Other    | All files can be selected, but successful processing depends on the installed decoders and file contents. |

**Important:** Selecting a file does not guarantee that it can be decoded. Video files require FFmpeg and a compatible audio stream. Files without a supported audio stream may fail.

---

## 🔬 Understanding the Spectrogram

A spectrogram is a visual representation of how the frequency content of a signal changes over time.

SpectreScope uses the Short-Time Fourier Transform (STFT) to divide the audio into short overlapping sections and calculate their frequency content.

The resulting visualization contains:

| Component       | Meaning                                    |
| --------------- | ------------------------------------------ |
| X-axis          | Time in seconds                            |
| Y-axis          | Frequency in hertz (Hz)                    |
| Color intensity | Relative signal magnitude in decibels (dB) |

### What can you investigate?

* Unusual frequency patterns.
* Repeated tones and signal sequences.
* Differences between quiet and loud sections.
* Potential visual clues in audio-based CTF challenges.

A spectrogram can help identify suspicious patterns, but it does not automatically decode hidden messages.

---

## 📁 Project Structure

The Python script can be organized as follows:

```text
SpectreScope/
│
├── app.py
├── spectrogram_output.png
├── README.md
└── .venv/
```

The `audio_analyzer.py` filename is an example. Use the actual filename present in your repository.

The PNG file is generated when the program successfully processes an audio file.

---

## ⚠️ Current Limitations

* The current script uses a graphical file picker rather than accepting a file path as a command-line argument.
* Hidden-text extraction and automated steganography detection are not implemented in the supplied script.
* The tool generates a static spectrogram rather than an interactive visualization.
* Video processing depends on FFmpeg and the availability of an audio stream.
* The generated PNG is saved in the current working directory, not necessarily beside the selected audio file.

---

## 🗺️ Future Improvements

Potential enhancements for future versions include:

* [ ] Command-line file path arguments.
* [ ] Configurable output filename and directory.
* [ ] Stereo channel separation.
* [ ] Audio filtering and reverse playback.
* [ ] Metadata extraction.
* [ ] Automated detection of unusual frequency patterns.
* [ ] Hidden-data detection and extraction modules.
* [ ] Batch audio processing.
* [ ] Exportable analysis reports.

These are planned improvements, not features currently implemented by the supplied script.

---

## 🔐 Responsible Use

SpectreScope is intended for educational purposes, authorized CTF challenges, and legitimate audio analysis.

Always ensure that you have permission to analyze the files you process.

---

## 🤝 Contributing

Contributions, bug reports, and feature suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement your changes.
4. Test your changes locally.
5. Submit a pull request with a clear description.

---

## 📜 License

Please refer to the repository's `LICENSE` file for the applicable license and terms of use.

---

## 👨‍💻 Author

**Swapnil0x17**

🔗 GitHub: [@Swapnil0x17](https://github.com/Swapnil0x17)

🔗 Repository: [SpectreScope](https://github.com/Swapnil0x17/SpectreScope)

🌐 Online Demo: [Try SpectreScope](https://spectrescope.streamlit.app/)

---

<p align="center">
  🔊 <strong>SpectreScope CLI</strong><br>
  <em>Explore the signal. Visualize the spectrum.</em>
</p>
