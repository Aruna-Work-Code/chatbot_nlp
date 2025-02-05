

# 🛍️ Hopper Chatbot  

**Hopper Chatbot** is an AI-powered chatbot designed for seamless integration with **e-commerce websites**. Using **Natural Language Processing (NLP)** with **Dialogflow**, this chatbot enables customers to place new orders, modify existing ones, track their purchases, and receive real-time updates.  

This chatbot is built with **FastAPI**, leveraging **MySQL** as its database backend for efficient order management and transaction processing.  

  ## ✨ Key Features  
- **🛒 Order Management** – Users can place new orders, add items, remove items, and complete transactions.  
- **📦 Order Tracking** – Users can check the status of their orders in real-time using order ID tracking.  
- **💬 NLP-Powered Conversations** – Uses Dialogflow to understand and process customer queries.  
- **⚡ FastAPI Webhook Integration** – The chatbot processes requests efficiently using FastAPI and integrates with Dialogflow.  
- **📊 MySQL Database Integration** – Securely stores and retrieves order details and customer interactions, managed in a MySQL database.
- **🔄 Session-Based Context Handling** – Maintains user context for personalized and smooth interactions.
- **🔄Context-Aware Responses**: Uses session-based tracking to maintain context throughout conversations.
   
## 🛠️ Technology Stack  
- **Backend:** Python (FastAPI) - Core programming language for API and database interactions.
- **NLP Engine:** Dialogflow - For NLP-based intent recognition.
- **Database:** MySQL - For order storage, tracking, and retrieval.
- **Framework:** FastAPI for API handling - For handling chatbot requests and responses

## Files Overview  
- **`main.py`** – The primary FastAPI webhook handling user requests and managing order operations.  
- **`db_helper.py`** – Database functions for inserting, retrieving, and managing orders.  
- **`generic_helper.py`** – Utility functions for processing chatbot requests and extracting session details.

 ## 📂 Project Structure  
📦 Hopper Chatbot  
│-- main.py          # FastAPI server and webhook handler  
│-- db_helper.py     # Database operations (order tracking, insertion, retrieval)  
│-- generic_helper.py # Helper functions for request processing  
│-- requirements.txt  # Dependencies and package requirements  

## 🔧 How It Works  
1. A user interacts with the chatbot on the e-commerce website.  
2. The chatbot processes the request using **Dialogflow** and Dialogflow detects the intent (e.g., new order, track order, modify order).
3. The request is processed through **FastAPI webhook**, which calls the appropriate function.
4. The chatbot interacts with the **MySQL database** to retrieve or store order details.   
5. The chatbot provides a response based on order details or user requests (e.g., order status, total price, confirmation).  

## 📌 Example User Interactions  
**User:** "I want to order a red dress and a blue top."  
**Chatbot:** "Added Red Dress and Blue Top to your cart. Do you need anything else?"  
**User:** "Track my order #1234."  
**Chatbot:** "Your order #1234 is currently out for delivery!"
**User:** "Track my order #5678."
**Chatbot:** "Your order #5678 is currently being processed and will be shipped soon!"  

## Use Case: E-Commerce Integration  
Hopper Chatbot is designed specifically for integration with **online dress stores**, enhancing customer experience by providing quick and automated order processing.  
This chatbot can be extended further with additional e-commerce functionalities, including payment processing and personalized recommendations.

## 🚀 Installation & Setup  

### Prerequisites  
Ensure you have the following installed:  
- Python 3.8+  
- MySQL Database  
- FastAPI  
- Dialogflow Account  

### Steps to Run the Chatbot Locally  
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/hopper-chatbot.git  
   cd hopper-chatbot  
   ```  
2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt  
   ```  
3. **Set Up MySQL Database**  
   - Create a database in MySQL  
   - Configure database credentials in `db_helper.py`  
   ```python
   cnx = mysql.connector.connect(
       host="localhost",
       user="your_mysql_user",
       password="your_mysql_password",
       database="your_database"
   )
   ```  
4. **Run FastAPI Server**  
   ```bash
   uvicorn main:app --reload  
   ```  
5. **Integrate with Dialogflow**  
   - Set up intents (e.g., `order.add`, `order.track`, `order.complete`).  
   - Link the webhook to FastAPI using the provided endpoint.
   
## 📈 Future Enhancements  
- **🔗 Payment Gateway Integration** for seamless transactions.  
- **🛍️ Personalized Recommendations** based on user preferences.  
- **🗣️ Voice-Based Chatbot** for enhanced user experience, better accessibility.  
- **🌍 Multilingual Capabilities** for broader accessibility or global reach.  
---
For any inquiries or contributions, feel free to reach out. 🚀
