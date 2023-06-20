Assistant Application
This is a command-line assistant application that allows you to manage contacts and obtain weather information. It provides various commands to perform different tasks efficiently.

Prerequisites
Python 3.6 or higher
pip package manager
Installation
Clone the repository or download the source code.
Navigate to the project directory.
bash
Copy code
cd assistant-application
Install the required dependencies using the following command.
Copy code
pip install -r requirements.txt
Usage
Run the application by executing the following command in the terminal.

Copy code
python assistant.py
The assistant will greet you and prompt you to enter a command. Use the available commands to interact with the assistant.

Available Commands
hello: Greet the assistant.
add <name> <phone>: Add a contact with the given name and phone number.
change <name> <phone>: Change the phone number of an existing contact.
phone <name>: Get the phone number of a contact.
show all: Show all saved contacts.
weather <city>: Get the current weather in the specified city.
time: Get the current time.
help: Show available commands.
good bye, close, exit: Close the assistant.
API Key
To retrieve weather information, you need to provide an API key. Replace <YOUR_API_KEY> in the code with your valid API key. You can obtain an API key from the OpenWeatherMap website (https://openweathermap.org/).