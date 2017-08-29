import json

import gensim
import pyLDAvis
import pyLDAvis.gensim

from text_analysis.settings import PUBLIC_NAME

dictionary = gensim.corpora.Dictionary.load('models/{}.dict'.format(PUBLIC_NAME))
corpus = gensim.corpora.MmCorpus('models/{}.mm'.format(PUBLIC_NAME))
lda = gensim.models.ldamodel.LdaModel.load('models/{}.model'.format(PUBLIC_NAME))

top = lda.top_topics(corpus)
topics = []
for t in top:
    topics.append(list(map(lambda x: x[1], sorted(t[0], key=lambda x: -x[0])[:5])))
print(topics)
with open('jsons/{}_topics.json'.format(PUBLIC_NAME), 'w') as f:
    json.dump(topics, f, indent=4)


data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(data, 'models/{}.html'.format(PUBLIC_NAME))
