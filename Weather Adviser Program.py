# Weather Adviser Program
weather = input("What’s the weather today? (sunny/rainy/snowy): ")
temperature = int(input("What’s the temperature outside? "))

if weather == "rainy":
    print("Take an umbrella ☔")
    if temperature < 60:
        print("And wear a jacket!")
elif weather == "sunny":
    print("It’s a bright day 🌞")
    if temperature > 85:
        print("Wear sunglasses and drink water 💧")
else:
    print("Bundle up, it’s cold ❄️")
