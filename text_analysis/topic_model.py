import json
from gensim import corpora, models

from text_analysis.settings import PUBLIC_NAME, NUM_TOPICS, NUM_WORDS

with open('jsons/tokenized_posts_{}.json'.format(PUBLIC_NAME), 'r') as f:
    texts = json.load(f)

# dictionary creation
dictionary = corpora.Dictionary(texts)
print(dictionary)
dictionary.filter_extremes(no_below=5, no_above=0.5)
dictionary.compactify()
print(dictionary)
dictionary.save('models/{}.dict'.format(PUBLIC_NAME))

# corpus creation
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('models/{}.mm'.format(PUBLIC_NAME), corpus)

# LDA_model creation
ldamodel = models.LdaModel(corpus, num_topics=NUM_TOPICS, id2word=dictionary)
ldamodel.save('models/{}.model'.format(PUBLIC_NAME))

# generated topics
topics = ldamodel.print_topics(num_topics=NUM_TOPICS, num_words=NUM_WORDS)
print(ldamodel.show_topics())

