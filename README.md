# AN AI Powered JLPT assistent on mid- range phones (ANDROID ) // AN EXPEREMENTAL PEOJECT ( one going) 
**Fine-tuning SLMs for N1-N5  Accuracy on Mid-Range Android**
-----------------------------------------------------------------------------------------------------
## 🎯 The Problem
I am a Self  Japanese laerner and So For That I Was Alaways Needed a Someone That can help to Pratice 24/7 And So I Was Useing AI to Boost My Learning and Found That 
Standard Large Language Models (LLMs) often struggle with the nuances of JLPT N1/N2 TO N5 grammar (like particle selection and formal registers). Furthermore, running these models on mid-range devices like the **Samsung M56** and **iQOO Z7s** requires high efficiency without sacrificing linguistic precision.

## 🛠️ Engineering Approach
This project focuses on the **Data-Centric AI** approach. Instead of using a massive model, I am fine-tuning "Small Language Models" (SLMs) using a custom-curated dataset.
  

## 🖥️ Choosen model
   
   📀 RAKUTEN 2.0 MINI(Instruct Model)  BY RAKUTEN GROUP.Inc  ( Main model )
   ## WHY RAKUTEN ?
     << MODEL INTRODUCATION > >
     I Choose  this model becuse its around 1.5B in parameters and runneble on  mid range mobiles
     It Was Relesed On February 2025 . licence under Apache 2.0 ( open source for Commercial use ).
     and its was Trained on High-Qulity japanese and english text makes its perfect choice for this project . 

     🧠 Performance 
      Inference: Designed for low-latency, cost-effective tasks like summarization and dialogue systems.
      Benchmarks: Delivers top-tier performance on the Japanese MT Bench for models in the sub-2B category.
      Primary languge : JAPANESE AND ENGLISH

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### 🏗️ Data Pipeline
1. **Cleaning:** Python scripts to handle Windows-specific pathing and JSON encoding.
2. **Structuring:** Reordering JSON keys to prioritize `title` and `jlpt_level`.
3. **Conversion:** Transforming raw JSON into **JSONL (JSON Lines)** format for QLoRA training.

### 📱 Target Hardware
- **Samsung Galaxy M56** (Exynos 1480 / 8GB RAM)
- **iQOO Z7s** (Snapdragon 695 / 6GB RAM)
- **Target Format:** 4-bit GGUF 


## 🚩 Tech Stack 
 - MAIN LANGUAGE :  PYTHON ( for fine tunning , data cleaning , and atometion taks eg, web sclaping etc ,)
 - APPLICATION LANGUAGE : JAVA/KOTLIN 
 - BASH ( GIT, GITHUB )

## HARDWARE & TECHNICES & DATA 
-GPU : NEVIDA A100 --> GOOLE COLAB 
- QLORA: NOOTBOOKS LIKE UNSLOTH WHICH HELP ME TO MANAGE SPACE ON A LIMITED STORAGE AND WILL TRAIN ONLY A SMALL PART TO MAKE HARDWARE FRIENDLY AND WILL USE LESS TIME .
MODEL : FROM  HUGGING FACE 
-----------------------------------------------------------------------------------------------------

## 🚀 Progress Roadmap
- [x] Finding RELIBLE DATA AND CLEANING 
- [x] Initial JSON cleaning and logic fixing.
- [x] Automated directory-to-path handling.       
- [ ] JSON to JSONL conversion script.
- [ ] QLoRA Fine-tuning on Kaggle/Colab.
- [ ] Quantization for Android deployment.
         Progress (50%) 

## 📂 Scripts Included
`data cleaning.py`: Standardizes raw JSON input, fixes formatting errors, and ensures `UTF-8` compatibility.

## 📝 Lessons Learned (Engineering Log)
*   **JSON HANDELING:** Learned how to format a json or edit an json to model Frindly json file 
*   **Path Handling:** Solved `OSError [Errno 22]` by implementing `.strip('"')` to handle Windows "Copy as Path" artifacts.
*   **Schema Logic:** Fixed a `TypeError` by ensuring `list` indices are not treated as `dictionary` keys during the mapping process.

## ⚖️ License
ALL RIGHTS RESERVED See `LICENSE` for more information.



## ABOUT ME 
 🐥こんにちは!
I’m a 16-year-old student builder with a deep-rooted fascination for Japanese engineering and linguistics. Currently, I’m experimenting with the Rakuten 1.5B model to explore how small language models can perform on mobile devices.
When I’m not staring at a terminal, I’m usually deep-diving into Japanese history or practicing my Kanji (and realizing how much I still have to learn!). I believe the best tech is built with a mix of modern innovation and traditional Kodawari 　自己紹介を読んでくださって ありがとう　。. 🏔️💻
## connect with me 
email : supradeepsingha06@outlook.com
gmail : supradeep176@gmail.com 
## my social accounts 
insta : cheeze_wizard

feel free to reach me out for feedback and suggetions byee

last modified : 21/04/26
