# 🍽️ ManaDude_FoodChatBot (NLP Project)

ManaDude_FoodChatBot is an **NLP-based conversational AI project** for **online food ordering and order tracking**, built using **Dialogflow ES**, **Python**, **FastAPI**, and **SQL**.

This project focuses on **Natural Language Understanding (NLU)**, intent classification, entity extraction, and backend fulfillment logic.

---

## 📌 Project Overview

This project demonstrates how a **chatbot-driven food ordering system** can be implemented using NLP techniques:

- Users interact with a chatbot (text-based)
- Dialogflow handles **intent detection & entity extraction**
- FastAPI processes webhook requests
- SQL database manages orders and statuses
- Responses are sent back as conversational replies

The core emphasis is on **NLP, conversational flow design, and backend integration**.

---

## 🧠 NLP Scope & Capabilities

- Intent classification (Order Food, Track Order, Cancel Order, etc.)
- Entity extraction (food item, quantity, order ID)
- Context-based multi-turn conversations
- Session-aware request handling
- Rule-based fulfillment logic
- Robust fallback handling

---

## 🚀 Key Features

- 🤖 Dialogflow-powered FoodChatBot
- 🧠 NLP-based intent & entity processing
- 🔁 FastAPI webhook backend
- 🗄️ SQL-based order persistence
- 🔒 Secure and validated webhook handling
- 🧪 Easy testing with Swagger & ngrok
- 📦 Modular backend helper utilities

---

## 🍽️ Supported Menu Items

- Pav Bhaji  
- Chole Bhature  
- Pizza  
- Mango Lassi  
- Masala Dosa  
- Biryani  
- Vada Pav  
- Rava Dosa  
- Samosa  

---

## 🧰 Technology Stack

### NLP & Chatbot
- Dialogflow ES
- System & custom entities
- Contexts & follow-up intents

### Backend
- Python 3.10+
- FastAPI
- Uvicorn

### Database
- SQL (MySQL compatible)
- mysql-connector-python

### Dev & Testing Tools
- ngrok
- Swagger UI
- Postman

---

## 📁 Project Structure

```
ManaDude_FoodChatBot/
│── Backend/
│   ├── main.py              # FastAPI webhook entry point
│   ├── db_helper.py         # Database access utilities
│   ├── generic_helper.py   # NLP & response helpers
│   └── requirements.txt
│
│── README.md
│── .gitignore
```

> Note: Frontend/UI is intentionally excluded — this is an **NLP-focused backend project**.

---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/venkata-sandeep-addala/ManaDude_FoodChatBot.git
cd ManaDude_FoodChatBot
```

---

### 2️⃣ Create & Activate Virtual Environment
```bash
python -m venv venv
```

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies
```bash
pip install -r Backend/requirements.txt
```

---

### 4️⃣ Run FastAPI Webhook Server
```bash
python -m uvicorn Backend.main:app --reload
```

Backend runs at:
```
http://127.0.0.1:8000
```

Swagger docs:
```
http://127.0.0.1:8000/docs
```

---

## 🌍 Exposing Webhook Using ngrok

```bash
ngrok http 8000
```

Copy the generated HTTPS URL and configure it in Dialogflow.

---

## 🤖 Dialogflow Webhook Configuration

| Setting | Value |
|------|------|
| Method | POST |
| Webhook URL | `https://xxxx.ngrok-free.app/` |
| Fulfillment | Enabled |
| Response Type | JSON |

### Sample Webhook Response
```json
{
  "fulfillmentText": "Your order has been placed successfully!"
}
```

---

## 🔐 Security & Best Practices

- Never commit credentials or tokens
- Use environment variables for DB config
- Validate Dialogflow payload structure
- Convert numeric parameters safely (float → int)
- Do not treat session IDs as user identity
- Use parameterized SQL queries only

---

## 🧪 Testing & Debugging

- Dialogflow Test Console
- Swagger UI (`/docs`)
- Postman for webhook simulation
- ngrok Inspector:
```
http://127.0.0.1:4040
```

---

## 🔮 Future Enhancements

- ML-based intent confidence scoring
- Recommendation engine
- Multilingual support
- Voice assistant integration
- Redis-based session caching
- Analytics on user intents

---

## 👨‍💻 Author

**Venkata Sandeep Addala**  
AI / NLP Engineer | Python | FastAPI | Conversational AI

---

## 📄 License

MIT License

---

### 🧠 Summary
A clean, production-aligned **NLP chatbot project** for food ordering and tracking, showcasing real-world Dialogflow and FastAPI integration.
