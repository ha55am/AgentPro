# 🧠 ScholarSage

**An Intelligent Agent for Academic Research Brainstorming and Summarization**

---

## 📘 Overview

**ScholarSage** is an intelligent ReAct-based research assistant powered by [AgentPro](https://github.com/traversaal-ai/AgentPro). It helps researchers, students, and educators brainstorm academic topics, discover relevant literature, and auto-generate PowerPoint slides with concise summaries.

---

## 🔍 Features

- 📚 **Topic-based Research Assistant**  
  Input any academic topic and get summarized insights from top scholarly papers.

- 🔎 **Semantic Scholar Integration**  
  Retrieves high-quality academic papers via Semantic Scholar API.

- 🧠 **OpenAI-Powered Summarization**  
  Summarizes abstracts or extracted text using GPT-4o for concise explanations.

- 📊 **PowerPoint Generation**  
  Automatically creates professional slides with titles, authors, summaries, and a final topic overview.

- 🧩 **Modular AgentPro Framework**  
  Built using the ReAct (Reasoning + Acting) loop with customized tool extensions.

---

## ⚙️ How It Works

1. User enters a research topic.
2. Agent searches for academic papers using the Semantic Scholar tool.
3. Abstracts or findings are summarized via the Summarizer tool.
4. Summaries are compiled into a PowerPoint file using the PowerPoint Generator tool.
5. An overall final summary slide is created using LLM summarization.

---

## 🛠️ Tools Implemented

- `SemanticScholarTool` – Finds papers using Semantic Scholar API  
- `SummarizerTool` – Uses OpenAI (GPT-4o) for summarization  
- `PowerPointGeneratorTool` – Generates slides from summaries  
<!-- PDF tools omitted for token optimization -->
<!-- - `PDFDownloaderTool` – (Optional) Download PDFs  
- `PDFReaderTool` – (Optional) Extract sections like abstract, intro, conclusion -->

---

## 🚀 Future Expansion

- Add full-paper analysis by chunking long texts.
- Use larger-context LLMs (e.g., Gemini, Claude) for complete literature reviews.
- Export full structured writeups with citations in markdown, PDF, or Word.
- Build a frontend (e.g., Streamlit) for ease of use by non-technical users.

---

## 💻 Tech Stack

- Python 3.10+
- OpenAI GPT-4o
- Semantic Scholar API
- `python-pptx`
- `dotenv`
- AgentPro (ReAct Agent Framework)

---

## 🏁 How to Run

Make sure to:
1. Clone the repository.
2. Install the requirements using `pip install -r requirements.txt`.
3. Create a `.env` file with your `OPENAI_API_KEY`.

Then run the following command:

```bash
python research_assistant.py
