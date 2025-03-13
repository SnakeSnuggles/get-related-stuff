def summary_maker(text):  
    return f"""Summarize this text while keeping important smaller details that contribute to the overall meaning. Don't just focus on major events—mention key moments, causes, and context that add depth: {text}"""
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
