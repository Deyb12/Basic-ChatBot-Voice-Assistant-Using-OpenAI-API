import streamlit as st
import openai
import pyttsx3

# Set up OpenAI API key
openai.api_key = st.secrets["api_secret"]
engine = pyttsx3.init()
# Function to generate answer from questions using OpenAI's GPT-3 language model
def ask_question(question):
    prompt = f"Q: {question}\nA:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    answer = response.choices[0].text.strip()
    return answer

# Function for text-to-speech functionality
def speak_text(text):
    
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)
    
    engine.say(text)
    engine.runAndWait() 

st.markdown("<h1 style='font-size: 42px; font-family: Courier New;'>Welcome to <span style='color: #D4AF37;'>DevBot AI</span>!</h1><p style = 'font-size: 18px;'>DevBot is an interactive chatbot assistant with a voiceover feature that can answer both basic and complex questions, depending on the user input. </p><br>", unsafe_allow_html=True)
# Initialize session state to store conversation history
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='font-size: 28px; font-family: Courier New;'>ChatBot<span style='color: #D4AF37;'> Console</span></h1><p style = 'font-size: 18px;'> Ask a question and DevBot will answer you right away. </p><br>", unsafe_allow_html=True)
# Split the screen into two columns
left_column, right_column = st.columns([4, 6])

# Define variable to hold latest bot answer
latest_answer = ""

# Get user message in the left column
with left_column:
    user_message = st.text_area("Enter your message:")

    # Store user message and generate bot response when the "Send" button is clicked
    if st.button("Send"):
        user_message_text =  f'<span style="color: green;">You:</span> {user_message}'
        st.session_state.conversation_history.insert(0, user_message_text) # Add user message to the beginning of the list
        answer = ask_question(user_message)
        bot_message_text = f'<span style="color: red;">Bot:</span> {answer}'
        st.session_state.conversation_history.insert(0, bot_message_text) # Add bot message to the beginning of the list
        latest_answer = answer
        user_message = ""
        
    gif_url = "https://miro.medium.com/v2/resize:fit:1200/1*9I6EIL5NG20A8se5afVmOg.gif"
    with st.columns(3)[0]:
        st.image(gif_url, width=260)
    


# Display conversation history in the right column
with right_column:
    st.write("Conversation history:")
    div_id = "conversation-history"
    st.markdown(f"""
        <div id="{div_id}" style="height: 400px; overflow-y: scroll; border: 1px solid #D4AF37; padding: 10px;">
            {"<br>".join(st.session_state.conversation_history)}
        </div>
        """,
        unsafe_allow_html=True
    )

# Play most recent bot response audio
if latest_answer:
   with st.spinner("DevBot is talking..."):
        speak_text(latest_answer)
  


footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Built with ❤ by <a style='display: block; text-align: center;' href="https://github.com/Deyb12" target="_blank">DAVE FAGARITA</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)
    
