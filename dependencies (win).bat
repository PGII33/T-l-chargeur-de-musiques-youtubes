winget install -e --id Python.Python.3.11
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.11 get-pip.py
pip install -r requirements.txt
