import openai

openai.api_key = "API KEY HIER EINFÜGEN"

prompt = "Welche APIs gibt es von OpenAI?"

response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=[
		{"role": "user", "content": prompt}
	    ]
	)

print(response.choices[0].message["content"])