import sys
import os
from datetime import datetime
import whisper
from pyannote.audio import Pipeline
from pyannote.audio import Audio
from pyannote_whisper.utils import diarize_text

if len(sys.argv) != 3:
    print("Usage: python script.py <path_to_audio_file> <output_folder>")
    sys.exit(1)

# Get the command line arguments
audio_file_path = sys.argv[1]
output_folder = sys.argv[2]

os.makedirs(output_folder, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
output_file_path = os.path.join(output_folder, f"{os.path.basename(audio_file_path)}_{timestamp}_transcription.txt")

# Load diarization pipeline and model
pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization",
                                    use_auth_token="")
model = whisper.load_model("tiny.en")

# Perform diarization
diarization_result = pipeline(audio_file_path)

# Process diarization result and save transcription to a text file
with open(output_file_path, "w") as output_file:
    audio = Audio(sample_rate=16000, mono=True)

    for segment, _, speaker in diarization_result.itertracks(yield_label=True):
        waveform, sample_rate = audio.crop(audio_file_path, segment)
        text = model.transcribe(waveform.squeeze().numpy())["text"]
        output_file.write(f"{segment.start:.2f}s {segment.end:.2f}s {speaker}: {text}\n")

print(f"Transcription saved to {output_file_path}")
