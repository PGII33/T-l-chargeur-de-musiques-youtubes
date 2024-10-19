@echo off

winget install -e --id Python.Python.3.11
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
del get-pip.py
pip install yt_dlp