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
Analyze the following text and generate **a diverse set** of effective Google search queries based on its key topics. 

### **Instructions:**
- Identify **all relevant topics** present in the text, not just the most obvious ones.
- Generate **concise and natural** searches.
- Prefer **multiple short searches over one long one**.
- Ensure **broad coverage** of themes, including historical, social, and political aspects.
- Avoid unnecessary focus on relationships between characters.

### **Example Output:**
["history of book banning", "election fearmongering examples", "hate crimes against immigrants statistics", "anti-Muslim discrimination stories", "government surveillance and free speech", "media bias in war coverage"]

Text:
    {summarized}

Return a **Python list of strings** with at least 5 varied and relevant search queries.
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
    for result in search(google_search, num_results=100,unique=True):
        print(result)
        if query not in links_to_add:
            links_to_add[query] = []
        links_to_add[query].append(result)
with open(f"{data_dir}to_sort.json", "w") as file:
    json.dump(links_to_add, file)
with open(f"{data_dir}summary.txt", "w") as file:
    file.write(summarized)
