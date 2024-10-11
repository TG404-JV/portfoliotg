import openai

# Set your API key
openai.api_key = 'YOUR_API_KEY'

# Make a request to the GPT API using the new method
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or use another available model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the meaning of life?"}
    ]
)

# Print the generated response
print(response['choices'][0]['message']['content'])
