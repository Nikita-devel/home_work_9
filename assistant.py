import datetime
import requests

# API_KEY = "<YOUR_API_KEY>"
API_KEY = "653c3ccd328356a16a58c6dbd440c093"


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Enter both name and phone"
        
    return inner


contacts = {}


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return "Contact added successfully"


@input_error
def change_contact(name, phone):
    contacts[name] = phone
    return "Contact updated successfully"


@input_error
def get_phone(name):
    return contacts[name]


def show_all_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}"for name, phone in contacts.items()])
    else:
      return "No contacts found"


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == 200:
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        return f"The current weather in {city} is {weather_description}. Temperature: {temperature}°C"
    else:
        return "Failed to retrieve weather information"


def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return f"The current time is {current_time}"


def help_commands():
    return """
    Available commands:
    - hello: Greet the assistant
    - add <name> <phone>: Add a contact with the given name and phone number
    - change <name> <phone>: Change the phone number of an existing contact
    - phone <name>: Get the phone number of a contact
    - show all: Show all saved contacts
    - weather <city>: Get the current weather in the specified city
    - time: Get the current time
    - help: Show available commands
    - good bye, close, exit: Close the assistant
    """


def main():
    print("Welcome to the Assistant! How can I help you?")
    while True:
        user_input = input("Enter a command: ").lower().split(" ", 1)
        command = user_input[0]
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            name, phone = user_input[1].split(" ")
            print(add_contact(name, phone))
        elif command == "change":
            name, phone = user_input[1].split(" ")
            print(change_contact(name, phone))
        elif command == "phone":
            name = user_input[1]
            try:
                print(get_phone(name))
            except KeyError:
                print("Contact not found")
        elif command == "show":
            if user_input[1] == "all":
                print(show_all_contacts())
        elif command == "weather":
            city = user_input[1]
            print(get_weather(city))
        elif command == "time":
            print(get_current_time())
        elif command == "help":
            print(help_commands())
        elif command in ["good", "bye", "close", "exit"]:
            print("Good bye!")
            break
        else:
            print("Invalid command. Type 'help' to see the available commands.")


if __name__ == "__main__":
    main()