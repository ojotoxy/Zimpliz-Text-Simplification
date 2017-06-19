FROM heryandi/python3-nltk-gensim:python-3.4.0-nltk-3.0.0b1-gensim-0.10.0

RUN pip3 install --upgrade nltk && python3 -m nltk.downloader all

RUN git clone https://github.com/ojotoxy/Zimpliz-Text-Simplification.git
