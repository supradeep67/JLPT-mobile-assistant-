# 📱 AI-Powered JLPT Assistant (Android, Mid-Range Phones)  
**Experimental Project — Ongoing**

---

## 🎯 The Problem
As a self-learner of Japanese, I wanted a 24/7 practice partner. Standard LLMs often miss the fine details of JLPT grammar (particles, registers), and running them on mid-range phones like the **Samsung M56** or **iQOO Z7s** demands efficiency without losing accuracy.

---

## 🛠️ Approach
Instead of huge models, I’m fine-tuning **Small Language Models (SLMs)** with a custom JLPT dataset (N5–N1). This makes them lightweight yet exam-ready.

---

## 🖥️ Chosen Model
###  RakutenAI 2.0 Mini (Instruct)  
By **Rakuten Group, Inc.** — released Feb 2025, Apache 2.0 licensed.  

- **Size:** ~1.5B parameters (perfect for mid-range phones)  
- **Training:** High-quality Japanese + English  
- **Performance:** Top-tier in sub-2B Japanese MT Bench  
- **Languages:** Japanese & English  

Rakuten’s  open-source and Japanese excellence makes this model the heart of my project. 🙌

---

## 🏗️ Data Pipeline
1. Clean JSON (fix paths, encoding).  
2. Structure keys (`title`, `jlpt_level`).  
3. Convert to JSONL for QLoRA fine-tuning.  

---

## 📱 Target Hardware
- Samsung Galaxy M56 (Exynos 1480 / 8GB RAM)  
- iQOO Z7s (Snapdragon 695 / 6GB RAM)  
- Format: 4-bit GGUF  

---

## 🚩 Roadmap
- [x] Reliable data collection + cleaning  
- [x] JSON fixes + automation  
- [ ] JSON → JSONL conversion  
- [ ] QLoRA fine-tuning (Colab/Kaggle)  
- [ ] Quantization for Android  
- [x] App development (UI done ✅)  

---

## 📝 Lessons Learned
- JSON handling & schema fixes  
- Path errors solved with `.strip('"')`  
- Debugging type mismatches in mapping  

---

## 📂 Tech Stack
- Python (fine-tuning, automation)  
- Java/Kotlin (Android app)  
- Bash (Git, GitHub)  
- GPU: NVIDIA A100 (Colab)  
- QLoRA: Unsloth notebooks for efficient training  

---

## 📱 App Features
- Modern UI  
- Chat history  
- Settings log  
- Customizable interface  
- Ongoing improvements  

---

## ⚖️ License
Apache 2.0 (RakutenAI) + custom scripts. See `LICENSE`.

---

## ABOUT ME 
 🐥こんにちは!
I’m a 16-year-old student builder with a deep-rooted fascination for Japanese engineering and linguistics. Currently, I’m experimenting with the Rakuten 1.5B model to explore how small language models can perform on mobile devices.
When I’m not staring at a terminal, I’m usually deep-diving into Japanese history or practicing my Kanji (and realizing how much I still have to learn!). I believe the best tech is built with a mix of modern innovation and traditional Kodawari 　自己紹介を読んでくださって ありがとう　。. 🏔️💻  

📧 Email: supradeepsingha06@outlook.com  
📧 Gmail: supradeep176@gmail.com  

# last edit : 11/05/26  

---

