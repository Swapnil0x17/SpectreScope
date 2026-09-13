# SpectreScope

**Advanced Browser-Based Spectrogram & Audio Forensics Tool**

SpectreScope is a lightweight, fully client-side audio analysis tool designed for digital forensics, CTF challenges, steganography detection, and signal analysis. It generates high-quality waveforms and spectrograms directly in the browser — no server, no upload to third parties, complete privacy.

---

## Features

- Drag & drop or click to upload audio files
- Real-time waveform visualization
- High-quality spectrogram generation
- Download spectrogram as PNG
- Fully client-side (no data leaves your browser)
- Clean terminal-inspired dark interface
- Supports multiple audio formats

---

## Supported Formats

- `.wav`
- `.mp3`
- `.flac`
- `.ogg`
- `.m4a`
- `.aac`
- `.webm`

> Note: Video files are not fully supported in the browser version.

---

## Live Demo

[Click here to use SpectreScope](https://yourusername.github.io/spectrescope/)

---

## How to Use (GUI)

1. Open the website
2. Drag and drop an audio file or click **Choose File**
3. Click **Analyze Audio**
4. View the Waveform and Spectrogram
5. Download the spectrogram if needed

---

## Local Usage

### Option 1: Just open the file
1. Download `index.html`
2. Open it in any modern browser (Chrome, Firefox, Edge)

### Option 2: Using a local server (Recommended)
```bash
# Using Python
python -m http.server 8000

# Then open:
http://localhost:8000
