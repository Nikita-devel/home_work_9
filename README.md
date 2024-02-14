# Console Assistant Bot

## Project Description

This console-based assistant bot serves as a prototype for a contact and calendar management application. The focus of this homework is on the bot's interface, implemented as a Command Line Interface (CLI). The CLI consists of three main components:

1. **Command Parser:** Responsible for parsing user input, extracting keywords, and identifying command modifiers from the input string.
2. **Command Handler Functions:** A set of functions, also known as handlers, that execute the corresponding commands.
3. **Request-Response Loop:** This part of the program manages user input and returns responses from the handler functions.

At its initial stage, the assistant bot can store and retrieve contact information. Specifically, it can save a contact's name and phone number, find a phone number based on a contact's name, update an existing contact's phone number, and display all saved contacts.

To implement this functionality, a dictionary is used to store user names as keys and corresponding phone numbers as values.

## Conditions

- The bot runs in an infinite loop, waiting for user commands.
- The bot terminates when it encounters the command: .
- The bot is case-insensitive to user input.
- The bot accepts the following commands:
  - "hello": Responds with "How can I help you?"
  - "add ...": Adds a new contact to the memory (dictionary), where ... is the user's input for name and phone number, separated by a space.
  - "change ...": Updates the phone number of an existing contact in the memory, where ... is the user's input for name and the new phone number, separated by a space.
  - "phone ...": Displays the phone number for the specified contact, where ... is the user's input for the contact's name.
  - "show all": Displays all saved contacts with their phone numbers.
  - "good bye", "close", "exit": Terminates the bot after printing "Good bye!".

## Error Handling

- All user input errors are handled by the `input_error` decorator. This decorator returns user-friendly messages such as "Enter user name," "Give me name and phone please," etc. It handles exceptions raised in the handler functions (KeyError, ValueError, IndexError) and returns appropriate messages to the user.

## Usage

1. Ensure Python is installed on your system.
2. Install the required dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```
3. Run the script (assistant_bot.py) in the command line:
  
  ```bash
  python assistant_bot.py
  ```
4. Follow the on-screen instructions to interact with the bot.
