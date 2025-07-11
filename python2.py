
# Create a function that takes orders of different customers and then prints all the items in the order respectively
#Items=Parameter
# Take Order=Function
# def take_orders(*orders):
#     for i in orders:
#         print("",i)
# take_orders("burger","fries","pizza")

# def greet(**parameters):
#  print("Hope you liked our services!")
#  print("The items you ordered are:")
#  for i,j in parameters.keys() :
#   print(f"{i},: {j}")
#  print("Your Total Bill Is:")
#  print(totalbilling(**parameters))

#  def totalbilling(**prices):
#     sum = 0
#     for i in prices:
#        sum+= prices[i]
#     return sum
 
#  greet(a=12,b=13,d=34,e=57)

# Write a function to find volume of a cuboid with the help of area of rectangle function
# l=float(input("Enter Length Of Rectangle"))
# b=float(input("Enter Breadth Of Rectangle"))
# h=float(input("Enter Height Of Rectangle"))
# def volume(l,b,h):
#     volume= area(l,b)*h
#     return volume 
# def area(l,b):
#     area=l*b
#     return area
# volume(l,b,h)
# area(l,b)
# print("Volume is",volume(l,b,h))
# print("Area is",area(l,b))
    
# Element = int(input("Enter The Element You Wish To Print For The Fibonacci numbers: "))
# a = 0
# b = 1
# print(a)
# print(b)
# for i in range(3, Element + 1):
#     c = a + b
#     a = b
#     b = c
#     print(c)

# def fibbonnaci(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#          return fibbonnaci(n-1)+fibbonnaci(n-2)
# n=int(input("Enter a number:"))
# for i in range(n):
#     print(fibbonnaci(i))

# def factorial(n):
#  if n==1 :
#    return 1
#  return n*factorial(n-1)

# n=int(input("Enter a number:"))
# a=factorial(n)
# print(a)

# def Add(x,y):
#     return x+y


# add= lambda x,y:x+y
# print(add(3,4))
 
#    Create a one line function to find exponential of a number with some other number take base and exponent as an input from user
# n = lambda: float(input("Base: ")) ** float(input("Exponent: "))
# print(n)
# def squares(argument):
#     return argument**2
# numbers=[1,2,3,4,5]

# squares=list(map(squares,numbers))
# print(squares)

# numbers= [1,2,3,4,5]

# numberless3 = list(filter(lambda x:x<=3,numbers))
# print(numberless3)

# pairs= [[1,5],[3,3],[2,4]]

# print(sorted(pairs,key= lambda x: x[1]**(-2)))

# list1 =[["A",17],["B",12],["C",15],["D",13],["E",10]]
# #1. Reduce 2 points from every racer's score
# # 2. After reduction print only the racer's that have points above the mean
# # 3. Sort the list on the basis of scores and tell the name of the top racer
# print(sorted(list1,key=lambda x:x[1]))
# print(sorted(list1,key=lambda x:x[1])[-1])
# reduced_scores = list(map(lambda x:x[1] - 2, list1))
# avg_score = sum(reduced_scores) / len(reduced_scores)
# reduced_scores.sort
# newlist=list(filter(lambda x:x>avg_score,reduced_scores))
# print(newlist)
# print(reduced_scores)


#  HW-Create a quiz game having 5 questions make it a multiplayer game and after completion of all players game, show the scoreboard also display the winner. Use functions
# def ask_questions(questions):
#     score = 0
#     for q, ans in questions:
#         user_ans = input(q + " ")
#         if user_ans.lower() == ans.lower():
#             score += 1
#     return score

# def main():
#     questions = [
#         ("What is the capital of India?", "Delhi"),
#         ("What is 5 + 5?", "10"),
#         ("Who won the 2022 FIFA World Cup?", "Argentina"),
#         ("Who wrote 'Harry Potter'?", "J.K. Rowling"),
#         ("What is the largest planet in our solar system?", "Jupiter")
#     ]
#     num_players = int(input("Enter number of players: "))
#     scores = []
#     names = []
#     for i in range(num_players):
#         name= input(f"Enter name for Player {i+1}: ")
#         names.append(name)
#         print(f"{names}, it's your turn!")
#         score = ask_questions(questions)
#         scores.append(score)
#     print("\n--- Scoreboard ---")
#     for i in range(num_players):
#         print(f"{names[i]}: {scores[i]} points")
#     max_score = max(scores)
#     winners = []
#     for i in range(num_players):
#         if scores[i] == max_score:
#             winners.append(names[i])
#     if len(winners) == 1:
#         print(f"\nWinner: {winners[0]}!")
#     else:
#         print(f"\nIt's a tie between: {'', winners}")

#   main()
# import google.generativeai as genai

# geminikey="AIzaSyCBE95l579vFQBQeJ0NeNbx6nYS5gGH7C4"
# genai.configure(api_key = geminikey)
# model=genai.GenerativeModel("gemini-2.0-flash")
# print(model.generate_content("Tell me the top 7 wonders of the world").text)

# def geminiresponse(userinput):
#     print("Here's the response from gemini")
#     return model.generate_content(userinput).text

# a= input("Enter the topic that you want to know about:")

# ans = geminiresponse(a)
# print(ans)
# know_more = input("Want to get a detailed answer [Y/N]")

# if (know_more =="Y"):
#     detailed_response=geminiresponse(f"Explain in detail about {a}")

# else:
#     print("Thanks for using gemini")





import streamlit as st
import google.generativeai as genai

# Setup
genai.configure(api_key="AIzaSyCBE95l579vFQBQeJ0NeNbx6nYS5gGH7C4")
model = genai.GenerativeModel("gemini-2.0-flash")

def geminiresponse(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"

# App UI
st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini AI Assistant")

# Initialize session state
if "summary" not in st.session_state:
    st.session_state.summary = ""
if "detailed" not in st.session_state:
    st.session_state.detailed = ""
if "short_summary" not in st.session_state:
    st.session_state.short_summary = ""

# User input
user_input = st.text_input("🔍 Enter a topic you'd like to know about:")

# Generate summary
if st.button("Generate Summary"):
    if user_input:
        st.session_state.summary = geminiresponse(user_input)
        st.session_state.detailed = ""  # Reset other states
        st.session_state.short_summary = ""
    else:
        st.warning("Please enter a topic!")

# Show summary if available
if st.session_state.summary:
    st.subheader("📄 Summary:")
    st.write(st.session_state.summary)

    col1, col2 = st.columns(2)

    # Get Detailed Answer
    if col1.button("🔍 Get Detailed Answer"):
        st.session_state.detailed = geminiresponse(f"Explain in detail about {user_input}")

    if st.session_state.detailed:
        st.subheader("🔬 Detailed Explanation:")
        st.write(st.session_state.detailed)

    if st.session_state.short_summary:
        st.subheader("🧾 Further Summarized Version:")
        st.write(st.session_state.short_summary)

# Footer
st.markdown("---")
st.caption("Powered by Gemini Flash • Made with ❤️ using Streamlit")

