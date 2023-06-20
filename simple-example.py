import openai

openai.api_key = "Hier deinen API-Key einfügen"

prompt = "Welche APIs gibt es von OpenAI?"

response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=[
		{"role": "user", "content": prompt}
	    ]
	)

print(response.choices[0].message["content"])
