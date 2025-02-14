# speech-to-text-whisper

Python code for transcribing audio files to text files using whisper and pyaanote tools.

#Installation Steps, for manual installtion

Create a virtual environment in python

python3 -m venv venv
source venv/bin/activate


Install whisper
pip install -U openai-whisper

To update the package to the latest version of this repository, please run:
pip install --upgrade --no-deps --force-reinstall git+https://github.com/openai/whisper.git

Install ffmpeg package,
apt install ffmpeg

pip install setuptools-rust


After these steps whisper modules and packages will be installed.

Install pyannote-whisper,


git clone https://github.com/yinruiqing/pyannote-whisper

cd  pyannote-whisper
pip install -r requirements.txt
pip install pyannote.audio
pip install pydub


download an audio clip in .wav format and copy it in pyannote-whisper/data folder

create an account in https://huggingface.co/ website and create a access token from the site. This access token needs to be used in pyannote python script.

============================================

A docker container has been built with the above installation steps pull it from the docker hub: 


=============================================

Command to execute the python script:

**python3 transcribe.py </path of input audio file/> </path to save the output text file/>**
