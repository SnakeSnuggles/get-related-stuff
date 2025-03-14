def summary_maker(text):  
    return f"""Summarize the following by focusing on key events, actions, and outcomes. Emphasize themes such as Islamophobia, book burning, censorship, and similar significant topics. Avoid analyzing personal relationships or character emotions. Present the summary in a clear chronological order:\n\n{text}"""

def line_maker(message_between):
    print("-"*50)
    print(message_between)
    print("-"*50)


data_dir = "data\\"
Pdata = f"{data_dir}data.txt"
Psummary = f"{data_dir}summary.txt"
Puser_sort = f"{data_dir}user_to_sort.json"
Pto_sort = f"{data_dir}to_sort.json"
Psorted = f"sorted.txt"
