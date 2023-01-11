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
1. Go to my.telegram.org , if not accessible than use any VPN
2. Enter Telegram phone number in format +918457345497
3. Enter the received code on @telegram
4. Click on Create Application
5. Enter any name and nickname.
6. Select other and leave discription empty and proceed.
7. You will get your APP ID & HASH
9. Сopy and paste your API ID & HASH into the .env file

## Run (Windows & Linux)
```bash
python main.py
```

## Usage
When you first log in to the app you need to add your Telegram accounts by clicking the "Add Account" button. Then, after logging in, you will be able to manage your account. For example, double-clicking on the account will allow you to check its status in the corresponding form. The color of the account depends on its current state. There are only 4:
1. Red - account is banned.
2. orange - account is not authorized.
3. yellow - authorization file is missing.
4. Green - there is nothing wrong with the account.

Also, the account when banned first becomes orange, but then only after checking the status will change to red. This is done because to check the account to ban you need to send a code, this is done so that each time you check the account did not come code.

### P.S
The project is still in development. You can test it and add your issues, I will be glad to everyone
