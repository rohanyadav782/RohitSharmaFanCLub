import streamlit as st
import pickle
import numpy as np
import pandas as pd
from dataset import  Dataset


@st.cache_resource
class Prediciton:
    def load_files(self):
        with open("pickle5.pkl", "rb") as file:
            dataset = Dataset()
            self.data = dataset.model_ready_data
            all_files = pickle.load(file)
            self.loaded_model = all_files["xgb_model"]
            self.month_ = all_files["month_encoder"]
            self.opponent_ = all_files["Opponent_encoder"]
            self.format_ = all_files["Format_encoder"]
            self.scalar = all_files["scalar"]
            self.feature_coefficient = all_files["Feature_importance"]
            self.model_evaluation = all_files["model_evaluation"]

            self.format_list = list(self.data["Format"].unique())

    def predict_runs(self):
        st.header("🏏 Cricket Runs Prediction")
        st.caption("Predict how many runs will rohit score on inserting his cricket detail!")
        col1, col2= st.columns(2)
        with col1:
            format_list = self.data["Format"].tolist()
            self.format = st.selectbox("Select Format",self.data["Format"].dropna().unique().tolist())
            self.format_selection=format_list.index(self.format)
            print(self.format_selection)
            self.opponent_list = self.data["Opponent"].tolist()
            self.opponent = st.selectbox("Select Opponent", self.data[self.data['Format'] == self.format]['Opponent'].dropna().unique().tolist())
            self.opponent = self.opponent_list.index(self.opponent)
            print(self.opponent)
            self.max_run_opponent = st.number_input("Max Run vs Opponent",step = 1)
            self.avg_run_opponent = st.number_input("Average Run vs Opponent",step = 1)
            self.last_5days_strikerate = st.number_input("Last 5Days StrikeRate",step = 1)
            self.strikerate = st.number_input("Enter Last Match StrikeRate")
            self.avg_run_month = st.number_input("Avg Run on Month", step=1)

            with col2:
                self.months_list = self.data["Month"].tolist()
                self.month = st.selectbox("Select Month", self.data['Month'].dropna().unique().tolist())
                self.month = self.months_list.index(self.month)
                print(self.month)
                self.venue_list = self.data["Venue"].tolist()
                self.venue_i = st.selectbox("Select Venue", self.data[self.data['Format'] == self.format]['Venue'].dropna().unique().tolist())
                self.venue = self.venue_list.index(self.venue_i)
                print(self.venue)
                self.max_run_month = st.number_input("Max Run on Month",step = 1)
                self.avg_strike_rate_month = st.number_input("Average StrikerRate on Month",step = 1)
                self.max_strike_rate_month = st.number_input("Max StrikerRate On Month",step = 1)
                self.avg_strike_rate_venue = st.number_input("Avg StrikerRate at Venue",step = 1)
                self.max_run_venue = st.number_input("Max Runs at Venue",step = 1)

        if st.button("Predict Runs"):
            with st.spinner("Predicting runs..."):

                new_data = np.array([[self.opponent,self.format_selection,self.venue,self.avg_strike_rate_venue,self.max_run_venue,self.avg_run_opponent,self.max_run_opponent,
                                      self.avg_run_month,self.max_run_month,self.avg_strike_rate_month,self.max_strike_rate_month,self.last_5days_strikerate,self.strikerate,self.month]])
                new_df = pd.DataFrame(new_data, columns=[
                     "Opponent", "Format","Venue","Avg_strike_rate_venue","Max_run_venue","Avg_runs_opponent","Max_runs_opponent",
                    "avg_runs_month","max_runs_month","avg_strikerate_month", "max_strikerate_month","last_5days_strikerate","Strike_rate","Month"])
                new_data_scaled = self.scalar.transform(new_df)
                # prediction = self.loaded_model.predict(new_data_scaled)
                probability = self.loaded_model.predict_proba(new_data_scaled)[:, 1]
                self.percentage = probability * 100
                if probability >= 0.50:
                    st.success(
                        f"""
                    
                    🏏 Cricket Prediction 🏏
                    
                     Probability : {round(self.percentage[0],2)}%
        
                     30+ Runs : ✅ Yes
                    """
                    )

                else:
                    st.warning(
                          f"""
                    🏏 Cricket Prediction 🏏
        
                    Probability : {round(self.percentage[0],2)}%
        
                    30+ Runs: ❌ No
                    """           )