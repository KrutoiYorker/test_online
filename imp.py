import requests

#bel_bank="https://www.nbrb.by/api/exrates/rates/USD?parammode=2"
#requests.get("https://audioboom.com/channel/kingfallsam")
test=requests.get("https://audioboom.com/channel/kingfallsam")

print(test.json()) #возвращает html


