import json
import os

from nltk.tokenize import RegexpTokenizer
import pymorphy2
from stop_words import get_stop_words
from tqdm import tqdm

from text_analysis.settings import PUBLIC_NAME


def parse(text):
    text = text.strip().lower()
    raw_tokens = tokenizer.tokenize(text)
    stopped_tokens = [i for i in raw_tokens if (not i in stop_words) and (len(i) > 2)]
    norm_tokens = [morph.parse(i)[0].normal_form for i in stopped_tokens]
    return norm_tokens

post_set = []
jsons = os.listdir('jsons/{}'.format(PUBLIC_NAME))
for json_file in jsons:
    with open('jsons/{}/{}'.format(PUBLIC_NAME, json_file), 'r') as f:
        post_set += json.load(f)
        print(len(post_set))

tokenized_posts = []
tokenizer = RegexpTokenizer(r'[а-я]+')
morph = pymorphy2.MorphAnalyzer()
stop_words = get_stop_words('ru')

num_united_posts = 0

for post, _ in zip(post_set, tqdm(range(len(post_set)))):
    tokens = []
    if num_united_posts < 9:
        tokens += parse(post['text'])
        num_united_posts += 1
    else:
        tokens += parse(post['text'])
        tokenized_posts.append(tokens)
        num_united_posts = 0

print('token ', len(tokenized_posts))

with open('jsons/tokenized_posts_{}.json'.format(PUBLIC_NAME), 'w') as f:
    json.dump(tokenized_posts, f, indent=4)

