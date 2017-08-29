import json
import os
import gensim
import pickle
from gensim.models.doc2vec import Doc2Vec
from nltk import sent_tokenize

publics = ['pn6', 'overhear']
model_file = 'public.d2v'


def read_corpus(data):
    for i, line in enumerate(data):
        yield gensim.models.doc2vec.TaggedDocument(line, [i])


if __name__ == '__main__':
    # with open(book, 'rb') as f:
    #     data = pickle.load(f)
    post_set = []
    for public in publics:
        jsons = os.listdir('jsons/{}'.format(public))
        for j in jsons:
            with open('jsons/{}/{}'.format(public, j), 'r') as f:
                post_set += json.load(f)
    all_text = '\n'.join(list(map(lambda x: x['text'], post_set)))
    # sentences = '\n'.join(sent_tokenize(all_text)) proebisto
    sentences = sent_tokenize(all_text)

    corpus = list(read_corpus(sentences))
    # print(corpus)
    if (os.path.isfile(model_file)):
        model = Doc2Vec.load(model_file)
    else:
        model = gensim.models.doc2vec.Doc2Vec(size=300, iter=50)
        model.build_vocab(corpus)

        for epoch in range(10):
            print("train epoch: " + str(epoch))
            model.train(corpus, total_examples=model.corpus_count, epochs=1)
            model.alpha -= 0.002
            model.min_alpha = model.alpha

        model.save(model_file)

    sentence = ['И', 'тогда', 'я', 'пошел', 'зарабатывать', 'для', 'того',
                'чтобы', 'выжить']

    inferred_vector = model.infer_vector(sentence)
    print(inferred_vector)

    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    print(sims[:10])
    print(len(sims), '    ', len(corpus))
    # Compare and print the most similar documents from the train corpus
    for index in range(10):
        print(u'%s %s: «%s»\n' % (index, sims[index], ' '.join(corpus[sims[index][0]].words)))
