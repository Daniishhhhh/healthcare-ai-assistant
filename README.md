🏥 SWASTHYA SETU
Multilingual Rural Healthcare Assistant

SWASTHYA SETU is a multilingual, AI-powered rural healthcare assistant designed to provide symptom-based health guidance, nearby hospital discovery, government health scheme awareness, and emergency escalation support.

The system focuses on improving healthcare accessibility for rural and semi-urban populations by leveraging AI intelligence, voice interaction, and location-aware services.

🎯 Problem Statement & Goals

Rural healthcare in India faces critical challenges such as:

Limited doctor availability at Primary Health Centres (PHCs)

Language barriers for non-English speakers

Delayed emergency response

Lack of awareness about government healthcare schemes

Difficulty locating nearby hospitals quickly

Heavy dependence on ASHA workers for first-level care

SWASTHYA SETU aims to bridge these gaps by offering:

Easy access to AI-based health triage

Multilingual support for rural users

Emergency risk detection

Nearby hospital navigation

Government scheme awareness

Safety-first medical guidance

🚀 Core Features
🤖 AI Symptom Guidance Assistant

The chatbot accepts natural language queries and provides structured medical guidance including:

Possible causes

Safe home care suggestions

When to consult a doctor

Emergency warning signs

Confidence score and risk level

The system follows strict medical safety rules to prevent misuse.

🗣️ Multilingual Voice Assistant

The assistant supports interactive voice communication:

Female voice output (English & Hindi)

Speech-to-text symptom input

Text-to-speech responses

Talking medical avatar animation

Voice ON/OFF toggle control

Language switch support

🚨 Smart Emergency Detection System

The emergency pipeline intelligently detects high-risk situations while avoiding false alarms.

Recognizes symptoms like:

Chest pain

Stroke indicators

Unconsciousness

Severe bleeding

Breathing difficulty

Seizures

Provides:

Immediate emergency guidance

Ambulance contact instructions

Critical risk classification

🏥 Hospital Locator with Navigation ⭐

One of the most impactful features of the system.

Users can:

Detect current GPS location

Enter location manually (JP Nagar, Banashankari, etc.)

Find nearest hospitals

View contact details and address

Navigate using Google Maps

Get driving route guidance

Dataset includes:

Government hospitals

Private hospitals

Bengaluru Central region coverage

📋 Government Health Schemes Assistant

The system provides structured information for healthcare schemes including:

Description

Eligibility

Benefits

Official source

Examples:

Arogya Karnataka

Ayushman Bharat

State welfare schemes

📞 Medical Helplines Directory

Users can access important helpline numbers:

Ambulance services

National health helplines

Mental health support

Women & child support lines

🧠 AI Safety & Guardrails

The assistant strictly follows medical safety guidelines:

No disease diagnosis

No medicine prescriptions

Encourages professional consultation

Provides clear disclaimers

Escalates emergencies when needed

⚡ Performance Optimizations

For demo reliability and speed:

Fast fallback response when API is slow

Reduced latency (≈5–7 seconds)

Optimized prompt engineering

Retrieval efficiency improvements

Telemetry disabled to reduce noise

Stable multilingual processing

🏗️ System Architecture
User (Web Interface)
        │
        ▼
Frontend (HTML + CSS + JS + Voice)
        │
        ▼
FastAPI Backend Server
        │
 ┌──────────────┬──────────────┬
 ▼              ▼              ▼
Emergency     Retrieval      Scheme
Engine        Engine         Engine
 │              │              │
 ▼              ▼              ▼
Risk Logic   ChromaDB        Structured Data
        │
        ▼
Azure OpenAI (GPT Model)
        │
        ▼
Safe Response Generator
        │
        ▼
Frontend Output + Voice

🧩 Technology Stack
Frontend

HTML5

CSS3

JavaScript

Web Speech API

Geolocation API

Google Maps Integration

Backend

FastAPI

Python

Azure OpenAI GPT-4.1

ChromaDB Vector Database

Retrieval Augmented Generation (RAG)

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
│   ├── database/
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
│
└── requirements.txt

🧪 How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Activate Environment
.venv\Scripts\activate

3️⃣ Run Backend
python -m uvicorn backend.main:app --reload --port 8000

4️⃣ Run Frontend

Open:

frontend/index.html


(or use Live Server)

🌍 Future Enhancements

WhatsApp chatbot integration

PHC appointment booking system

Regional language expansion

Offline AI support

Telemedicine integration

Health record storage

⚠️ Medical Disclaimer

This system provides informational and educational guidance only.

It does NOT:

Diagnose diseases

Prescribe medications

Replace medical professionals

Always consult a qualified healthcare provider for medical concerns.

In emergencies, contact local emergency services immediately.

👨‍💻 Team

Developed as part of an AI Healthcare Innovation Project.

Team Members:

Danish Sidiq
