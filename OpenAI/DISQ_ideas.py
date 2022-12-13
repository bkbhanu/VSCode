import openai


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


openai.api_key = open_file('/home/bhanu12/Keys/openaiapi.txt')


def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=temp,
        max_tokens=tokens,
        top_p=top_p,
        frequency_penalty=freq_pen,
        presence_penalty=pres_pen,
        stop=stop)
    text = response['choices'][0]['text'].strip()
    return text


if __name__ == '__main__':
    prompt = 'Digital Impact Square (DISQ), A Tata Consultancy Services (TCS) Foundation Initiative, is an open social innovation center - in the city of Nashik, Maharashtra. DISQ encourages innovation using digital technologies to address social challenges prevalent in Health and Hygiene, Housing and Transportation, Food and Agriculture, Energy, Water and Environment, Financial and Personal Security, Citizen Empowerment and Transparency, Education and Skills development across India. These challenges are drawn from the voice of citizens, domain experts, local administration and government. To know more about Digital Impact Square, watch video here Digital Impact Square: Is a living lab where research and technology from academia and industry influences everyday life Fosters a culture of innovation through a series of sustained innovation cycles Accelerates the journey of many from being ideators to entrepreneurs, researchers or corporate leaders. Write a sample email to share the quarterly impact report detailing the impact of each startups incubated at DISQ'
    response = gpt3_completion(prompt)
    print(response)