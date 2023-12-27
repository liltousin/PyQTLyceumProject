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

### Optional

```bash
git clone https://github.com/TilmanK/PyQt6-stubs
cd PyQt6-stubs
python setup.py install
cd ..
rm -rf PyQt6-stubs
```

## Setting up .env

1. Go to my.telegram.org, if not accessible than use any VPN
2. Enter Telegram phone number in format +918457345497
3. Enter the received code on @telegram
4. Click on Create Application
5. Enter any name and nickname.
6. Select other and leave discription empty and proceed.
7. You will get your APP ID & HASH
8. Сopy and paste your API ID & HASH into the .env file

### Настройка .env

1. Перейдите на сайт my.telegram.org, если он недоступен, используйте любой VPN.
2. Введите номер телефона Telegram в формате +918457345497
3. Введите полученный код на @telegram
4. Нажмите на кнопку Создать приложение
5. Введите любое имя и ник.
6. Выберите другое, оставьте описание пустым и продолжите.
7. Вы получите свой APP ID и HASH.
8. Скопируйте и вставьте свой API ID и HASH в файл .env

## Run (Windows & Linux)

```bash
python main.py
```

## Project description and usage instructions

When you first log in to the app you need to add your Telegram accounts by
clicking the "Add Account" button. Then, after logging in, you will be able to
manage your account. For example, double-clicking on the account will allow you
to check its status in the corresponding form. The color of the account depends
on its current state. There are only 4:

1. Red - account is banned.
2. Orange - account is not authorized.
3. Yellow - authorization file is missing.
4. Green - there is nothing wrong with the account.

In addition, the account at the time of the ban first turns orange, and only
after checking the status changes to red. This is done because to check the
account for a ban you need to send a code. Therefore, so that each time you
check the account does not come a code, orange status can mean both ban and no
authorization.

### Описание проекта и инструкция по использованию

При первом входе в приложение вам необходимо добавить свои аккаунты Telegram,
нажав кнопку "Добавить аккаунт". Затем, после входа в приложение, вы сможете
управлять своим аккаунтом. Например, двойное нажатие на аккаунт позволит вам
проверить его статус в соответствующей форме. Цвет аккаунта зависит от его
текущего состояния. Их всего 4:

1. Красный - аккаунт заблокирован.
2. Оранжевый - аккаунт не авторизован.
3. Желтый - отсутствует файл авторизации.
4. Зеленый - с аккаунтом все в порядке.

Кроме того, аккаунт в момент бана сначала становится оранжевым, и только после
проверки статус меняется на красный. Это делается потому, что для проверки
аккаунта на бан необходимо отправить код. Поэтому, чтобы при каждой проверке
аккаунта не приходил код, оранжевый статус может означать как бан, так и
отсутствие авторизации.

## P.S

The project is still in development. You can test it and add your issues, I will
be glad to everyone

#

Проект находится еще в разработке. Вы можете тестировать его и добавлять свои
issue, буду рад каждому
