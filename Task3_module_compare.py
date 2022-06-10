def compare (S1, S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count / max(len(S1), len(S2))

if __name__ == '__main__':
    pairs = [
    ('kitten', 'sitting'),
    ('saturday', 'sunday'),
    ('море', 'гора'),
    ('компьютер', 'компьютеры')
    ]
    for s, t in pairs:
        print(s, t, compare(s, t))