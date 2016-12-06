# Creates a vocabulary file containing all words in files in the
# word_sim_dir. Meant for collecting all words in one file.
import sys
import os

if __name__ == '__main__':
    word_sim_dir = sys.argv[1]
    out_vocab = sys.argv[2]
    vocab = set()
    for i, filename in enumerate(os.listdir(word_sim_dir)):
        for line in open(os.path.join(word_sim_dir, filename), 'r'):
            line = line.strip().lower()
            word1, word2, val = line.split()
            vocab.update([word1, word2])
    f = open(out_vocab, 'wb')
    for word in vocab:
        f.write("%s\n" % word)
