import gensim
import pyLDAvis
import pyLDAvis.gensim

from text_analysis.settings import PUBLIC_NAME

dictionary = gensim.corpora.Dictionary.load('models/{}.dict'.format(PUBLIC_NAME))
corpus = gensim.corpora.MmCorpus('models/{}.mm'.format(PUBLIC_NAME))
lda = gensim.models.ldamodel.LdaModel.load('models/{}.model'.format(PUBLIC_NAME))

data = pyLDAvis.gensim.prepare(lda, corpus, dictionary)
pyLDAvis.save_html(data, 'models/{}.html'.format(PUBLIC_NAME))
