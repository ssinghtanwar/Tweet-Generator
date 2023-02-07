import streamlit as st
import openai
import random

openai.api_key = "OpenAI_key"

prompt = [
    {
        "hashtag" : "#programer_lyf",
        "text" : "ask a question for a web developer"
    },
    {
        "hashtag" : "#python_pro",
        "text" : "tweet a meme regarding python"
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Write a tweet that highlights the benefits of using Python for data analysis."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Generate a tweet that talks about the ease of use of Python compared to other programming languages."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Create a tweet that showcases the latest advancements in the Python community."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Write a tweet that lists the most important libraries used in Python for machine learning."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Generate a tweet that talks about the role of Python in web development."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Create a tweet that highlights the importance of understanding the underlying concepts in Python."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Write a tweet that lists the benefits of contributing to open-source projects in Python."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "ask a question for a web developer"
    },
    {
        "hashtag" : "#python_pro",
        "text" : "tweet a meme regarding python"
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Write a tweet that highlights the benefits of using Python for data analysis."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Generate a tweet that talks about the ease of use of Python compared to other programming languages."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Create a tweet that showcases the latest advancements in the Python community."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Write a tweet that lists the most important libraries used in Python for machine learning."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Generate a tweet that talks about the role of Python in web development."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Create a tweet that highlights the importance of understanding the underlying concepts in Python."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Write a tweet that lists the benefits of contributing to open-source projects in Python."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Generate a tweet that talks about the importance of documentation in Python projects."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Create a tweet that highlights the popularity of Python among beginners and experienced developers alike."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that talks about the role of mentorship in the programming field."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that lists the common mistakes made by beginner programmers."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that lists the most popular applications of Python in the industry."
    },    
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet about the benefits of learning to code."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that highlights the importance of problem-solving skills in programming."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that compares and contrasts the different programming languages."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet that showcases the latest trends in the programming industry."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that lists some of the most common obstacles faced by beginner programmers."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that gives advice to aspiring programmers on how to get started in the field."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet ications coming soonthat highlights the importance of collaboration in programming projects."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that talks about the impact of open-source technologies in the programming world."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that shares interesting programming projects you have worked on."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet that talks about the role of creativity in programming."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that lists the most popular programming languages among developers."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet that talks about the challenges faced by experienced programmers."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that highlights the role of debugging skills in programming."
    },
    {
        "hashtag" : "#programer_lications coming soonyf",
        "text" : "Create a tweet that showcases the impact of technology in the field of programming."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Generate a tweet that talks about the importance of documentation in Python projects."
    },
    {
        "hashtag" : "#python_pro",
        "text" : "Create a tweet that highlights the popularity of Python among beginners and experienced developers alike."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that talks about the role of mentorship in the programming field."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that lists the common mistakes made by beginner programmers."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that lists the most popular applications of Python in the industry."
    },    
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet about the benefits of learning to code."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that highlights the importance of problem-solving skills in programming."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that compares and contrasts the different programming languages."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet that showcases the latest trends in the programming industry."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that lists some of the most common obstacles faced by beginner programmers."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that gives advice to aspiring programmers on how to get started in the field."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet that highlights the importance of collaboration in programming projects."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that talks about the impact of open-source technologies in the programming world."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that shares interesting programming projects you have worked on."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet that talks about the role of creativity in programming."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that lists the most popular programming languages among developers."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Write a tweet that talks about the challenges faced by experienced programmers."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Generate a tweet that highlights the role of debugging skills in programming."
    },
    {
        "hashtag" : "#programer_lyf",
        "text" : "Create a tweet that showcases the impact of technology in the field of programming."
    },
]


def generate_answer():
    chosen_promt = random.choice(prompt)
    text_openai = chosen_promt["text"]
    hashtags = chosen_promt["hashtag"]
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text_openai,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.9,
    )

    tweet = response.choices[0].text

    tweet = tweet + " " + hashtags

    return tweet



st.title("Programming Chatbot using GPT-3")

if st.button("Get answer"):
    answer = generate_answer()
    st.success(answer)
