import json

from nltk.tokenize import RegexpTokenizer
import pymorphy2
from stop_words import get_stop_words

from text_analysis.settings import PUBLIC_NAME

with open('jsons/{}.json'.format(PUBLIC_NAME), 'r') as f:
    post_set = json.load(f)
    print(len(post_set))


tokenized_posts = []
tokenizer = RegexpTokenizer(r'[а-я]+')
morph = pymorphy2.MorphAnalyzer()
stop_words = get_stop_words('ru')

for post in post_set:
    text = post['text'].strip().lower()
    raw_tokens = tokenizer.tokenize(text)
    stopped_tokens = [i for i in raw_tokens if (not i in stop_words) and (len(i) > 2)]
    norm_tokens = [morph.parse(i)[0].normal_form for i in stopped_tokens]
    tokenized_posts.append(norm_tokens)

with open('jsons/tokenized_posts_{}.json'.format(PUBLIC_NAME), 'w') as f:
    json.dump(tokenized_posts, f, indent=4)

