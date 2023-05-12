import openai
openai.api_key = "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"

while True:
    prompt = input("\nIntroduce una pregunta: ")

    if prompt == "exit":
        break

    completion = openai.Completion.create(engine="text-davinci-003",
                            prompt=prompt,
                            max_tokens=2048)

    print(completion.choices[0].text)
                        