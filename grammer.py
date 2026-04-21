import json
import os

# Clean the path input
file_to_correct = input(" please input your file path : ").strip('"')
noov=  (input ( " please input what do you add it !  : "))

# 1. Load the existing data
with open(file_to_correct, 'r', encoding="utf-8") as f: 
    original_data = json.load(f)

reordered_list = []

# 3. Process the data
for item in original_data:
    ordered_item = {
        "title": item.get("title"),
        "jlpt_level": noov,
        
        "short_explanation": item.get("short_explanation"),
        "long_explanation": item.get("long_explanation"),
        "formation": item.get("formation"),
        "examples": item.get("examples")
    }
    reordered_list.append(ordered_item)

# 4. Save the file !!!!
correct_data = "newvocabn5.0.json"
with open(correct_data, "w", encoding="utf-8") as d:
    json.dump(reordered_list, d, indent=2, ensure_ascii=False)

print(" Done! File saved here: ", os.path.abspath(correct_data))
