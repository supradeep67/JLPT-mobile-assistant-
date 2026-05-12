# 🙂 Progress Log

## Date: 8 May 2026
Over the past week, I’ve been troubleshooting why **llama.cpp** kept crashing when running a test model (**phi‑4 mini instruct**). After a lot of trial and error, I made a major decision: I’m abandoning the **llameged** library and switching to a new one.  

Today I discovered the **llamtick** library, tested it on my model, and it worked! Next step: start writing the AI logic for my main app.

---

## Date: 9 May 2026
Integration of the **llamtick** library is complete. I tested it on the **Qwen 2.5‑0.5B Instruct** model. It runs, but the outputs are currently random and not useful.  

Now I’m investigating why this is happening and working on a fix.
