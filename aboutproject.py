import streamlit as st
import pandas as pd
from dataset import  Dataset
data = Dataset()
class AboutProject:
    def projectinfo(self):
        st.write("""
        ### 🏏 The Rohit Sharma FanClub
    
        The **Rohit Sharma FanClub** is a **full-stack, AI-powered cricket application**
        built around the career, performance, and statistics of Indian cricketer
        **Rohit Sharma**.
    
        The project combines **Data Science, Machine Learning, Data Visualization,
        Database Management, Web Development, Authentication, and Generative AI**
        into a single **Streamlit-based application**.
    
        The main objective of the project is to transform **raw cricket match data**
        into useful **insights and predictions** while also providing an interactive
        platform for **Rohit Sharma fans**.
        """)
        st.subheader("The Application provides :")
        st.write("""
        ### 🚀 Key Features
    
        - 🏏 **Rohit Sharma Career Information**
        - 📊 **Interactive Cricket Statistics**
        - 📈 **Performance Dashboards**
        - 🤖 **Machine Learning-Based Run Prediction**
        - 🔮 **Prediction of Whether Rohit Sharma Can Score 30+ Runs**
        - 🧠 **AI-Powered Cricket Assistant**
        - 👤 **User Registration and Login**
        - 📧 **OTP Verification**
        - 💾 **NeonDB  Integration**
        - 🖼️ **Rohit Sharma Fan Memories**
        - 📱 **Responsive and Interactive Streamlit Interface**
        """)
        st.subheader("🚀 How Was This Project Built?")

        st.write("""
    
    The project was developed **step-by-step**, starting from **raw cricket data**
    and gradually transforming it into a complete **full-stack, AI-powered cricket
    application**.
    
    The development process covered everything from **data collection and data
    cleaning** to **feature engineering, machine learning, data visualization,
    database integration, authentication, and application deployment**.
    """)
        st.subheader("🔄 Complete Development Pipeline")

        st.write("""
    
        **Data Collection → Data Understanding → Data Cleaning → Feature Engineering
        → Exploratory Data Analysis → Machine Learning → Model Evaluation
        → Model Saving → Database Integration → Backend Development
        → Frontend Development → Authentication → AI Assistant → Testing → Deployment**
        """)
        st.divider()
        st.header("🎯 Problem Statement")
        st.write("""
        Traditional cricket statistics mainly provide historical information.

        For example:

        - How many runs did a player score?
        - What is his strike rate?
        - How did he perform against a particular opponent?
        - What is his performance at a particular venue?

        But historical statistics alone don't provide a predictive interface.

        The objective of this project was therefore to build a platform that can:
        """)
        st.write("""

        - 📊 Analyze historical batting performance.
        - 🔍 Identify important performance patterns.
        - 🤖 Predict the probability of scoring 30+ runs.
        - 📈 Estimate expected runs.
        - 🎛️ Allow users to explore performance interactively.
        - 🧠 Provide an AI-powered cricket assistant.
        - 🖼️ Provide fan-oriented media functionality.
        """)


    def architecture(self):
        st.write("### 🏗️ Project Architecture")

        st.code("""
                                 CRICKET DATA
                                      │
                                      ▼
                              DATA COLLECTION
                                      │
                                      ▼
                             DATA PREPROCESSING
                                      │
                                      ▼
                           EXPLORATORY DATA ANALYSIS
                                      │
                                      ▼
                             FEATURE ENGINEERING
                                      │
                            ┌─────────┴─────────┐
                            ▼                   ▼
                      WOE / IV ANALYSIS        VIF
                            │                   │
                            └─────────┬─────────┘
                                      ▼
                               MODEL TRAINING
                                      │
                                      ▼                                
                               CLASSIFICATION                     
                                      │                                
                                      ▼                                
                                  DT/RF/XGB               
                                      │
                                      ▼
                            Random Forest(Final Model)
                                      │
                                      ▼
                              MODEL SERIALIZATION
                                      │
                                      ▼
                              STREAMLIT APPLICATION
                                      │
                          ┌───────────┼───────────┬───────────┐
                          ▼           ▼           ▼           ▼
                         ML      Dashboard      NeonDB      GenAI
                          │           │           │           │
                          └───────────┴───────────┴───────────┘
                                      │
                                      ▼
                                FINAL PLATFORM
        """, language="text")

    def datascience_journey(self):
        tab1,tab2=st.tabs(["🛠️ Technical Pipeline","👨🏻‍💻 Model Building Journey"])
        with tab1:
            # ============================================================
            # 📊 DATA SCIENCE JOURNEY
            # ============================================================

            st.subheader("📊 Data Science Journey")

            st.caption(
                "The data science pipeline transforms raw Rohit Sharma cricket data "
                "into meaningful insights, machine learning predictions, and an "
                "interactive cricket analytics platform."
            )

            # ============================================================
            # 1. DATA COLLECTION
            # ============================================================

            st.subheader("1️⃣ Data Collection")

            st.write(
                "Historical Rohit Sharma cricket data was collected using "
                "Cricbuzz-sourced information and Cricket API data. The raw "
                "information was converted into a structured dataset suitable "
                "for analysis and machine learning."
            )

            st.caption("Core dataset features")

            st.write("""
            - 🆔 Match_ID – Unique match identification
            - 🏏 Opponent – Opposition team
            - 🏟️ Venue – Match location
            - 🏆 Format – ODI, T20, TEST, IPL
            - 📅 Month & Year – Time-related information
            - ⚡ Strike Rate – Batting efficiency
            - 4️⃣ Fours & 6️⃣ Sixes – Boundary statistics
            - ⚾ Balls – Balls faced
            - 🏃 Runs – Runs scored
            - 🎯 Above 30 – Binary classification target
            - 📆 Date – Match date
            """)

            # ============================================================
            # 2. DATA CLEANING & PREPROCESSING
            # ============================================================

            st.subheader("2️⃣ Data Cleaning & Preprocessing")

            st.write(
                "The collected data was cleaned and transformed into a consistent "
                "machine-learning-ready format. Duplicate records, missing values, "
                "incorrect data types, and date-related issues were handled."
            )

            st.write("""
            - 🧹 Duplicate identification and removal
            - 🔧 Missing-value handling
            - 🔢 Data-type conversion
            - 📅 Date parsing and chronological sorting
            - 🏷️ Categorical and numerical variable preparation
            - 🎯 Target variable creation and validation
            """)

            st.caption("Example")

            st.code("""
            Score: 56(45)
            → Runs = 56
            → Balls = 45
    
            Test scores:
            78(101) + 45(50)
            → Runs = 123
            → Balls = 151
            """, language="text")

            # ============================================================
            # 3. TARGET VARIABLE
            # ============================================================

            st.subheader("3️⃣ Target Variable")

            st.write(
                "The main classification objective is to predict whether Rohit "
                "Sharma will score 30 or more runs in a match."
            )

            st.write("""
            - 🟢 Runs ≥ 30 → Yes / 1
            - 🔴 Runs < 30 → No / 0
            """)

            st.caption(
                "The 30-run threshold was selected as a practical performance "
                "indicator because crossing this level can represent a meaningful "
                "start in many cricket innings."
            )

            # ============================================================
            # 4. EXPLORATORY DATA ANALYSIS
            # ============================================================

            st.subheader("4️⃣ Exploratory Data Analysis (EDA)")

            st.write(
                "EDA was performed to understand batting patterns, trends, "
                "distributions, and relationships within the historical data."
            )

            st.write("""
            📊 Key analysis areas:
    
            - Performance by cricket format
            - Performance against different opponents
            - Strike-rate variation
            - Runs and boundary distribution
            - Performance trends over time
            - Top-performing opponents
            - Overall run distribution
            """)

            st.caption(
                "Charts and visualizations were used to convert numerical data "
                "into easily understandable cricket insights."
            )

            # ============================================================
            # 5. FEATURE ENGINEERING
            # ============================================================

            st.subheader("5️⃣ Feature Engineering")

            st.write(
                "Feature engineering transformed raw match information into "
                "meaningful predictive variables. Historical and contextual "
                "features were created to help the models learn batting patterns."
            )

            st.write("""
            - 📊 Historical average runs
            - 🏟️ Venue-based performance
            - 🆚 Opponent-based performance
            - 🏆 Format-based performance
            - 📅 Month-based information
            - 📈 Historical / rolling performance
            - ⚡ Strike rate, fours, sixes and balls
            """)

            st.caption(
                "Chronological ordering was maintained to reduce future-data "
                "leakage when creating historical features."
            )

            # ============================================================
            # 6. WOE
            # ============================================================

            st.subheader("6️⃣ WOE – Weight of Evidence")

            st.write(
                "Weight of Evidence (WOE) was explored to understand how different "
                "feature categories or bins distinguish between the two target classes."
            )

            st.caption(
                "Feature → Bins/Categories → Class Distribution → WOE → "
                "Target Relationship"
            )

            # ============================================================
            # 7. IV
            # ============================================================

            st.subheader("7️⃣ IV – Information Value")

            st.write(
                "Information Value (IV) was used with WOE to estimate the predictive "
                "strength of individual variables for separating the two target classes."
            )

            st.write("""
            | IV Range | Interpretation |
            |---|---|
            | < 0.02 | Very Weak |
            | 0.02 – 0.10 | Weak |
            | 0.10 – 0.20 | Medium |
            | 0.20 – 0.30 | Strong |
            | > 0.30 | Very Strong |
            """)

            st.caption(
                "These are general guidelines and should not be treated as absolute rules."
            )

            # ============================================================
            # 8. VIF
            # ============================================================

            st.subheader("8️⃣ VIF – Multicollinearity Analysis")

            st.write(
                "Variance Inflation Factor (VIF) was used to identify highly "
                "correlated predictors containing overlapping information."
            )

            st.write("""
            - 🔎 VIF ≤ 10 Feature Investigate 
            - ✅ VIF ≤ 5 → Feature retained
            - ❌ VIF > 10 → Feature considered for removal
            """)

            st.caption(
                "VIF analysis helps reduce multi-collinearity and improves "
                "feature interpretability."
            )

            # ============================================================
            # 9. MACHINE LEARNING MODELS
            # ============================================================

            st.subheader("9️⃣ Machine Learning Models")

            st.write(
                "Multiple classification algorithms were trained and compared "
                "to determine the most suitable model for predicting the 30+ runs outcome."
            )

            st.write("""
            🌳 **Decision Tree** – Learns decision rules using a tree structure.
    
            🌲 **Random Forest** – Combines multiple decision trees using an ensemble approach.
    
            🚀 **XGBoost** – Gradient boosting algorithm that sequentially improves model errors.
    
            """)

            # ============================================================
            # 10. MODEL COMPARISON
            # ============================================================

            st.subheader("🔟 Model Selection")

            st.write(
                "Models were compared using multiple evaluation metrics rather than "
                "accuracy alone. Precision, recall, F1-score, ROC-AUC and Gini were considered."
            )

            model_comparison = data.model_comparison
            st.dataframe(
                model_comparison,
                use_container_width=True,
                hide_index=True
            )

            st.success("🏆 Final Classification Model: RandomForest")

            # ============================================================
            # 12. MODEL EVALUATION
            # ============================================================

            st.subheader("1️⃣2️⃣ Model Evaluation")

            st.write(
                "The final model was evaluated using several classification metrics "
                "to understand both overall performance and the quality of positive predictions."
            )

            st.write("""
            - 🎯 **Accuracy** – Overall percentage of correct predictions
            - 🔍 **Precision** – Correctness of positive predictions
            - 📌 **Recall** – Ability to identify actual positive cases
            - ⚖️ **F1-Score** – Balance between precision and recall
            - 📈 **ROC-AUC** – Overall classification discrimination
            - 📊 **Confusion Matrix** – TP, TN, FP and FN analysis
            - 📉 **Precision-Recall Curve** – Precision/recall trade-off
            """)

            # ============================================================
            # 13. MODEL SERIALIZATION
            # ============================================================

            st.subheader("1️⃣3️⃣ Model Serialization")

            st.write(
                "After training and evaluation, the finalized model and required "
                "preprocessing components were serialized using Pickle. This allows "
                "the Streamlit application to load the trained model directly without "
                "retraining it for every prediction."
            )

            st.caption(
                "Training Dataset → Model Training → Trained Model → Pickle → "
                "Saved Model → Streamlit Prediction"
            )

            # ============================================================
            # 14. STREAMLIT APPLICATION
            # ============================================================

            st.subheader("1️⃣4️⃣ Streamlit Application")

            st.write(
                "The machine learning models, analytics, database and AI features "
                "were integrated into a complete Streamlit application. Users can "
                "interact with the system through an easy-to-use graphical interface."
            )

            st.write("""
            The application includes:
    
            🏠 **Home** – Project introduction and overview
    
            🏏 **Fan Page** – Rohit Sharma fan-oriented content
    
            🤖 **Prediction** – ML-based 30+ runs prediction
    
            📊 **Dashboard** – Interactive cricket statistics and visualizations
    
            🧠 **AI Assistant** – AI-powered cricket interaction
    
            ℹ️ **About Project** – Complete project and development information
            """)

            # ============================================================
            # 15. FULL-STACK INTEGRATION
            # ============================================================

            st.subheader("1️⃣5️⃣ Full-Stack Integration")

            st.write(
                "The final application combines the data science pipeline with "
                "database management, authentication, AI and interactive web development."
            )

            st.write("""
            💾 **NeonDB** – Stores user and application data
    
            🔐 **Authentication** – User registration and login system
    
            📧 **OTP System** – Account verification and security
    
            🧠 **Generative AI** – AI-powered cricket assistant
    
            🖼️ **Fan Memories** – Rohit Sharma fan media functionality
    
            🖥️ **Streamlit** – Frontend and application interface
            """)

            # ============================================================
            # 🚀 COMPLETE END-TO-END PIPELINE
            # ============================================================

            st.subheader("🚀 Complete End-to-End Pipeline")

            st.write("""
            🏏 **Rohit Sharma Cricket Data**
    
            ↓
    
            📥 **Data Collection**
    
            ↓
    
            🧹 **Data Cleaning & Preprocessing**
    
            ↓
    
            🔎 **Exploratory Data Analysis**
    
            ↓
    
            ⚙️ **Feature Engineering**
    
            ↓
    
            📊 **WOE / IV Analysis**
    
            ↓
    
            🔗 **VIF Analysis**
    
            ↓
    
            🤖 **Machine Learning**
    
            ↓
    
            🌳 **Model Comparison**
    
            ↓
    
            🏆 **Random Forest Final Model**
    
            ↓
    
            📈 **Model Evaluation**
    
            ↓
    
            💾 **Model Serialization**
    
            ↓
    
            🖥️ **Streamlit Application**
    
            ↓
    
            📊 **Prediction + Dashboard + Fan Page**
    
            ↓
    
            🗄️ **NeonDB + GenAI + Voice System**
    
            ↓
    
            🚀 **Final AI-Powered Rohit Sharma Cricket Platform**
            """)

            st.success(
                "🏏 From raw cricket data to a complete AI-powered full-stack application."
            )
        with tab2:
            st.subheader("🤖 Model Building Journey")

            st.caption(
                "My model-building process was iterative. Instead of training one model and "
                "stopping at the first result, I repeatedly evaluated the models, investigated "
                "feature importance, identified possible data leakage, refined the feature set, "
                "and validated the models on unseen data."
            )

            st.write("""
            🔹 **Step 1 — Initial Model Building**

            I started with 19 engineered features and trained multiple classification models,
            including Decision Tree, Random Forest and XGBoost.

            The models were evaluated using Accuracy, Precision, Recall, F1-Score,
            ROC-AUC and Gini.

            🔹 **Step 2 — Feature Importance Analysis**

            After the initial training, I analyzed feature importance to understand which
            variables were influencing the model predictions.

            Some features such as `sixes`, `boundaries_venue` and recent performance
            features showed high importance. This made me investigate whether these
            features were providing information that would not actually be available
            before predicting a new match.

            🔹 **Step 3 — Data Leakage Investigation**

            This was one of the most important stages of my model-building journey.

            Since the objective was to predict whether Rohit Sharma would score 30+ runs
            before the match, I realized that features containing same-match or
            post-match information could introduce data leakage.

            Therefore, I investigated and removed leakage-prone features instead of
            simply accepting higher model performance.

            🔹 **Step 4 — Feature Refinement**

            After removing problematic features, I retrained the models and compared
            their performance again.

            I also investigated low-importance features and removed features that were
            not contributing meaningfully to the prediction.

            Features related to recent strike rate, recent runs and other potentially
            non-predictive information were progressively reviewed.

            🔹 **Step 5 — VIF-Based Feature Selection**

            I used Variance Inflation Factor (VIF) to identify Multi-collinearity between
            the predictor variables.

            For this project, features having **VIF > 10 were removed**.

            This process was repeated to obtain a cleaner and less redundant feature set.

            🔹 **Step 6 — Historical Feature Engineering**

            During the refinement process, I focused more on historical features because
            the prediction should be based on information available before the match.

            I introduced useful contextual features such as:

            • Average runs by month
            • Maximum runs by month
            • Average strike rate by month
            • Maximum strike rate by month
            • Historical venue performance
            • Historical opponent performance
            • Historical format performance

            This shifted the model from using potentially future information toward
            using historical cricket performance.

            🔹 **Step 7 — Repeated Model Evaluation**

            After every major feature change, I retrained and compared the models using:

            • Accuracy
            • Precision
            • Recall
            • F1-Score
            • ROC-AUC
            • Gini

            This helped me understand how each feature-selection decision affected
            the model rather than making decisions based on a single experiment.

            
            🔹 **Step 8 — Unseen Data Validation & Model Selection**

            After completing the feature selection and retraining process, I compared
            the final models, especially **XGBoost and Random Forest**.
            
            The evaluation results showed that XGBoost had strong classification
            performance, with approximately **75% recall** and **79% ROC-AUC** in one
            of the final evaluation stages.
            
            However, I did not select the model only by looking at the evaluation metrics.
            
            I tested both models with **unseen data** and carefully observed their
            predicted classes.
            
            During this validation, I noticed that:
            
            • **XGBoost showed a tendency to predict the positive class (Target = 1)
              for the unseen observations.**
            
            • This meant that although XGBoost showed good evaluation metrics, its
              prediction behavior on the new unseen data was not giving the desired
              balance between **Target = 1 and Target = 0** predictions.
            
            • **Random Forest performed more appropriately on the unseen data**, producing
              predictions for both classes (Target = 1 and Target = 0) rather than
              predominantly predicting only one class.
            
            I therefore considered the actual prediction behavior of the models on
            unseen data along with their evaluation metrics.
            
            🔹 **Why Random Forest was Finalized**
            
            The final decision was to use **Random Forest** for the prediction component
            because it showed more appropriate behavior when tested on unseen data.
            
            This was an important learning point in my project:
            
            **A model should not be selected only because it has a higher evaluation
            metric. Its behavior on genuinely unseen data and its ability to produce
            meaningful predictions for both classes also need to be investigated.**


            🔹 **Step 9 — Final Model**

            After the complete experimentation and validation process, I finalized
            **Random Forest** for the prediction component of the application.

            The final model was selected after considering both model evaluation metrics
            and its observed behavior on unseen data.

            🔹 **Key Learning**

            The biggest lesson from this stage was that a higher model score does not
            automatically mean a better real-world model.

            I learned to investigate feature importance, detect data leakage, use
            historical features, control Multi-collinearity, compare multiple models,
            and validate predictions on unseen data before finalizing a model.
            """)

            st.caption("""

💡 Data Science is not just about training a model — it is about
                understanding the data, questioning the results, finding problems, 
                experimenting with features, and validating the final solution.

💡 My final model-selection decision was based on both quantitative evaluation and practical validation on unseen data.

            """)

    def about_features(self):
        # ============================================================
        # 🖥️ APPLICATION FEATURES
        # ============================================================

        st.subheader("🖥️ Application Features")

        st.caption(
            "The Rohit Sharma FanClub is designed as an interactive full-stack "
            "cricket platform where users can explore statistics, generate ML "
            "predictions, interact with AI, and enjoy fan-oriented features."
        )

        # ============================================================
        # 🏠 1. HOME
        # ============================================================

        st.subheader("🏠 1. Home")

        st.write(
            "The Home page acts as the main entry point of the Rohit Sharma FanClub. "
            "It introduces the platform and provides users with a quick overview of "
            "Rohit Sharma, the project, and the major features available in the application."
        )

        st.caption(
            "The page is designed to give users a simple starting point before "
            "they explore predictions, statistics, the fan page, or the AI assistant."
        )

        st.write("""
        **Main functionality:**

        - 🏏 Rohit Sharma introduction and overview
        - 📊 Quick cricket statistics
        - 👥 FanClub community information
        - 🧭 Easy navigation to different application sections
        - 🎨 Interactive and fan-friendly interface
        """)

        # ============================================================
        # 🏏 2. FAN PAGE
        # ============================================================

        st.subheader("🏏 2. Fan Page")

        st.write(
            "The Fan Page is the entertainment and community-oriented section "
            "of the application. It is designed specifically for Rohit Sharma fans "
            "and provides a more personal and interactive experience."
        )

        st.caption(
            "This section combines cricket information with fan-oriented content "
            "to make the application more than just a machine learning project."
        )

        st.write("""
        **Main functionality:**

        - ❤️ Rohit Sharma fan-oriented content
        - 🖼️ Fan memories and uploaded media
        - 🏏 Cricket-related information
        - 👥 Community interaction features
        - 📸 Rohit Sharma memories section
        """)

        # ============================================================
        # 🤖 3. PREDICTION
        # ============================================================

        st.subheader("🤖 3. Prediction")

        st.write(
            "The Prediction page is the core Machine Learning component of the "
            "application. It uses historical Rohit Sharma batting data and the "
            "trained RandomForest classification model to predict whether he is likely "
            "to score 30 or more runs."
        )

        st.caption(
            "The model generates a probability score and applies the optimized "
            "classification threshold to produce the final prediction."
        )

        st.write("""
        **Prediction workflow:**

        📥 User Input  
        ↓  
        ⚙️ Data Preprocessing  
        ↓  
        🧠 Feature Transformation  
        ↓  
        🚀 Random Forest Model  
        ↓  
        📊 Probability Prediction  
        ↓  
        🎚️ Optimized Threshold  
        ↓  
        🎯 Final 30+ Runs Prediction

        **Output includes:**

        - 🎯 Probability of scoring 30+ runs
        - ✅ Predicted outcome
        - 📈 Expected performance information
        - 🔍 Model-based insights
        """)

        # ============================================================
        # 📊 4. DASHBOARD
        # ============================================================

        st.subheader("📊 4. Dashboard")

        st.write(
            "The Dashboard provides an interactive visual analysis of Rohit Sharma's "
            "historical batting performance. Users can filter the data and explore "
            "statistics across formats, opponents, time periods, and other cricket "
            "dimensions."
        )

        st.caption(
            "The dashboard converts the underlying cricket dataset into interactive "
            "charts, metrics, comparisons, and performance insights."
        )

        st.write("""
        **Dashboard features:**

        - 🏏 Performance by cricket format
        - 🆚 Performance against opponents
        - 📈 Runs and strike-rate analysis
        - 4️⃣ Fours and 6️⃣ Sixes analysis
        - 🎯 Batting performance indicators
        - 📅 Year and month-based analysis
        - 🏆 Top-performing opponents
        - 📊 Interactive charts and graphs
        - 🔎 Format and opponent filters
        - 📋 Match-level data exploration
        """)

        # ============================================================
        # 🧠 5. AI ASSISTANT
        # ============================================================

        st.subheader("🧠 5. AI Assistant")

        st.write(
            "The AI Assistant adds a Generative AI layer to the cricket application. "
            "It allows users to interact with an AI-powered cricket assistant and "
            "ask questions related to Rohit Sharma, cricket, statistics, performances, "
            "and the project."
        )

        st.caption(
            "The AI Assistant is integrated with Generative AI to provide "
            "conversational responses instead of relying only on predefined information."
        )

        st.write("""
        **AI Assistant capabilities:**

        - 💬 Natural-language conversation
        - 🏏 Rohit Sharma-related questions
        - 📊 Cricket statistics and performance discussions
        - 🧠 AI-generated cricket responses
        - ❓ Interactive question answering
        - 🎙️ Voice-based interaction support
        """)

        # ============================================================
        # 👤 6. USER AUTHENTICATION
        # ============================================================

        st.subheader("👤 6. User Registration & Login")

        st.write(
            "The application includes a user authentication system that allows "
            "fans to create accounts and securely access the platform."
        )

        st.caption(
            "Authentication connects the application with the NeonDB database "
            "and provides a personalized user experience."
        )

        st.write("""
        **Authentication features:**

        - 📝 User registration
        - 🔐 User login
        - 👤 User-ID based account access
        - 📧 Email verification
        - 🔢 OTP-based verification
        - 🔑 Password-based authentication
        - 💾 User information stored in NeonDB
        """)

        # ============================================================
        # 📧 7. EMAIL OTP
        # ============================================================

        st.subheader("📧 7. OTP Verification")

        st.write(
            "Email & SMS OTP verification adds an additional security layer to the "
            "registration and account-related workflow. A temporary verification "
            "code is generated and sent to the user's registered contact details."
        )

        st.caption(
            "The OTP mechanism helps verify that the provided email address and contact number "
            "belongs to the user."
        )

        # ============================================================
        # 💾 8. POSTGRESQL
        # ============================================================

        st.subheader("💾 8. NeonDB Database")

        st.write(
            "NeonDB is used as the application's persistent database layer. "
            "It allows the system to store and retrieve user information and "
            "application-related records dynamically."
        )

        st.caption(
            "Database integration transforms the application from a static "
            "machine learning demo into a data-driven full-stack platform."
        )

        st.write("""
        **Database functionality:**

        - 👤 User account storage
        - 📧 Email and contact information
        - 🔐 Authentication-related data
        - 📊 Application records
        - 🔎 Data retrieval and filtering
        - ☁️ NeonDB cloud database integration
        """)


        # ============================================================
        # 🏆 FINAL PROJECT SUMMARY
        # ============================================================

        st.subheader("🏆 Final Project Summary")

        st.write(
            "The Rohit Sharma FanClub combines Data Science, Machine Learning, "
            "Generative AI, Data Visualization, PostgreSQL, Authentication, "
            "Voice Interaction, and Streamlit development into a single application."
        )

        st.caption(
            "The project demonstrates how a raw cricket dataset can be transformed "
            "into a complete, interactive and AI-powered full-stack application."
        )

        st.success(
            "🏏 From cricket data → 📊 analytics → 🤖 ML prediction → 🧠 GenAI → "
            "💾 database → 🖥️ full-stack platform."
        )
    def techstack(self):
        # ============================================================
        # 🛠️ TECHNOLOGY STACK
        # ============================================================

        st.subheader("🛠️ Full Technology Stack")

        st.caption(
            "The Rohit Sharma FanClub combines data collection, data science, "
            "machine learning, visualization, web development, database management, "
            "Generative AI, authentication, and deployment "
            "technologies into a single application."
        )

        # ------------------------------------------------------------
        # 🐍 Programming
        # ------------------------------------------------------------

        st.write("### 🐍 Programming")

        st.caption("Programming language used to build the complete application.")

        st.write("**Python**")

        # ------------------------------------------------------------
        # 📥 Data Collection
        # ------------------------------------------------------------

        st.write("### 📥 Data Collection")

        st.caption(
            "Cricket information was collected from web-sourced cricket data "
            "and CricAPIs."
        )

        st.write("""
        - 🏏 Cricbuzz-sourced cricket data
        - 🔌 CricAPI
        - 📊 Historical match datasets
        """)

        # ------------------------------------------------------------
        # 📊 Data Processing & Analysis
        # ------------------------------------------------------------

        st.write("### 📊 Data Processing & Analysis")

        st.caption(
            "These libraries were used for data cleaning, transformation, "
            "statistical analysis, exploratory data analysis, and feature engineering."
        )

        st.write("""
        - 🐼 **Pandas** – Data manipulation and preprocessing
        - 🔢 **NumPy** – Numerical operations
        - 📈 **Statistical Analysis** – Understanding cricket performance patterns
        - 🔎 **Exploratory Data Analysis (EDA)** – Discovering trends and relationships
        - ⚙️ **Feature Engineering** – Creating predictive features
        """)

        # ------------------------------------------------------------
        # 🤖 Machine Learning
        # ------------------------------------------------------------

        st.write("### 🤖 Machine Learning")

        st.caption(
            "Multiple machine learning algorithms were evaluated before selecting "
            "the final model for the 30+ runs classification task."
        )

        st.write("""
        - 🌳 **Decision Tree**
        - 🌲 **Random Forest**
        - 🚀 **XGBoost**
        
        """)

        # ------------------------------------------------------------
        # 🔬 Feature Analysis
        # ------------------------------------------------------------

        st.write("### 🔬 Feature Analysis")

        st.caption(
            "Feature-analysis techniques were used to understand predictive strength "
            "and identify multi-collinearity among variables."
        )

        st.write("""
        - 📊 **WOE – Weight of Evidence**
        - 📈 **IV – Information Value**
        - 🔗 **VIF – Variance Inflation Factor**
        """)

        # ------------------------------------------------------------
        # 📊 Visualization
        # ------------------------------------------------------------

        st.write("### 📊 Data Visualization")

        st.caption(
            "Visualization tools were used to present cricket performance, "
            "model insights, trends, comparisons, and interactive dashboards."
        )

        st.write("""
        - 📈 **Matplotlib**
        - 📊 **Seaborn**
        - 🖥️ **Streamlit Charts & Dashboard Components**
        """)

        # ------------------------------------------------------------
        # 🌐 Web Application
        # ------------------------------------------------------------

        st.write("### 🌐 Web Application")

        st.caption(
            "Streamlit was used to combine the machine learning models, "
            "analytics, database, AI features, and user interface into one application."
        )

        st.write("""
        - 🖥️ **Streamlit**
        - 🏠 Home
        - 🏏 Fan Page
        - 🤖 Prediction
        - 📊 Dashboard
        - 🧠 AI Assistant
        - ℹ️ About Project
        """)

        # ------------------------------------------------------------
        # 💾 Database
        # ------------------------------------------------------------

        st.write("### 💾 Database Management")

        st.caption(
            "NeonDB provides persistent storage for application and user-related data."
        )

        st.write("""
        
        - ☁️ **Neon PostgreSQL**
        """)

        # ------------------------------------------------------------
        # 🧠 Generative AI
        # ------------------------------------------------------------

        st.write("### 🧠 Generative AI")

        st.caption(
            "Generative AI powers the conversational cricket assistant, "
            "allowing users to ask questions and receive AI-generated responses."
        )

        st.write("""
        - 🤖 **Google GenAI API**
        - 💬 AI-powered Cricket Assistant
        """)


        # ------------------------------------------------------------
        # 🔐 Authentication & Email
        # ------------------------------------------------------------

        st.write("### 🔐 Authentication & Email")

        st.caption(
            "Authentication and OTP verification provide a secure user registration "
            "and login workflow."
        )

        st.write("""
        - 👤 User Registration & Login
        - 🔢 Email/SMS OTP Verification
        - 📧 **SMTP**
        - 📬 **SMS Gateway API**
        """)

        # ------------------------------------------------------------
        # 💾 Model Serialization
        # ------------------------------------------------------------

        st.write("### 💾 Model Serialization")

        st.caption(
            "The trained model and required preprocessing components are serialized "
            "so the Streamlit application can load them directly for prediction."
        )

        st.write("""
        - 📦 **Pickle / Serialized Model**
        - 🧠 Trained Random Forest Model
        - ⚙️ Preprocessing Components
        - 🎚️ Optimized Prediction Threshold
        """)

        # ------------------------------------------------------------
        # 🚀 Deployment
        # ------------------------------------------------------------

        st.write("### 🚀 Deployment")

        st.caption(
            "The completed Streamlit application was deployed as a cloud-based "
            "interactive cricket platform."
        )

        st.write("""
        - ☁️ **Streamlit Cloud**
        - 📦 **GitHub Repository**
        """)

        # ------------------------------------------------------------
        # 🧰 Development Tools
        # ------------------------------------------------------------

        st.write("### 🧰 Development Tools")

        st.caption(
            "Development and version-control tools used during project implementation."
        )

        st.write("""
        - 🔧 **Git**
        - 🐙 **GitHub**
        - 💻 **Syder**
        - 🐍 **PyCharm**
        """)

        # ============================================================
        # 🏆 FINAL STACK SUMMARY
        # ============================================================

        st.subheader("🏆 Technology Stack Summary")

        st.caption(
            "The complete technology stack connects the data science pipeline "
            "with the application's AI, database, authentication, voice, and "
            "web-development components."
        )

        st.write("""
        🐍 **Python**
        → 📊 **Pandas + NumPy**
        → 🔎 **EDA + Feature Engineering**
        → 🔬 **WOE + IV + VIF**
        → 🤖 **Machine Learning + XGBoost**
        → 📈 **Matplotlib + Seaborn**
        → 🖥️ **Streamlit**
        → 💾 **PostgreSQL + Neon**
        → 🧠 **Google GenAI**
        → 🔐 **Authentication + Email/SMS OTP**
        → 📦 **Pickle Model**
        → 🐙 **GitHub**
        → ☁️ **Streamlit Cloud**
        """)

        st.success(
            "🚀 A complete Data Science + Machine Learning + GenAI + "
            "Full-Stack Cricket Application"
        )
    def main(self):
        st.header("📊 About Project")
        tab1,tab2,tab3,tab4,tab5 = st.tabs(["🔍 Overview","🏗️ Project Architecture",
                                            "📊 DataScience Journey","🖥️ About Features","🛠️ Technology Stack"])
        with tab1:
            self.projectinfo()
        with tab2:
            self.architecture()
        with tab3:
            self.datascience_journey()
        with tab4:
            self.about_features()
        with tab5:
            self.techstack()
