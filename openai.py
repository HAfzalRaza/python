import openai
openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "write an essay about neuroscience" }])
print(completion.choices[0].message.content)