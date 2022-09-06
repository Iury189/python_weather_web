import requests, json, webbrowser

api_key = "3d57b8d8656846b828a661fde61cbe9b"
lang = "pt_BR"

while True:
    cidade = str(input("Digite o nome de uma cidade: "))
    if (cidade.strip() == ''):
        print("O nome da cidade não pode ficar vazia.")
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&lang={lang}"
        clima = requests.get(url).json()
        break
        
if clima["cod"] != "404":
    geografia = clima["id"]
    id_city = geografia
    print("Aguardando resultado...")
    webbrowser.open(f"https://openweathermap.org/city/{id_city}")
else:
    print(f"A cidade {cidade} não foi encontrada.")
