import requests


api_key ='e48e55aba1f20576005d0657a414d710'

user_input =input("Enter city: ")
print(user_input)
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
if weather_data.json()['cod']=='404':
    print("No City Found")
else:

    weather =weather_data.json()['weather'][0]['main']
    temp =round(weather_data.json()['main']['temp'])
    print(f"The weather in{user_input}is:{weather}")
    print(f"The temprature in{user_input} is:{temp}°F")
