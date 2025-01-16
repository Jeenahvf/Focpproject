#Write a program that manages a list of countries and their capital cities. It should prompt the user to enter the name of a country. If the program already "knows" the name of the capital city, it should display it. Otherwise it should ask the user to enter it. This should carry on until the user terminates the program (how this happens is up to you).
def manage_countries_and_capitals():
    # Initialize an empty dictionary to store country-capital pairs
    country_capitals = {}

    print("Welcome to the Country-Capital Manager!")
    print("Type 'exit' at any time to quit the program.")
    
    while True:
        # Prompt the user to enter a country
        country = input("\nEnter the name of a country: ").strip()
        
        # Handle termination request
        if country.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        # Normalize country name to lowercase for case-insensitive matching
        country_lower = country.lower()
        
        # Check if the country is already known
        if country_lower in country_capitals:
            print(f"The capital of {country} is {country_capitals[country_lower]}.")
        else:
            # If the country is not known, ask the user to provide the capital
            capital = input(f"I don't know the capital of {country}. Please enter it: ").strip()
            
            # Store the new country and capital in the dictionary
            country_capitals[country_lower] = capital
            print(f"Thank you! The capital of {country} has been stored as {capital}.")

# Run the program
manage_countries_and_capitals()
