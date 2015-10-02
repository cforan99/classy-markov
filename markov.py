import sys
from random import choice

class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        texts = []

        for input_path in filenames:
            file_text = open(input_path).read()
            texts.append(file_text.split())

        self.make_chains(texts)


    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        chains = {}

        for text in corpus:
            for i in range(len(text) - 2):
                key = (text[i], text[i + 1])
                value = text[i + 2]

                if key not in chains:
                    chains[key] = []

                chains[key].append(value)

        self.corpus = chains

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        return " ".join(words)


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    n = len(sys.argv)
    input_paths = []
    for i in range(1, n):
        input_paths.append(sys.argv[i])

    # we should make an instance of the class
    basic_markov = SimpleMarkovGenerator()

    # we should call the read_files method with the list of filenames
    basic_markov.read_files(input_paths)

    # we should call the make_text method 5x
    for i in range(5):
        random_text = basic_markov.make_text(basic_markov.corpus)
        print random_text
        print "\n"