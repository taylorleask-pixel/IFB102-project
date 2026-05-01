# weather.py
import requests
import json
from config import API_KEY

def fetch_weather(city):
    """
    Fetch weather data from OpenWeatherMap API for a given city.
    
    Args:
        city (str): Name of the city to get weather for
        
    Returns:
        dict: Dictionary containing weather information or None if error
    """
    
    # Base URL for current weather data
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # Use 'metric' for Celsius, 'imperial' for Fahrenheit
    }
    
    try:
        # Make the API request
        print(f"Fetching weather data for {city}...")
        response = requests.get(base_url, params=params, timeout=10)
        
        # Check if request was successful
        if response.status_code == 200:
            # Parse JSON response
            weather_data = response.json()
            
            # Extract the required information
            weather_info = {
                'city': weather_data.get('name', 'Unknown'),
                'condition': weather_data['weather'][0]['main'],  # Rain, Clear, Clouds, etc.
                'temperature': weather_data['main']['temp'],  # In Celsius
                'wind_speed': weather_data['wind']['speed']  # In meters/second
            }
            
            return weather_info
            
        elif response.status_code == 404:
            print(f"Error: City '{city}' not found. Please check the city name.")
            return None
        elif response.status_code == 401:
            print("Error: Invalid API key. Please check your API key in config.py")
            return None
        else:
            print(f"Error: HTTP {response.status_code} - {response.reason}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the internet. Check your network connection.")
        return None
    except requests.exceptions.Timeout:
        print("Error: Request timed out. Please try again.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except (KeyError, json.JSONDecodeError) as e:
        print(f"Error parsing weather data: {e}")
        return None

def main():
    """
    Main function to test the fetch_weather function
    """
    print("="*50)
    print("Weather Information System")
    print("="*50)
    
    # Ask user for a city
    city = input("\nEnter city name (or press Enter for default cities): ").strip()
    
    if not city:
        # Test with some default cities if user just presses Enter
        test_cities = ["London", "New York", "Tokyo", "Sydney"]
        print("\nTesting with default cities:")
        
        for city_name in test_cities:
            print("\n" + "-"*40)
            weather = fetch_weather(city_name)
            
            if weather:
                print(f"\n✓ Weather in {weather['city']}:")
                print(f"  Condition: {weather['condition']}")
                print(f"  Temperature: {weather['temperature']:.1f}°C")
                print(f"  Wind Speed: {weather['wind_speed']:.1f} m/s")
            else:
                print(f"✗ Failed to fetch weather for {city_name}")
    else:
        # Fetch weather for user-specified city
        print()
        weather = fetch_weather(city)
        
        if weather:
            print("\n" + "="*50)
            print("Weather Information:")
            print("="*50)
            print(f"City: {weather['city']}")
            print(f"Condition: {weather['condition']}")
            print(f"Temperature: {weather['temperature']:.1f}°C")
            print(f"Wind Speed: {weather['wind_speed']:.1f} m/s")
            print("="*50)
        else:
            print(f"\nFailed to fetch weather for '{city}'. Please check the city name and try again.")

if __name__ == "__main__":
    main()
