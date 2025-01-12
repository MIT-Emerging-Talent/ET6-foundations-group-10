def check_weather(weather):
    """
    This function checks the type of weather and gives a response.
    It accepts one parameter:
    - weather: A string representing the weather (sunny, rainy, snowy, cloudy).

    It prints a message based on the weather type.
    """
    if weather == "sunny":
        print("It's bright today!")
    elif weather == "rainy":
        print("Take an umbrella.")
    elif weather == "snowy":
        print("It’s snowing!")
    elif weather == "cloudy":
        print("The sky is gray.")
    else:
        print("I don't know this weather.")

def ask_weather():
    """
    This function asks the user for the weather condition and 
    calls the check_weather function to respond.
    It does not accept any parameters.
    """
    weather = input("How is the weather? (sunny, rainy, snowy, cloudy) ").lower()
    check_weather(weather)

def main():
    """
    The main function is the entry point of the program.
    It starts the process of asking the user for weather information.
    """
    print("Let’s talk about the weather!")
    ask_weather()

# Start the program
main()

