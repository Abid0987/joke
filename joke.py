import requests

def get_random_joke():
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        response.raise_for_status()  # Raise an error for bad responses
        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    except requests.RequestException as e:
        return f"Oops! Something went wrong: {e}"

def main():
    print("Welcome to the Random Joke Generator!")
    while True:
        user_input = input("Type 'joke' to get a joke or 'exit' to quit: ").strip().lower()
        if user_input == 'joke':
            print(get_random_joke())
        elif user_input == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Invalid input. Please type 'joke' or 'exit'.")

if __name__ == "__main__":
    main()