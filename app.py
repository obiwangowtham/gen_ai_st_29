import streamlit as st
from openai import OpenAI
#f=open("op_k.txt","r")
#open_ai_key=f.read().strip()

#make the key secret
open_ai_key=st.secrets["open_ai_key"]
client=OpenAI(api_key=open_ai_key)
#-------------


st.title("AI Chatbot")
st.chat_message("assistant").write("Hi, How may i help you?")
if "messages" not in st.session_state:
    st.session_state["messages"]=[]
for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])
user_input=st.chat_input("Ask something about the movie Lion king")
if user_input:
    st.chat_message("user").write(user_input)
    response=client.chat.completions.create(model="gpt-3.5-turbo",
                                            messages=[{"role":"system","content":"""
                                        you are known to be a polite and helpful AI bot.Act as a movie 
                                                       assistant and answer all the queries realted to the movie "the lion 
                                                       king".Your primary task is to help the  movie enthusiast get the right response.
                                                       If the user query is not relevant to the movie lion king,politely ask the user for
                                                       doubts related to the context"""}]+st.session_state["messages"]+
                                                       [{"role":"user","content":user_input}])
    st.chat_message("assistant").write(response.choices[0].message.content)
    st.session_state["messages"].append({"role":"user","content":user_input})
    st.session_state["messages"].append({"role":"assistant","content":response.choices[0].message.content})
