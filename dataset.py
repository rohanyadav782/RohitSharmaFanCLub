import pandas as pd
import  streamlit as st

class Dataset:
    def __init__(self):
        self.raw_data = pd.read_excel("cricket_dataset.xlsx",sheet_name="raw_data")
        self.cleaned_data = pd.read_excel("cricket_dataset.xlsx",sheet_name="cleaned_data")
        self.model_ready_data = pd.read_excel("cricket_dataset.xlsx",sheet_name="model_ready_data")
        self.model_comparison = pd.read_excel("cricket_dataset.xlsx",sheet_name="model_comparison")
        self.feature_importance = pd.read_excel("cricket_dataset.xlsx",sheet_name="feature_importance")

    def main(self):
        st.subheader("📰 DataSet")
        tab1,tab2,tab3,tab4,tab5 = st.tabs(["📋 Raw Data","✨ Cleaned Data","⚙️ Model Ready Data","⚖️ Model Comparison","📊 Feature Importance"])
        with tab1:
            toprawdata = self.raw_data.head(10)
            st.dataframe(toprawdata,use_container_width=True,hide_index = True)
        with tab2:
            topcleaneddata = self.cleaned_data.head(10)
            st.dataframe(topcleaneddata,hide_index = True)
        with tab3:
            topmodelreadydata = self.model_ready_data.head(10)
            st.dataframe(topmodelreadydata,hide_index = True)
        with tab4:
            st.dataframe(self.model_comparison,hide_index = True)
        with tab5:
            st.dataframe(self.feature_importance,hide_index = True)