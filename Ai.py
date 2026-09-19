import streamlit as st
from google import genai
import os


# ============================================================
# GEMINI API KEY MANAGER
# ============================================================

class GeminiManager:

    def __init__(self):

        # Get all API keys from Streamlit secrets
        self.api_keys = [
            st.secrets.get("GEMINI1"),
            st.secrets.get("GEMINI2"),
            st.secrets.get("GEMINI3"),
            st.secrets.get("GEMINI4"),
            st.secrets.get("GEMINI5")
        ]

        # Remove empty keys
        self.api_keys = [
            key for key in self.api_keys
            if key
        ]

        if not self.api_keys:
            raise ValueError("No Gemini API keys found!")

        # Start with first key
        self.current_key = 0

    # --------------------------------------------------------
    # CREATE GEMINI CLIENT
    # --------------------------------------------------------

    def get_client(self):

        return genai.Client(
            api_key=self.api_keys[self.current_key]
        )

    # --------------------------------------------------------
    # MOVE TO NEXT KEY
    # --------------------------------------------------------

    def next_key(self):

        self.current_key = (
            self.current_key + 1
        ) % len(self.api_keys)

    # --------------------------------------------------------
    # SEND REQUEST
    # --------------------------------------------------------

    def ask(self, conversation):

        total_keys = len(self.api_keys)

        # Try each available API key at most once
        for attempt in range(total_keys):

            key_number = self.current_key + 1

            print(f"Using Gemini API Key {key_number}")

            try:

                # Create client using current key
                client = self.get_client()

                # Send request to Gemini
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=conversation
                )

                # --------------------------------------------
                # SUCCESS
                # --------------------------------------------

                # Move to next key for the NEXT request
                self.next_key()

                return response.text

            except Exception as e:

                error = str(e).lower()

                # --------------------------------------------
                # QUOTA / RATE LIMIT ERROR
                # --------------------------------------------

                if (
                    "429" in error
                    or "quota" in error
                    or "resource exhausted" in error
                    or "rate limit" in error
                ):

                    print(
                        f"Gemini API Key {key_number} "
                        f"quota/rate limit reached."
                    )

                    # Try next API key
                    self.next_key()

                else:

                    # Some other Gemini error
                    print("Gemini Error:", e)

                    return None

        # ----------------------------------------------------
        # ALL KEYS FAILED
        # ----------------------------------------------------

        return (
            "All Gemini API keys have reached their quota."
        )


# ============================================================
# AI ASSISTANT
# ============================================================

@st.cache_resource
class AiAssistant:

    def main(self):

        # ----------------------------------------------------
        # CREATE GEMINI MANAGER
        # ----------------------------------------------------

        self.gemini = GeminiManager()

        # ----------------------------------------------------
        # SYSTEM PROMPT
        # ----------------------------------------------------

        self.system_prompt = """
        You are Rohit Sharma AI Assistant.

        STRICT RULE:

        You can answer questions about:
        - Rohit Sharma
        - His cricket career
        - Batting
        - ODI
        - Test cricket
        - T20 cricket
        - IPL
        - Cricket records
        - Cricket terminology
        - General cricket information
        - Anything about Rohit Sharma

        If the user's question is NOT related to Rohit Sharma or cricket,
        DO NOT answer the question.

        You MUST respond exactly:

        "Sorry, I could not proceed. I can answer only questions related to Rohit Sharma or cricket."

        Answer this without any hesitation.

        Do not explain the unrelated topic.
        Do not provide additional information.

        Do not answer general questions such as:
        - Python
        - SQL
        - Mathematics
        - Politics
        - Movies
        - Technology
        - General knowledge
        - Personal advice
        - Any other non-cricket topic.

        If the question is hi, hello, hey or similar greetings,
        you can welcome the user with a greeting.

        For questions about the user's project dataset,
        say that project-specific data will be connected later.

        Make sure all details you share about Rohit Sharma
        are genuine. Do not provide rumors or fake information.

        Always follow these restrictions.
        """

        # ----------------------------------------------------
        # SESSION STATE
        # ----------------------------------------------------

        if "messages" not in st.session_state:

            st.session_state.messages = []

        # ----------------------------------------------------
        # APPLICATION TITLE
        # ----------------------------------------------------

        st.title("🤖 AI Assistant")

        st.write(
            "Hye I'm your AI Assistant "
            "ask anything about Rohit Sharma."
        )

        # ----------------------------------------------------
        # DISPLAY PREVIOUS MESSAGES
        # ----------------------------------------------------

        for message in st.session_state.messages:

            with st.chat_message(message["role"]):

                st.markdown(message["content"])

        # ----------------------------------------------------
        # CHAT INPUT
        # ----------------------------------------------------

        chat_input = st.chat_input(
            "Ask something about Rohit Sharma..."
        )

        if chat_input:

            # ------------------------------------------------
            # DISPLAY USER MESSAGE
            # ------------------------------------------------

            with st.chat_message("user"):

                st.markdown(chat_input)

            # ------------------------------------------------
            # SAVE USER MESSAGE
            # ------------------------------------------------

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": chat_input
                }
            )

            # ------------------------------------------------
            # CREATE CONVERSATION
            # ------------------------------------------------

            conversation = (
                self.system_prompt
                + "\n\n"
            )

            # Only use last 10 messages
            recent_messages = (
                st.session_state.messages[-10:]
            )

            # Add previous messages
            for message in recent_messages:

                conversation += (
                    f"{message['role'].upper()}: "
                    f"{message['content']}\n"
                )

            # ------------------------------------------------
            # GENERATE GEMINI RESPONSE
            # ------------------------------------------------

            try:

                with st.chat_message("assistant"):

                    with st.spinner(
                        "Thinking 2.O... 🏏"
                    ):

                        answer = self.gemini.ask(
                            conversation
                        )

                    # ----------------------------------------
                    # DISPLAY RESPONSE
                    # ----------------------------------------

                    if answer is not None:

                        st.markdown(answer)

                    else:

                        answer = (
                            "Sorry, AI services are "
                            "currently unavailable."
                        )

                        st.error(answer)

                # --------------------------------------------
                # SAVE ASSISTANT RESPONSE
                # --------------------------------------------

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

            except Exception as e:

                print("Application Error:", e)

                st.error(
                    "Sorry, AI services are "
                    "currently unavailable."
                )


# ============================================================
# RUN APPLICATION
# ============================================================