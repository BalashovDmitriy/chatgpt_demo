import openai
from os import getenv

OPENAI_API_KEY = getenv("OPENAI_API_KEY")
print(OPENAI_API_KEY)

openai.api_key = OPENAI_API_KEY


def generate_response(text):
    response = openai.Completion.create(
        prompt=text,
        engine="text-davinci-003",
        max_tokens=1000,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    if response and response.choices:
        return response.choices[0].text.strip()
    else:
        return None


if __name__ == '__main__':
    print("Привет! Чем могу помочь?")
    while True:
        user_input = input()
        print(generate_response(user_input))
