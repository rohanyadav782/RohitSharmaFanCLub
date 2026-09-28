# 🏏 Rohit Sharma FanClub

### AI-Powered Cricket Analytics, Prediction & Fan Engagement Platform

<p align="center">
  <b>📊 Cricket Analytics • 🤖 Machine Learning • 📰 Live News • 💬 AI Assistant • 👤 Fan Profiles</b>
</p>

<p align="center">
  <a href="https://rohitsharmafanclub.streamlit.app/">🚀 Live Demo</a> •
  <a href="https://github.com/rohanyadav782/RohitSharmaFanCLub">💻 GitHub Repository</a>
</p>

---

## 📌 About The Project

**Rohit Sharma FanClub** is an interactive cricket analytics and fan-engagement web application built around Rohit Sharma's cricket career.

The project combines **Data Science, Machine Learning, Data Visualization, PostgreSQL, APIs, and Generative AI** into a single Streamlit application.

Instead of being just a fan page, the platform allows users to explore cricket statistics, view analytics dashboards, get performance predictions, read cricket news, interact with an AI assistant, and maintain their own fan profile.

---

## ✨ Key Features

### 🏠 Home

A central landing page providing quick access to the different sections of the application.

### 🏏 Fan Club

- Rohit Sharma career information
- Cricket images and memories
- Fan-oriented content
- User interaction and profile-based experience

### 🤖 Performance Prediction

Machine Learning models are used to estimate Rohit Sharma's performance based on match-related features.

The prediction module includes:

- Multiple ML Models
- Feature preprocessing
- Feature engineering
- Model evaluation
- Serialized ML models
- Probability-based prediction
- Support for formats such as **ODI, T20, Test and IPL**

### 📊 Cricket Analytics Dashboard

Interactive dashboards provide insights into:

- Runs
- Batting average
- Strike rate
- 4s & 6s
- 50s & 100s
- Performance trends
- Opponent-wise performance
- Format-wise statistics
- Match-level analysis

### 📰 Cricket News

The application fetches cricket-related news using **Google News RSS feeds**.

`Requests` is used to retrieve the feed and `Feedparser` processes the RSS response to extract headlines. Duplicate headlines are removed before displaying the news.

### 💬 AI Cricket Assistant

An AI-powered assistant allows users to interact with the application and ask cricket-related questions.

### 👤 User Authentication & Profiles

The application includes a user authentication system backed by PostgreSQL.

Users can:

- Create an account
- Login
- Maintain their profile
- Store user information
- Access personalized fan features

### 🖼️ Upload Rohit Memories

Users can upload and share Rohit Sharma-related images and memories through the application.

---

# 🧠 Machine Learning

The prediction module follows a complete ML workflow:

```text
Cricket Data
     ↓
Data Cleaning
     ↓
Feature Engineering
     ↓
Feature Selection
     ↓
Preprocessing
     ↓
Train/Test Split
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Model Serialization
     ↓
Streamlit Prediction Interface
```

### Models Used

| Model | Purpose |
|---|---|
| XGBoost | Main performance prediction model |
| Decision Tree | Model experimentation |
| Random Forest | Ensemble model comparison |

The final prediction interface uses the trained models and preprocessing pipeline saved from the training stage.

---

# 📊 Data & Analytics

The project uses cricket match and player-performance data containing features such as:

- Match ID
- Opponent
- Format
- Venue
- Month
- Year
- Strike Rate
- Fours
- Sixes
- Balls
- Runs
- Performance indicators
- Match date

Feature engineering and statistical techniques are applied before model training.

---

# 🛠️ Tech Stack

### Programming & Data Science

- 🐍 Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost

### Web Application

- Streamlit

### Database

- PostgreSQL
- Neon

### Data Visualization

- Plotly
- Power BI
- Streamlit Charts

### APIs & Data Collection

- Google News RSS
- Requests
- Feedparser
- SMS Gateway APIs
- CricBuzz

### AI

- Generative AI / Gemini
- AI Cricket Assistant

### Deployment & Development

- Git
- GitHub
- Streamlit Cloud

---

# 🏗️ Application Architecture

```text
                    ┌─────────────────────┐
                    │    Cricket Data     │
                    │ APIs / RSS / Excel  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Processing &    │
                    │ Feature Engineering │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
       ┌─────────────────┐          ┌─────────────────┐
       │ Machine Learning│          │ Cricket         │
       │ Models          │          │ Analytics       │
       └────────┬────────┘          └────────┬────────┘
                │                            │
                └──────────────┬─────────────┘
                               ▼
                    ┌─────────────────────┐
                    │     Streamlit       │
                    │     Application     │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
       ┌──────────┐      ┌───────────┐    ┌────────────┐
       │PostgreSQL│      │ AI         │    │ Live News  │
       │  / Neon  │      │ Assistant  │    │   Feed     │
       └──────────┘      └───────────┘    └────────────┘
```

---

# 📂 Project Structure

```text
RohitSharmaFanCLub/
│
├── main.py
├── home.py
├── fan_page.py
├── loginpage.py
├── prediciton.py
├── dashboard.py
├── Ai.py
│
├── cricket_feature_engineered.xlsx
├── model.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

> File names may change as the project evolves.

---

# 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/rohanyadav782/RohitSharmaFanCLub.git
```

### 2. Move into the project directory

```bash
cd RohitSharmaFanCLub
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file and add your required credentials:

```env
DATABASE_URL=your_neon_database_url
GEMINI_API_KEY=your_gemini_api_key
EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_app_password
```

**Never commit your `.env` file or API keys to GitHub.**

### 6. Run the application

```bash
streamlit run main.py
```

---

# 🌐 Live Application

🚀 **Try the application:**

https://rohitsharmafanclub.streamlit.app/

---

# 🔐 Security

Sensitive credentials are handled through environment variables.

The project uses:

- `.env`
- Streamlit secrets/environment configuration
- PostgreSQL connection credentials
- API keys outside the source code

Sensitive files should remain excluded through `.gitignore`.

---

# 🎯 What I Learned From This Project

This project helped me work across different parts of a real-world data application:

- Collecting data from external sources
- Data cleaning and feature engineering
- Machine Learning model development
- Model evaluation and serialization
- Building interactive dashboards
- Working with PostgreSQL/NeonDB
- User authentication
- API/RSS integration
- Generative AI integration
- Streamlit application development
- Git/GitHub workflow
- Cloud deployment
- Managing environment variables and secrets

---

# 🔮 Future Improvements

Some planned improvements include:

- 📈 More advanced player-performance models
- 🧠 Deep Learning-based prediction
- 🏏 More cricket players
- 📊 Real-time match analytics
- 🔔 Personalized cricket notifications
- 🖼️ AI-powered image classification
- 📱 Improved mobile UI
- 📅 Match prediction and upcoming-match analysis

---

# 👨‍💻 Author

### Rohan Bholaram Yadav

**Data Science | Machine Learning | Python | Analytics**

📌 Built as a hands-on project combining cricket, data science and full-stack application development.

---

## ⭐ Support

If you find this project interesting, consider giving the repository a ⭐ on GitHub.

```text
🏏 Cricket + 📊 Data Science + 🤖 AI
             ↓
      Rohit Sharma FanClub
```

**Thanks for visiting! 🚀**
