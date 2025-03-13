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
Analyze the following text and extract multiple core themes. For each theme, generate at least **two distinct** Google search queries.

### **Instructions:**
- **Identify multiple overarching themes** (e.g., "discrimination," "cultural identity," "political rhetoric," "immigration").
- Create search queries in **different formats**:
  - ✅ **General topics** ("history of book banning")
  - ✅ **Cause-effect searches** ("how election fearmongering affects minorities")
  - ✅ **First-person experiences** ("stories of immigrant families overcoming discrimination")
  - ✅ **Fact-based queries** ("statistics on anti-Muslim hate crimes in the US")
- **Make queries natural for Google and YouTube searches.** 

### **Example Output:**
["history of book banning", "how political rhetoric fuels discrimination", "stories of immigrants overcoming religious prejudice", "statistics on anti-Muslim hate crimes in the US"]

Text:
    {summarized}

Return a **Python list of strings** formatted strictly as shown in the example.
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
