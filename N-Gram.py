# very elegant way to generate N-gram in python using * star
input_list = ['all', 'this', 'happened', 'more', 'or', 'less']

def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])
