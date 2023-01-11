# PyQTLyceumProject

## Installation
### Windows
```bash
git clone https://github.com/liltousin/PyQTLyceumProject.git
cd PyQTLyceumProject
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
git update-index --assume-unchanged .env
```
### Linux 
```bash
git clone https://github.com/liltousin/PyQTLyceumProject.git
cd PyQTLyceumProject
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
git update-index --assume-unchanged .env
```
## Setting up .env
1. Go to my.telegram.org , if not accessible than use any VPN<br>
2. Enter Telegram phone number in format +918457345497<br>
3. Enter the received code on @telegram<br>
4. Click on Create Application<br>
5. Enter any name and nickname.<br>
6. Select other and leave discription empty and proceed.<br>
7. You will get your APP ID & HASH<br>
9. Сopy and paste your API ID & HASH into the .env file<br>

## Run (Windows & Linux)
```bash
python main.py
```

## Usage
