import streamlit as st
from databaseconnection import  DatabaseConnection

class Profile:

    def main(self):
        st.header("👤 My Profile")
        st.divider()
        with st.spinner("User Detail Loading..."):
            try:
                db = DatabaseConnection()
                db.connect_db()
                user = st.session_state.user_id
                self.cursor = db.conn.cursor()
                self.cursor.execute("SELECT * FROM users_data WHERE user_id = %s;",(user,))
                rows = self.cursor.fetchone()
                if rows:
                    user_detail = rows
                    st.write(f"""
                Name     :- {user_detail[1]}
    
                User-ID  :- {user_detail[0]}
    
                Number   :- {user_detail[2]}
    
                Email    :- {user_detail[3]}
    
                Password :- {user_detail[4]}
                """)

                else:
                    st.warning("User not found")

            except Exception as e:
                st.error("Connection failed, Make sure your network is strong !")
                st.warning(e)
