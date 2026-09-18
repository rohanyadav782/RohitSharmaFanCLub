import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from dataset import  Dataset

@st.cache_resource
class Dashboard:
    def load_data(self):
        data = Dataset()
        self.df = data.cleaned_data

    def main(self):
        self.load_data()
        st.subheader("📈 Dashboard")
        if self.df.empty:
            st.warning("⚠️ No data available for the selected filters.")
        else:
            tab1, tab2,tab3 = st.tabs(['🏏Career Overview', "📈 Batting Performance","️⚔️ Opponent & Venue"])
            with tab1:
                self.career_overview()
            with tab2:
                self.batting_performance()
            with tab3:
                self.opponent_venue()

    def career_overview(self):
        self.format_slicer = st.sidebar.multiselect("Format",sorted(self.df["Format"].dropna().unique()),default=sorted(self.df["Format"].dropna().unique()))
        self.year_slicer = st.sidebar.multiselect("Year",sorted(self.df["Year"].dropna().unique()),default=sorted(self.df["Year"].dropna().unique()))

        data = self.df[
            (self.df["Format"].isin(self.format_slicer)) &
            (self.df["Year"].isin(self.year_slicer))
            ]
        innings = len(data)
        runs = int(data["runs"].sum())
        average = round(data["runs"].mean(),2)
        strike_rate = round(data["Strike_rate"].mean(),2)
        fifties = ((data["runs"] >= 50) & (data["runs"] < 100)).sum()
        centuries = (data["runs"] >= 100).sum()

        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.metric("Total Innings",innings )
        col2.metric("Total Runs",runs)
        col3.metric("Average Runs",average)
        col4.metric("Strike Rate",strike_rate)
        col5.metric("50s",fifties)
        col6.metric("100s",centuries)
        st.divider()
        col1, col2 = st.columns(2)
        # ---------------- RUNS BY YEAR ----------------
        with col1:
            yearly = (data.groupby("Year")["runs"].sum().reset_index())
            fig = px.bar(yearly,x="Year",y="runs",title="📈 Runs by Year",text_auto=True)
            st.plotly_chart(fig,width='stretch')
        # ---------------- AVERAGE RUNS FORMAT ----------------
        with col2:
            format_avg = (data.groupby("Format")["runs"].mean().reset_index())
            fig = px.bar(format_avg,x="Format",y="runs",title="📊 Average Runs by Format",text_auto=True)
            st.plotly_chart(fig,width='stretch')
        # ---------------- BOUNDARIES ----------------
        col3, col4 = st.columns(2)
        with col3:
            boundaries = (data.groupby("Format")[["Fours", "Sixes"]].sum().reset_index())
            fig = px.bar(boundaries,x="Format",y=["Fours", "Sixes"],barmode="group",title="🏏📊 Boundaries by Format")
            st.plotly_chart(fig,width='stretch')
        # ---------------- STRIKE RATE ----------------
        with col4:
            fig = px.scatter(data,x="Balls",y="runs",color="Format",size="Strike_rate",title="🏏⚡ Strike Rate Analysis")
            st.plotly_chart(fig,width='stretch')
        # ---------------- VENUE TABLE ----------------
        st.subheader("🏟️ Venue Performance")
        venue_table = (
            data.groupby("Venue").agg(Innings=("runs", "count"),Runs=("runs", "sum"),Average=("runs", "mean"),
                                         StrikeRate=("Strike_rate", "mean")).round(2))
        st.dataframe(venue_table,width='stretch')

    def batting_performance(self):
        # self.year_slicer_2 = st.sidebar.multiselect("Year",sorted(self.df["Year"].dropna().unique()),default=sorted(self.df["Year"].dropna().unique()))
        # self.format_slicer = st.sidebar.multiselect("Format",sorted(self.df["Format"].dropna().unique()),default=sorted(self.df["Format"].dropna().unique()))
        self.month_slicer = st.sidebar.multiselect("Month",sorted(self.df["Month"].dropna().unique()),default=sorted(self.df["Month"].dropna().unique()))
        data = self.df[(self.df["Year"].isin(self.year_slicer)) &
            (self.df["Month"].isin(self.month_slicer)) &(self.df["Format"].isin(self.format_slicer))]
        col1, col2, col3, col4 = st.columns(4)
        total_runs = int(
            data["runs"].sum())

        avg_sr = round(data["Strike_rate"].mean(),2)
        month_runs = (data.groupby("Month")["runs"].sum())
        year_runs = (data.groupby("Year")["runs"].sum())
        best_month = (month_runs.idxmax()
                      if not month_runs.empty
                      else "-")

        peak_year = (year_runs.idxmax()
                     if not year_runs.empty
                    else "-")

        col1.metric("Total Runs",total_runs)
        col2.metric("Average Strike Rate",avg_sr)
        col3.metric("Peak Month",best_month)
        col4.metric("Peak Year",peak_year)

        st.divider()
        col1, col2 = st.columns(2)
        # ---------------- MONTH RUNS ----------------
        with col1:
            month_run = (data
                .groupby("Month")["runs"]
                .sum()
                .reset_index())
            fig = px.line(month_run,x="Month",y="runs",markers=True,title="📈 Runs by Month")
            st.plotly_chart(fig,
                width ='stretch')

        # ---------------- MONTH STRIKE RATE ----------------

        with col2:
            month_sr = (data
                .groupby("Month")["Strike_rate"]
                .mean()
                .reset_index())
            fig = px.line(month_sr,x="Month",y="Strike_rate",markers=True,title="⚡ Strike Rate by Month")
            st.plotly_chart(fig,width ='stretch')

        col3, col4 = st.columns(2)

        # ---------------- 4 VS 6 ----------------

        with col3:
            fours = data["Fours"].sum()
            sixes = data["Sixes"].sum()

            fig = px.pie(names=["4s", "6s"],values=[fours, sixes],title="4s vs 6s")

            st.plotly_chart(
                fig,width ='stretch')

        # ---------------- 50S & 100S ----------------

        with col4:
            temp = data.copy()
            temp["Fifties"] = (
                    (temp["runs"] >= 50) &
                    (temp["runs"] < 100))

            temp["Centuries"] = (
                    temp["runs"] >= 100)

            format_scores = (temp
                .groupby("Format")
                [["Fifties", "Centuries"]]
                .sum()
                .reset_index())

            fig = px.bar(
                format_scores,
                x="Format",
                y=["Fifties", "Centuries"],
                barmode="group",
                title="Fifties & Centuries")

            st.plotly_chart(fig,width='stretch')

        # ---------------- OPPONENT ----------------

        st.subheader("🆚📊 Opponent-wise Performance")

        opponent_runs = (data
            .groupby("Opponent")["runs"]
            .sum()
            .sort_values()
            .reset_index())

        fig = px.bar(opponent_runs,
            x="runs",
            y="Opponent",
            orientation="h",
            title="Runs Against Opponents")

        st.plotly_chart(fig,width='stretch')

    def opponent_venue(self):
        col1, col2, col3, col4 = st.columns(4)
        self.venue_slicer = st.sidebar.multiselect("Venue", sorted(self.df["Venue"].dropna().unique()),
                                                    default=sorted(self.df["Venue"].dropna().unique()))
        self.opponent_slicer = st.sidebar.multiselect("Opponent", sorted(self.df["Opponent"].dropna().unique()),
                                                   default=sorted(self.df["Opponent"].dropna().unique()))
        data = self.df[(self.df["Venue"].isin(self.venue_slicer)) &
                       (self.df["Opponent"].isin(self.opponent_slicer))]

        venue_count = data["Venue"].nunique()
        opponent_count = data["Opponent"].nunique()

        venue_runs = (data
            .groupby("Venue")["runs"]
            .sum())

        opponent_runs = (data
            .groupby("Opponent")["runs"]
            .sum())

        best_venue = (venue_runs.idxmax()
            if not venue_runs.empty
            else "-")

        best_opponent = (opponent_runs.idxmax()
            if not opponent_runs.empty
            else "-")

        col1.metric("Venues",venue_count)
        col2.metric("Opponents",opponent_count)
        col3.metric("Best Venue",best_venue)
        col4.metric("Best Opponent",best_opponent)

        st.divider()

        col1, col2 = st.columns(2)

        # ---------------- VENUE PERFORMANCE ----------------

        with col1:
            venue_data = (data
                .groupby("Venue")["runs"]
                .mean()
                .reset_index()).sort_values("runs",ascending=False).head(10)

            fig = px.bar(venue_data,
                x="Venue",
                y="runs",
                title="🏆 Top 10 Venue by Average Runs")

            st.plotly_chart(fig,width='stretch')

        # ---------------- OPPONENT PERFORMANCE ----------------

        with col2:
            opponent_data = (data
                .groupby("Opponent")["runs"]
                .mean()
                .reset_index()).sort_values("runs",ascending=False).head(10)

            fig = px.bar(opponent_data,
                x="Opponent",
                y="runs",
                title="⭐ Top 10 Opponent by Average Runs")

            st.plotly_chart(fig,width='stretch')

        st.subheader("📋 Bottom 5 Opponent by Average Runs")
        bottom_5 = (data
                         .groupby("Opponent")["runs"]
                         .mean()
                         .reset_index()).sort_values("runs", ascending=False).tail(5)
        st.dataframe(bottom_5,hide_index=True)

        centuries_data = (data[data['runs']>=100]
                         .groupby("Opponent")["runs"]
                         .count()
                         .reset_index(name='centuries')).sort_values("centuries", ascending=False).head(5)

        st.subheader("📋 Most Centuries Against Opponent")
        st.dataframe(centuries_data, hide_index=True)



