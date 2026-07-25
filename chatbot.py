from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage

load_dotenv()

model = ChatMistralAI(
    model="mistral-small-latest"
)

print("choose your AI mode")
print("press 1 for Angry Mode")
print("press 2 for funny mode")
print("press 3 for normal mode")

choice = input("tell your response:")

if choice == "1":
    mode = "You are an angry AI Agent. You respond aggresively and impatiently"

elif choice == "2":
    mode="You are a funny AI Agent. You respond with humor and jokes" 

elif choice == "3":
    mode="You are a normal AI Agent. You have answers to all the questions."

messages =[
    SystemMessage(content =mode)
   
]


print("------Welcome type 0 to exit the application-----")
while True:
   
    prompt = input("You:")
    messages.append(HumanMessage(content = prompt ))
    if prompt == "0":
        break
    response = model.invoke(messages)
    messages.append(AIMessage(content = response.content))
    print("ChatBot:",response.content)

print(messages)