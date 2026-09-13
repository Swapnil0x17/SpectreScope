import streamlit as st
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os
import tempfile

st.set_page_config(page_title="SpectreScope", layout="wide")

st.title("SpectreScope")
st.markdown("**Spectrogram Analysis Tool**")

uploaded_file = st.file_uploader(
    "Please select an audio/video file...",
    type=["wav", "mp3", "flac", "ogg", "m4a", "aac", "mp4", "mkv", "avi", "webm"]
)

if uploaded_file is not None:
    st.write(f"[+] Selected file: {uploaded_file.name}")

    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.read())
        audio_path = tmp_file.name

    try:
        st.write("[+] Loading audio...")
        y, sr = librosa.load(audio_path, sr=None)
        st.write(f"[+] Duration: {len(y)/sr:.2f} seconds | Sample Rate: {sr} Hz")

        st.write("[+] Computing spectrogram...")
        D = librosa.stft(y)
        S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

        st.write("[+] Generating image...")
        fig = plt.figure(figsize=(14, 6))
        librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='hz', cmap='magma')
        plt.colorbar(format='%+2.0f dB')
        plt.title('Spectrogram Analysis - Intercepted Call')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.tight_layout()

        st.pyplot(fig)

        # Save image
        output_image = "spectrogram_output.png"
        fig.savefig(output_image, dpi=300, bbox_inches='tight')
        st.success(f"[+] Image saved as → {output_image}")

        # Download button
        with open(output_image, "rb") as file:
            st.download_button(
                label="Download Spectrogram PNG",
                data=file,
                file_name="spectrogram_output.png",
                mime="image/png"
            )

    except Exception as e:
        st.error(f"[!] Error: {e}")
        st.warning("Note: Video files (.mp4, .mkv, etc.) require ffmpeg to be installed.")

    finally:
        os.unlink(audio_path)

else:
    st.info("No file selected. Please upload a file to begin.")
