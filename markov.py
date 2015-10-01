import sys
from random import choice

class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""

        input_text = ""

        for input_path in filenames:
            file_text = open(input_path).read()
            input_text += " " + file_text

        return input_text


    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""

        # chains = {}

        # words = corpus.split()

        # for i in range(len(words) - 2):
        #     key = (words[i], words[i + 1])
        #     value = words[i + 2]

        #     if key not in chains:
        #         chains[key] = []

        #     chains[key].append(value)

        # return chains

    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        # key = choice(chains.keys())
        # words = [key[0], key[1]]
        # while key in chains:
        #     word = choice(chains[key])
        #     words.append(word)
        #     key = (key[1], word)

        # return " ".join(words)


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    n = len(sys.argv)
    input_paths = []
    for i in range(1, n):
        input_paths.append(sys.argv[i])

    # we should make an instance of the class

    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    pass