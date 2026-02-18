# 🏥 SWASTHYA SETU AI

## Multilingual Rural Healthcare Assistant

SWASTHYA SETU AI is an **AI-powered multilingual healthcare assistant** designed to provide **symptom-based medical guidance**, **government health scheme information**, **emergency detection**, **nearby hospital discovery**, and **helpline access** for rural and semi-urban populations.

The system focuses on improving healthcare accessibility by leveraging **AI, Retrieval-Augmented Generation (RAG)**, **location intelligence**, and **voice interaction** to deliver safe, structured, and explainable medical responses.

---

## 🎯 Problem Statement & Goals

Healthcare access in rural regions faces several challenges:

* Limited doctor availability at Primary Health Centres (PHCs)
* Language barriers for non-English speakers
* Delayed emergency response
* Dependence on ASHA workers for first-level triage
* Lack of awareness about government health schemes
* Difficulty locating nearby hospitals quickly

SWASTHYA SETU AI aims to bridge these gaps by providing:

* AI-based symptom triage assistance
* Multilingual voice interaction (English + Hindi)
* Emergency risk detection and escalation
* Government health scheme awareness
* Nearby hospital navigation with maps
* Quick access to medical helplines
* Confidence-aware medical guidance using evidence retrieval

---

## 🚀 Key Features

### 🤖 AI Medical Chat Assistant

* Symptom-based guidance using Retrieval-Augmented Generation (RAG)
* Context-aware responses grounded in medical references
* Confidence scoring with explainability
* Guardrails to prevent unsafe medical advice
* Fast fallback responses when API latency is high

---

### 🌍 Multilingual Support

* Automatic language detection
* Translation pipeline for Hindi and English
* Voice input and female voice output support
* Smooth speech synthesis for regional languages

---

### 🚨 Emergency Detection Engine (Improved)

* Detects critical symptoms like:

  * Chest pain
  * Stroke indicators
  * Unconsciousness
  * Severe bleeding
  * Breathing difficulty
  * Seizures

* Prevents false alarms for mild symptoms (e.g., cough)

* Overrides AI response with emergency instructions

* Provides immediate helpline guidance

---

### 🏥 Nearby Hospital Finder ⭐

One of the most impactful features added.

Users can:

* Detect current GPS location
* Enter location manually (JP Nagar, Banashankari, etc.)
* Find nearest hospitals instantly
* View contact details and addresses
* Navigate via Google Maps with route guidance

Dataset includes:

* Government hospitals
* Private hospitals
* Bengaluru central region coverage

---

### 🧾 Government Health Schemes Assistant

* AI-powered scheme search (Ayushman Bharat, Arogya Karnataka, etc.)
* Clean structured response format:

  * Description
  * Eligibility
  * Benefits
  * Official Sources

---

### 📞 Helpline Directory

* Quick access to emergency healthcare numbers
* One-tap calling interface
* Clean responsive UI for rural accessibility

---

### 🎤 Voice Interface

* Speech-to-text symptom input
* Text-to-speech female AI doctor voice
* Talking medical avatar animation
* Voice ON/OFF toggle
* Hindi pronunciation fixes implemented

---

### 📊 Confidence Scoring System

Combines:

* Medical guideline similarity
* Symptom pattern matches
* Case similarity

Provides transparency and trust in AI decisions.

---

## ⚡ Performance Optimizations

For demo stability and responsiveness:

* Fast fallback responses when API is slow
* Reduced latency (~5–7 seconds)
* Optimized prompts
* Retrieval pipeline improvements
* Disabled telemetry errors
* Improved caching behavior
* Rate-limit handling (429 retry logic)

---

## 🧠 System Architecture

```
User (Web Interface)
        │
        ▼
Frontend (HTML + CSS + JS + Voice + Maps)
        │
        ▼
FastAPI Backend Server
        │
        ├── Emergency Detection Engine
        │
        ├── Language Detection & Translation
        │
        ├── Retrieval Engine (ChromaDB Vector Search)
        │         │
        │         ├── Medical Guidelines
        │         ├── Symptom Patterns
        │         └── Case Database
        │
        ├── Confidence Scoring Engine
        │
        ├── Hospital Location Engine
        │
        ├── Azure OpenAI LLM
        │
        ▼
Structured Safe Response
        │
        ▼
Voice Output + UI Rendering
```

---

## ⚙️ Technology Stack

### Frontend

* HTML5
* CSS3 (Animated Medical UI)
* JavaScript
* Web Speech API (Voice input/output)
* Geolocation API
* Google Maps Navigation

### Backend

* FastAPI
* Python 3.11+
* Azure OpenAI
* ChromaDB (Vector Database)
* Uvicorn

### AI & NLP

* Retrieval Augmented Generation (RAG)
* Embeddings for semantic search
* Translation services
* Confidence scoring algorithms

---

## 📂 Project Structure

```
healthcare-ai-assistant/
│
├── backend/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── data/
│   │   └── hospitals.json
│   ├── index.html
│   ├── hospitals.html
│   ├── schemes.html
│   ├── helplines.html
│   ├── app.js
│   ├── hospitals.js
│   └── style.css
│
├── chroma_db/
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/swasthya-setu-ai.git
cd healthcare-ai-assistant
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create `.env` file:

```
AZURE_API_KEY=your_key
AZURE_ENDPOINT=your_endpoint
CHAT_DEPLOYMENT=your_model
```

### 5️⃣ Run Backend

```bash
uvicorn backend.main:app --reload --port 8000
```

### 6️⃣ Run Frontend

Use VS Code Live Server or open:

```
frontend/index.html
```

---

## 🔗 API Endpoints

### Chat Endpoint

```
POST /chat
```

Request:

```json
{
  "query": "I have fever and cough"
}
```

Response:

```json
{
  "status": "SUCCESS",
  "risk_level": "LOW",
  "confidence": 82,
  "message": "Possible viral infection..."
}
```

---

### Government Scheme Endpoint

```
POST /scheme
```

Request:

```json
{
  "query": "Ayushman Bharat"
}
```

---

## 🧪 Demo Scenarios

Try queries like:

* "I have fever and headache"
* "Chest pain and difficulty breathing"
* "Ayushman Bharat scheme"
* "High sugar symptoms"
* "Find hospitals near me"

Voice input also supported 🎤

---

## 🔐 Safety & Guardrails

The system is designed with safety-first principles:

* No medical diagnosis
* No prescription recommendations
* Emergency override priority
* Confidence threshold enforcement
* Verified context grounding

---

## 📈 Future Improvements

* WhatsApp integration using Twilio
* Doctor appointment booking
* Offline rural deployment
* Mobile app version
* Real medical dataset integration
* Real-time hospital availability

---

## 🏆 Hackathon Value Proposition

This project demonstrates:

* AI for social impact
* Healthcare accessibility innovation
* Responsible AI with guardrails
* Multilingual human-AI interaction
* End-to-end full-stack engineering

---

## 👨‍💻 Authors

Developed by:

**Danish Sidiq**
AI / ML Engineer & Full Stack Developer

---

## 📜 License

This project is intended for educational and research purposes.

---

## ⭐ Acknowledgements

* Azure OpenAI
* FastAPI Community
* ChromaDB
* Web Speech API
* Government Health Resources

---

## ❤️ Vision

> AI should not replace doctors — it should help people reach them faster.

SWASTHYA SETU AI aims to empower communities with accessible healthcare intelligence.
