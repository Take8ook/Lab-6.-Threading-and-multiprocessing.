import wikipedia
import time
from threading import Thread


def saving_data(player_name, is_for_threads=False):
    wiki_page = wikipedia.page(player_name)
    file_name = ""
    if is_for_threads:
        file_name = "Lab_6_4 with threads.txt"
    else:
        file_name = "Lab_6_4.txt"
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("URL: " + wiki_page.url + "\n")
        file.write(wiki_page.original_title + "\n")
        file.write(wiki_page.summary + "\n" * 2)


players = [
    "Mesut Ozil",
    "Nuri Sahin",
    "Roman Weidenfeller",
    "Mauro Icardi",
    "Cristiano Ronaldo",
    "Pele",
    "Lev Yashin",
    "Emre Can",
    "Sami Khedira",
    "Fabio Cannavaro"
]
wikipedia.set_lang("en")
start = time.time()
for player in players:
    saving_data(player)

print(f"Time - {round(time.time() - start, 4)} s")

start = time.time()
ths = []
for player in players:
    ths.append(Thread(target=saving_data, args=(player, True, )))
for th in ths:
    th.start()
for th in ths:
    th.join()
print(f"Time for threads- {round(time.time() - start, 4)} s")
