🏥 SWASTHYA SETU AI

Multilingual Rural Healthcare Assistant with Emergency Intelligence

SWASTHYA SETU AI is a multilingual healthcare assistant designed to provide symptom-based guidance, government scheme awareness, hospital discovery, and emergency escalation support for rural and semi-urban communities.

The system combines AI intelligence, voice interaction, and location-aware services to improve healthcare accessibility and awareness.

🎯 Problem Statement & Goals

Healthcare accessibility in India — especially in rural and underserved areas — faces major challenges:

Limited doctor availability

Language barriers for non-English speakers

Lack of awareness about government schemes

Delayed emergency response

Difficulty locating nearby hospitals quickly

Dependence on intermediaries (ASHA workers)

SWASTHYA SETU aims to bridge these gaps by offering:

AI-powered symptom guidance

Multilingual voice interaction

Emergency detection with escalation

Nearby hospital discovery with navigation

Government healthcare scheme awareness

Safety-first medical information delivery

🚀 Key Features
🤖 1. AI Symptom Guidance Chatbot

Accepts natural language symptom queries

Provides structured health guidance:

Possible causes

Home care suggestions

Doctor consultation advice

Emergency signs

Safety guardrails prevent diagnosis or prescriptions

Confidence scoring system

Risk classification (LOW / MODERATE / CRITICAL)

🗣️ 2. Multilingual Voice Assistant

Female voice support

English and Hindi language modes

Speech-to-text input

Text-to-speech output

Talking medical avatar animation

Manual voice toggle (user control)

🚨 3. Smart Emergency Detection System

Improved emergency pipeline with:

Context-aware detection (avoids false alarms like cough)

Critical symptom recognition:

Chest pain

Stroke symptoms

Unconsciousness

Severe bleeding

Breathing difficulty

Instant emergency instructions

Ambulance helpline integration

🏥 4. Hospital Locator with Navigation (NEW ⭐)

One of the most impressive features for demo.

Capabilities:

Detect user GPS location

Manual location entry (JP Nagar, Banashankari, etc.)

Nearest hospitals ranking using distance calculation

Government + private hospitals dataset

Google Maps navigation button

Driving route guidance from user location

Dataset includes:

Bengaluru Central hospitals

Contact numbers

Addresses

Coordinates

📋 5. Government Health Schemes Assistant

Structured information display:

Description

Eligibility

Benefits

Official Source

Examples:

Arogya Karnataka

Ayushman Bharat

State schemes

System detects scheme queries and formats response cleanly.

📞 6. Medical Helplines Directory

Emergency helplines

National health numbers

Mental health support lines

Women and child helplines

🧠 7. AI Safety & Guardrails

The assistant follows strict medical safety rules:

No diagnosis

No medicine prescriptions

Encourages doctor consultation

Emergency escalation when needed

Clear disclaimers

⚡ Performance Improvements

For demo readiness:

Fast response fallback system (5-7 seconds)

Reduced API delays

Local response generation when API is slow

Optimized prompt engineering

Disabled unnecessary telemetry

Improved retrieval efficiency

🏗️ System Architecture
                User (Web / Mobile)
                        │
                        ▼
                Frontend Interface
        (HTML + CSS + JavaScript + Voice)
                        │
                        ▼
                FastAPI Backend Server
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
 Emergency Engine   RAG Retrieval     Scheme Engine
        │               │                │
        ▼               ▼                ▼
   Risk Detection   ChromaDB Vector   Structured Data
                        │
                        ▼
                Azure OpenAI LLM
                        │
                        ▼
                Safe Response Generator
                        │
                        ▼
                    Frontend

🧩 Technology Stack
Frontend

HTML5

CSS3

JavaScript

Web Speech API

Geolocation API

Google Maps Navigation

Backend

FastAPI

Python

Azure OpenAI (GPT-4.1)

ChromaDB Vector Database

RAG (Retrieval Augmented Generation)

AI Components

Prompt Engineering

Confidence Engine

Emergency Detection Pipeline

Language Translation Layer

📂 Project Structure
healthcare-ai-assistant/
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── services/
│   │   ├── rag_services.py
│   │   ├── llm_service.py
│   │   ├── retrieval_service.py
│   │   ├── emergency_engine.py
│   │   ├── language_service.py
│   │   └── case_loader.py
│   ├── database/
│   │   └── chroma_client.py
│   └── models/
│
├── frontend/
│   ├── index.html
│   ├── hospitals.html
│   ├── schemes.html
│   ├── helplines.html
│   ├── app.js
│   ├── hospitals.js
│   ├── style.css
│   └── data/
│       ├── hospitals.json
│       └── helplines.json
│
└── requirements.txt

🧪 How to Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Activate Virtual Environment
.venv\Scripts\activate

3️⃣ Run Backend
python -m uvicorn backend.main:app --reload --port 8000

4️⃣ Run Frontend

Open:

frontend/index.html


or use Live Server.

🌍 Future Enhancements

WhatsApp chatbot integration

PHC appointment booking

Regional language expansion

Offline AI model support

Doctor teleconsultation

Medical image analysis

⚠️ Medical Disclaimer

This system provides educational and informational guidance only.

It does NOT:

Diagnose diseases

Prescribe medications

Replace professional medical consultation

Always consult a qualified healthcare provider for medical concerns.

In emergencies, contact local emergency services immediately.

👨‍💻 Team

Developed as part of an AI healthcare innovation project.

Team Members:

Danish Sidiq
