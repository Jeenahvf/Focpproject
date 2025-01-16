import random
import json
import logging
from pathlib import Path

# Setup logging
logging.basicConfig(filename="chat_log.txt", level=logging.INFO, 
                    format="%(asctime)s - USER: %(message)s")
logging.info("Chat session started")

# Agent names
agent_names = ["Shyam", "Hari", "Krishnaa", "Rabi"]

# Load responses from a JSON file
responses_file = Path("responses.json")
def load_responses(file_path):
    responses = {}
    try:
        with file_path.open("r") as f:
            responses = json.load(f)  # Load JSON data into a dictionary
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Default responses will be used.")
    return responses

responses = load_responses(responses_file)

random_responses = [
    "That's an interesting question, {name}!",
    "I'm not sure about that, {name}, but I'll find out.",
    "Could you please elaborate, {name}?",
    "I'm here to help, {name}!"
]

def save_log(message):
    """Save user and agent messages to the log file."""
    logging.info(message)

def chatbot():
    print("Welcome to the University of Poppleton chat system!")
    
    # User name input with validation
    user_name = input("Hello! May I know your name? ").strip()
    while not user_name:
        user_name = input("Please enter a valid name: ").strip()

    # Agent selection
    print("Available agents: " + ", ".join(agent_names))
    agent_name = input("Please choose an agent name from the list above: ").strip()
    
    # Validate agent name
    while agent_name not in agent_names:
        agent_name = input(f"Agent name '{agent_name}' not found. Please choose a valid agent name: ").strip()

    print(f"Hello, {user_name}! My name is {agent_name}. I am your Personal Assistant. How can I assist you today?")
    logging.info(f"Chat session started with agent: {agent_name}")

    while True:
        user_input = input(f"{user_name}: ")
        save_log(f"USER: {user_input}")

        if user_input.lower() in ["bye", "see you", "quit", "exit"]:
            print(f"Goodbye, {user_name}! Great day ahead {user_name}!")
            save_log("Chat session ended")
            break

        response_found = False
        for keyword, response in responses.items():
            if keyword.lower() in user_input.lower():  # Check for partial matching
                print(f"{agent_name}: {response}")
                save_log(f"AGENT: {response}")
                response_found = True
                break

        if not response_found:
            random_response = random.choice(random_responses).format(name=user_name)
            print(f"{agent_name}: {random_response}")
            save_log(f"AGENT: {random_response}")

        # Simulate random disconnection
        if random.random() < 0.05:  # 5% chance of disconnection
            disconnection_message = "Oh no, it seems we've been disconnected. Please try again later!"
            print(f"{agent_name}: {disconnection_message}")
            save_log(f"AGENT: {disconnection_message}")
            break

if __name__ == "__main__":
    while True:
        chatbot()
        another_session = input("Would you like to start another session? (yes/no): ").strip().lower()
        if another_session not in ["yes", "y"]:
            print("Thank you for using the chat system. Goodbye!")
            break