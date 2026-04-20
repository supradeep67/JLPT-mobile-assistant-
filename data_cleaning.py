import json 
import os 

file_part = r"your file path" 

# 1. Loading my data
with open(file_part, 'r', encoding="utf-8") as a:
    raw_data = json.load(a)

conversation_data = []

# 2. Process the data
for kanji, info in raw_data.items():
    jlpt = info.get("jlpt_new")
    meaning = ", ".join(info.get("meanings", []))
    on_reading = ", ".join(info.get("readings_on", []))
    kun_reading = ", ".join(info.get("readings_kun", [])) # add from your exiting json file  the lebels  to make it formating as you like 
    radicals = ", ".join(info.get("wk_radicals", []))
    wankani_level = info.get("wk_level", "N/A")

    #  making a strucarier that a model can understand
    entry = {
        "instruction": f"explain the JLPT N{jlpt} kanji '{kanji}'.",
        "input": "",
        "output": (f"Sure, the kanji '{kanji}' is a JLPT N{jlpt} character meaning '{meaning}'. "
                   f"Its On-readings are '{on_reading}' and Kun-readings are '{kun_reading}'. "
                   f"It is composed of radicals like {radicals}. "
                   f"WaniKani level: {wankani_level}.")
    }
    conversation_data.append(entry) 

# 3. Save the new data 
with open("formatted_kanji.json", 'w', encoding='utf-8') as w:
    json.dump(conversation_data, w, ensure_ascii=False, indent=4)

    print ("data conversation is completed !  please check it  here ")
print("Your file is saved here:", os.path.abspath("formatted_vocabs.json"))

