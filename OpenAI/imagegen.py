import openai

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

openai.api_key = open_file('/home/bhanu12/Keys/openaiapi.txt')


response = openai.Image.create(
  prompt='Honesty is the best policy',
  n=1,
  size="256x256"
)
image_url = response['data'][0]['url']
# print(image_url)
print(response)

# if __name__ == '__main__':
#     prompt = 'Vani is a really good friend. She is quite busy but hardly calls. how can i nudge her to call more often'
#     response = gpt3_completion(prompt)
#     print(response)

# def gpt3_completion(prompt, engine='text-davinci-002', temp=0.7, top_p=1.0, tokens=400, freq_pen=0.0, pres_pen=0.0, stop=['<<END>>']):
    # prompt = prompt.encode(encoding='ASCII',errors='ignore').decode()
    # response = openai.Completion.create(
    #     engine=engine,
    #     prompt=prompt,
    #     temperature=temp,
    #     max_tokens=tokens,
    #     top_p=top_p,
    #     frequency_penalty=freq_pen,
    #     presence_penalty=pres_pen,
    #     stop=stop)
    # text = response['choices'][0]['text'].strip()
    # return text
# 

import os
import openai
openai.api_key = open_file('/home/bhanu12/Keys/openaiapi.txt')
openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)


