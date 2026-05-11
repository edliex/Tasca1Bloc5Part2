import random, datetime, json

tiempo = []
for i in range(5):
    tiempo.append(random.randint(13,20))

maxima = minima = tiempo[0]
media = 0
for temp in tiempo:
    if temp > maxima:
        maxima = temp
    if temp < minima:
        minima = temp
    media += temp

media = media/5

data = datetime.date.today()
print(data)
temps_json = {"Temperatura maxima": maxima, 
              "Temperatura minima": minima, 
              "Temperatura media": media
              }
    
with open(f"temp_{data}.json","w", encoding='utf-8') as fitx:
    json.dump(temps_json, fitx, indent=4)
    
