---
title: Holiday_Assistant
app_file: app.py
sdk: gradio
sdk_version: 5.34.2
---
# 🌴 Holiday Planner — Your AI Sidekick for Trip Planning

**Holiday Planner** is an intelligent personal assistant designed to help you plan your holidays effortlessly.  
It can search for flights, explore destinations, perform web searches, retrieve Wikipedia info, run calculations, and even send mobile notifications — all through an interactive **Gradio** interface.

---

## 🚀 Features

- ✈️ **Flight Search**  
  Uses the **Google Flights API (via SerpAPI)** to find the best flights between airports using their IATA codes (e.g., STR → FRA).

- 🌐 **Web Search**  
  Integrated with **Google Serper API** to perform general online searches.

- 📚 **Wikipedia Search**  
  Fetch summaries and detailed information from Wikipedia using LangChain’s Wikipedia tool.

- 📂 **File Management**  
  Provides a **sandboxed local file system** using `FileManagementToolkit` — save and retrieve files securely within the app.

- 🧮 **Python REPL Tool**  
  Run Python code snippets safely (e.g., for quick calculations or data transformations).

- 🔔 **Push Notifications**  
  Sends real-time alerts to your **mobile device** through the **Pushover app**.

- 🧭 **Gradio Interface**  
  A clean and interactive chat-based UI for easy communication with your AI holiday planner.

---

## 🧠 Architecture Overview

The system is built with **LangChain** and **LangGraph**, featuring:
- A main “worker” agent orchestrating all tasks  
- Multiple integrated tools (flight search, Wikipedia, Google, etc.)  
- A persistent state graph to manage agent reasoning steps  

---

## 🧰 Tech Stack

- **Python 3.10+**
- **LangChain / LangGraph**
- **Gradio** (frontend)
- **SerpAPI** (for flight and Google search)
- **Playwright** (for browser automation)
- **Pushover API** (for notifications)
- **Wikipedia API**
- **AsyncIO**

---

## ⚙️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/holiday-planner.git
   cd holiday-planner

