import json
import os
import random

# Modular fragments for variety SO THE MODEL DOSENT SOULD LIKE A BROKEN ROBOT 
intros = [
    "Sure! Let's break down '{t}'.",
    "Of course. '{t}' is a useful {L} grammar point.",
    "Certainly! '{t}' is commonly used in {L} level Japanese."
]                                                            # I GENERETED THIS PROMPT PART FROM AI YOU CAN COSTIMIZE IT HOWEVER YOU WANT 

explanations = [
    "It is used to {s} Basically, {long}",
    "This expression {s} In detail, {long}",
]

def format_grammar_data():
    file_path = input("Enter your JSON file path: ").strip()
    # ENTER YOUR JSON FILE ::
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    
    if isinstance(data, dict):
        data = [data]

    formatted_data = []

    for item in data:
        t = item.get("title", "Unknown")
        L = item.get("jlpt_level", "N/A")
        s = item.get("short_explanation", "")
        long = item.get("long_explanation", "")
        f_rule = item.get("formation", "")
        examples = item.get("examples", [])

        # Build output
        output = f"{random.choice(intros).format(t=t, L=L)} {random.choice(explanations).format(s=s, long=long)}"
        output += f"\n\nFormation: {f_rule}"

        if examples:
            selected = random.sample(examples, min(len(examples), 2))
            output += "\n\nExamples:"
            for ex in selected:
                output += f"\n- {ex['jp']} ({ex['en']})"

        formatted_data.append({
            "instruction": f"Explain the Japanese grammar point '{t}'.",
            "input": "",
            "output": output
        })

    with open("alpaca_output_forN5.json", "w", encoding="utf-8") as w:
        json.dump(formatted_data, w, ensure_ascii=False, indent=2)
    print("Done! Check 'alpaca_output.json'.")

if __name__ == "__main__":
    format_grammar_data()