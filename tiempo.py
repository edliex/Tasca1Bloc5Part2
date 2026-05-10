import random, datetime

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
    
with open(f"temp_{data}.txt","w", encoding='utf-8') as fitx:
    fitx.write(f"Temperatura maxima: {maxima}, Temperatura minima: {minima}, Temperatura media: {media}")
    