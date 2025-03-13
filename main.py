from ask_ai.ask import ask 
import json
from googlesearch import search
from vars import *

lines = []
with open(f"{data_dir}data.txt", "r",encoding="latin-1") as line_f:
    for line in line_f:
        lines.append(line.strip())  # Remove trailing newline characters
prompt = " ".join(lines)
def ai_sum():
    to_summarize = summary_maker(prompt)
    summarized = ask(to_summarize)
    return summarized
def written_sum():
    with open(f"{data_dir}summary.txt","r") as file:
        summary = file.read()
    summarized = summary
    return summarized

summarized = ai_sum()

print(f"finnished summarize:\n{summarized}\n---------------------------------")

responce_real = ask(f'''
Analyze the following text and extract its core themes. Then, create a list of broad Google search queries based on these themes. The queries should:

    - Be broad enough to encompass various contexts (historical, social, political, etc.).
    - Reflect overarching themes without getting lost in niche or overly specific details.
    - Be structured as natural, real-world search queries that someone would actually use (e.g., "history of book banning," "impact of fearmongering on society").
    - Stay under one central theme (e.g., "fearmongering," "religious freedom," or "social dynamics").

Return the queries in a Python list of strings, formatted strictly as shown below.

Text:
    {summarized}

Output Example:

["history of censorship", "effects of fearmongering on society", "how political rhetoric influences public opinion", "impact of religious intolerance in contemporary times"]
''')
print("Finished keywords:\n---------------------------")

keyword_list = []
try: 
    list_start = responce_real.index("[")
    list_end = responce_real.index("]")
    responce_real = responce_real[list_start:list_end+1]
    keyword_list = eval(responce_real)

except ValueError:
    print(responce_real)
    quit()

[print(f"{index}: {keyword}") for index,keyword in enumerate(keyword_list)]
what_bad = input("Which ones are bad?: ")
what_bad = what_bad.split(" ")
what_bad = [bad for bad in what_bad if bad.strip()]

for bad in what_bad:
    keyword_list[int(bad)] = ""
keyword_list = [word for word in keyword_list if word != ""]

[print(f"{index}: {keyword}") for index,keyword in enumerate(keyword_list)]

links_to_add = {}
for query in keyword_list:
    print("_"*50)
    print(f"{query}")
    print("_"*50)
    google_search = f"{query} site:youtube.com/watch"
    for result in search(google_search, num_results=9,unique=True):
        print(result)
        if query not in links_to_add:
            links_to_add[query] = []
        links_to_add[query].append(result)
with open(f"{data_dir}to_sort.json", "w") as file:
    json.dump(links_to_add, file)
with open(f"{data_dir}summary.txt", "w") as file:
    file.write(summarized)
