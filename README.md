# A Basic Cisco Router / Switch Configurator 
This project is in active d evelopment and most of the functions inside it are not yet ready for use.

## Installation
To install this project, you will need to have Python 3.0 or higher installed on your system. You can download Python from [here](https://www.python.org/downloads/).

Once Python is installed, git clone this repo by ```git clone https://github.com:Abinash3366/Cisco-Configurator.git``` or download the zip [here](https://github.com/Abinash3366/Cisco-Configurator/archive/refs/heads/master.zip).
This program does not contain any malicious code and is safe to use however it is always advisable to check the code before running it. 

You will also require the modules `pyserial` and `pyperclip`. You can install these modules by running the following commands in your terminal:
```Pip install pyserial```
```Pip install pyperclip```  or by running ```pip install -r requirements.txt``` <br>

**TLDR**: Install Python, clone the repo, install the modules and run the program (Commands below)
1. ```git clone https://github.com:Abinash3366/Cisco-Configurator.git```
2. ```cd Cisco-Configurator```
3. ```pip install -r requirements.txt```
4. ```python main.py``` or ```python3 main.py```

## Usage
Once the program is downloaded and modules are installed you can run the program by running the following command in your terminal:
```python3 main.py``` or ```python main.py``` depending on your system.

To use the automatic send functionality you will need to have a Cisco device connected to your computer. You can connect the device to your computer using a USB to Console cable. This project assumes that your on a Windows device using a USB to Console cable as mention before, If you would like to change replace the references of ```com``` to your OS's port. <br>
## What works?
Basic Setup works for both Router and Switches. <br>
Basic Interface setup works for both routers and switches. <br>
The program is currently able to send commands to a Cisco device and copy the output to your clipboard. <br>

### Other Notices
As the name suggests this configurator is just a basic one and is only meant to save the 5m that it will take to manually put the commands in. Again project is still in development and more features will be added in the future. <br>

### Contributing & Issues
Pull requests are always welcome!
If you have any issues with the program please confirm that your device and cable are working properly and that you have entered the correct port. If you are still having issues please open an issue, and I will try to fix it as soon as possible. <br>

