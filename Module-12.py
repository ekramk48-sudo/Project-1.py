# Answer to the question no-01
import requests
def fetch_joke():
    url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print(data["value"])

    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")

if __name__ == "__main__":
    fetch_joke()

# Answer to the question no-02
import requests
def get_weather():
    api_key = "2143d50d81bb35d006ee1af5801447d7"
    municipality = input("Enter the name of a municipality: ")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            description = data["weather"][0]["description"]
            temp_celsius = data["main"]["temp"]

            print(f"Weather in {municipality.capitalize()}:")
            print(f"Condition: {description.capitalize()}")
            print(f"Temperature: {temp_celsius:.1f}°C")
        elif response.status_code == 404:
            print("Municipality not found. Please enter a valid Municipality name!.")

        else:
            print("An error occurred! You did not write any municipality name!")

    except requests.exceptions.RequestException:
        print("Network error! Please check your connection.")

if __name__ == "__main__":
    get_weather()
