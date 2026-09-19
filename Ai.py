import streamlit as st
from google import genai
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()


@st.cache_resource
class AiAssistant:
    def main(self):
        # Create the Gemini API client
        self.client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"])

        self.groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

        # System prompt that defines the AI assistant's behavior
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
        
        Answer this without any hesitation

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
        
        if question is hye,hello,hi or like this then you can welcome them by greeting!

        For questions about the user's project dataset, say that
        project-specific data will be connected later.
        
        Make sure all detail you were sharing about rohit sharma is genuine 
        not any rumors or fake information should be scrap always find real information about indian cricketer rohit sharma

        
        Always follow these restrictions
        
        """
        # session_state is used to preserve chat messages between
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # APPLICATION TITLE AND DESCRIPTION
        st.title("🤖 AI Assistant")
        st.write("Hye I'm your AI Assistant ask anything about Rohit Sharma.")

        # Loop through all previously stored messages
        # and display them in the Streamlit chat interface.
        for message in st.session_state.messages:

            # message["role"] will be either:
            # "user" or "assistant"
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Display a chat input box at the bottom of the application.
        self.chat_input = st.chat_input("Ask something about Rohit Sharma...")

        if self.chat_input:

            # Show the user's message immediately in the chat UI.
            with st.chat_message("user"):
                st.markdown(self.chat_input)

            # Store the user's message in session_state so it
            st.session_state.messages.append({"role": "user", "content": self.chat_input})

            # Start the conversation with the system prompt.
            conversation = self.system_prompt + "\n\n"

            # This helps:
            # - Reduce API token usage
            # - Improve response speed
            # - Prevent the conversation from becoming too large
            recent_messages = st.session_state.messages[-10:]

            # Add previous conversation messages to the prompt.
            for message in recent_messages:
                conversation += (f"{message['role'].upper()}: "
                                 f"{message['content']}\n")

            # # GENERATE AI RESPONSE
            try:
            #     with st.chat_message("assistant"):
            #         with st.spinner(
            #             "Thinking... 🏏"):
            #             try:
            #                 groq_messages = [
            #                     {
            #                         "role": "system",
            #                         "content": self.system_prompt
            #                     }
            #                 ]
            #                 # Add recent conversation
            #                 for message in recent_messages:
            #                     groq_messages.append(
            #                         {
            #                             "role": message["role"],
            #                             "content": message["content"]
            #                         }
            #                     )
            #                 # Groq request
            #                 groq_response = self.groq_client.chat.completions.create(
            #                     model="openai/gpt-oss-20b",
            #                     messages=groq_messages,
            #                     temperature=0.3,
            #                     max_tokens=800)
            #                 answer = (groq_response.choices[0].message.content)
            #                 st.markdown(answer)
            #                 # Save Groq response
            #                 st.session_state.messages.append(
            #                     {
            #                         "role": "assistant",
            #                         "content": answer
            #                     }
            #                 )
            #             except Exception as groq_error:
                with st.chat_message("assistant"):
                    with st.spinner(" Thinking2.O..."):
                    # Send the conversation to the Gemini model.
                        response = self.client.models.generate_content(model="gemini-3.6-flash",
                                                                   contents=conversation)

                # Display Gemini's response in the chat.
                st.markdown(response.text)

            # Store the assistant's response in session_state
                st.session_state.messages.append({"role": 'assistant', "content": response.text})

                # Create the assistant chat message container.

            # HANDLE ERRORS
            except Exception as gemini_error:
              st.error("Sorry, AI services are currently unavailable.")

                            # st.error(
                            #     f"Gemini Error: {gemini_error}"
                            # )
                            #
                            # st.error(
                            #     f"Groq Error: {groq_error}"
                            # )
