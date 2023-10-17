# proper import statements
import openai

# this function takes in a text input and return ChatGPT's response
def find_response_date(full_text):
    
    openai.api_key = "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"

    # setting the paramters for response
    response = openai.Completion.create(
        engine = 'text-davinci-003',
        prompt = full_text,
        max_tokens = 100,
        temperature = 1,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0,
        n = 1,
        stop = None
    )

    response_final = response.choices[0].text.strip()
    print("response done")
    return response_final

# set the industry
industry = "credit cards"

# set of questions
question_1 = "What is the market size of " + industry + " in 2023?"
question_2 = "What are the major highlights of " + industry + ", in 2023?"
question_3 = "What are the drivers behind the market size growth of " + industry + "?"
question_4 = "Who is the target audience for " + industry +  "?"
question_5 = "What challenges do customers face in adopting " + industry + "?"
question_6 = "Can you list major competitors in " + industry + " with their market share and competitive advantage and a SWOT of each competitor?"
question_7 = "What are the barriers to entry in " + industry + "?"

full_text = question_1 # question to input
result = find_response_date(full_text)
print(result)

# to input all the questions at once, uncomment the code below
'''
question_array = [question_1, question_2, question_3, question_4, question_5, question_6, question_7]

for question in question_array:
    full_text = question # question to input
    result = find_response_date(full_text)
    print(result)
'''



