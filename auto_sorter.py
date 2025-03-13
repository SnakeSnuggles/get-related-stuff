from ask_ai.ask import ask
from youtube_transcript_api import YouTubeTranscriptApi
import json
from vars import *

raw_data = {}
with open(f"{data_dir}to_sort.json", "r") as file:
    raw_data = file.read()
summary = ""
with open(f"{data_dir}summary.txt","r") as file:
    summary = file.read()

print(summary)
data = json.loads(raw_data)

results = []

for theme,links in data.items():
    for link in links:
        if link.strip() == "":
            continue
        ID = link.split("=")[1]
        transcript = ""
        try:
            script = YouTubeTranscriptApi.get_transcript(ID,languages=["en"])
            transcript = " ".join([entry["text"] for entry in script])
        except Exception as e:
            print(f"Error fetching transcript for {link}. Skipping...")
            print(f"Error {e}")

            continue
        to_summarize = summary_maker(transcript)
        summarized_transcript = ask(to_summarize)
        result = ask(f'''
Analyze the provided transcript and determine whether the given theme is relevant to its overall content. Use the summary as additional context to improve accuracy. 

### Criteria:
- **True (Relevant)**: The theme is a core topic, directly aligns with major ideas, OR significantly overlaps with related themes (e.g., Islamophobia, discrimination, political rhetoric, societal backlash).
- **False (Not Relevant)**: The theme is only loosely connected, is a minor background detail, or lacks meaningful overlap with the transcript's focus.

Consider **broader thematic connections**, not just direct word matching.

Return **only** `"True"` or `"False"`. Do not include any explanations, additional text, or formatting.
UNDER NO CIRCUMSTANCES SHOULD YOU RETURN ANYTHING BUT THE TRUE OR FALSE thank you very much
Summary (context):
{summary}

Transcript:
{summarized_transcript}
''')
        is_related = "true" in result.lower()
        print('_'*50)
        print(f"Video sum: {summarized_transcript}")
        print(result.strip())
        print(f"Video: {link} \nrelated:{is_related}")

        if is_related:
            results.append(link)

with open(f"{data_dir}user_to_sort.json","a") as f:
    for result in results:
        f.write(f"{result}\n")
