from openai import OpenAI
client = OpenAI(apiKey="")

# Add json schema

def classify_UFC100():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # response_format={"type": "json_object"},
    messages=[
        {"role": "user", "content": "Who won the world series in 2020?"},
    ]
    )
    print(response.choices[0].message.content)

def classify_kinetics():
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    # response_format={"type": "json_object"},
    messages=[
        {"role": "user", "content": "Who won the world series in 2020?"},
    ]
    )
    print(response.choices[0].message.content)