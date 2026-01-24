# ManaDude_FoodChatBot
This is a NLP project for online food ordering and tracking using Dialogflow, Python, FastAPI, SQL

# 🍔 Online Food Ordering Website with FoodChatBot (Production-Grade)

A **production-ready online food ordering website** integrated with a **FoodChatBot** powered by **Dialogflow ES** and a **FastAPI (Uvicorn) backend**.  
This system enables users to browse food items, place orders, and check order status via a conversational chatbot.

---

## 📌 Project Overview

This project demonstrates a **modern chatbot-driven food ordering workflow**:

- Customers interact with the website
- The chatbot handles menu queries, orders, and order status
- Backend services process requests securely
- Designed with scalability and production best practices in mind

---

## 🚀 Key Features

- 🌐 Responsive food business website
- 📋 Indian food menu (veg-focused)
- 🤖 Dialogflow-powered FoodChatBot
- 🔁 FastAPI webhook backend
- 🧩 Clean separation of frontend & backend
- 🔒 Secure request handling & validation
- 🧪 Easy testing with Swagger & ngrok

---

## 🍽️ Menu Items

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

### Frontend
- HTML5
- CSS3
- JavaScript (Vanilla)

### Backend
- Python 3.10+
- FastAPI
- Uvicorn

### Chatbot
- Dialogflow ES
- Webhook-based fulfillment

### Database (Optional / Extensible)
- MySQL
- mysql-connector-python

### Dev & Testing Tools
- ngrok
- Swagger UI
- Postman

---

## 📁 Project Structure

```
ManaDude_FoodChatBot/
│── Frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
│── Backend/
│   ├── main.py
│   ├── db_helper.py
|   ├── generic_helper.py
│   └── requirements.txt
│
│── README.md
│── .gitignore
```

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

### 3️⃣ Install Backend Dependencies
```bash
pip install -r Backend/requirements.txt
```

---

### 4️⃣ Run FastAPI Server
```bash
python -m uvicorn Backend.main:app --reload
```

Backend available at:
```
http://127.0.0.1:8000
```

Swagger API docs:
```
http://127.0.0.1:8000/docs
```

---

## 🌍 Exposing Webhook Using ngrok

```bash
ngrok http 8000
```

Copy the HTTPS URL and configure it in Dialogflow.

---

## 🤖 Dialogflow Webhook Configuration

| Setting | Value |
|------|------|
| Method | POST |
| Webhook URL | `https://xxxx.ngrok-free.app/` |
| Response Type | JSON |
| Fulfillment | Enabled |


---

## 🔐 Security & Best Practices

- Never commit secrets to Git
- Use `.env` files for credentials
- Validate Dialogflow payloads
- Treat order IDs as strings/integers (not floats)
- Session IDs are **conversation-based**, not user identity
- Use parameterized SQL queries

---

## 🧪 Testing & Debugging

- Swagger UI for API testing
- Dialogflow Test Console
- ngrok Inspector:
```
http://127.0.0.1:4040
```

---

## 🚀 Deployment Recommendations

- Frontend: Netlify / Vercel / S3
- Backend: AWS EC2 / ECS / GCP Cloud Run
- Database: RDS / Cloud SQL
- Reverse proxy: Nginx
- HTTPS: Cloudflare / Load Balancer

---

## 🔮 Future Enhancements

- 🛒 Cart & checkout
- 💳 Payment gateway integration
- 🔐 User authentication
- 📦 Order tracking
- 📊 Admin dashboard
- ☁️ CI/CD pipeline

---

## 👨‍💻 Author

**Venkata Sandeep Addala**  
AI Engineer | Python | FastAPI | Chatbots

---

## 📄 License

MIT License

---

### 🧠 Summary
A scalable, chatbot-first online food ordering system designed with real-world production standards.
