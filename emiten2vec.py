#
# Emiten2Vec
#
# https://github.com/anvie/emiten2vec
#
#

from gensim.models import Word2Vec

import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Emiten2Vec\nhttps://github.com/anvie/emiten2vec')
    parser.add_argument('--model', default='model/emiten2vec.model', help='Path ke file model')
    return parser.parse_args()

def main():
    args = parse_args()

    print("Memuat...")
    m = Word2Vec.load(args.model)

    while True:
        keyword = input("> Masukkan kata kunci: ")

        result = m.wv.most_similar(positive=keyword, topn=10)
        for em, sc in result:
            print(f"   * {em}\t{sc}")
        print("")

if __name__ == "__main__":
    main()
