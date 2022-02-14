from lookup_table import generateTable
from probability_table import convertFreqIntoProb

def MarkovChain(text, k=4):
    T = generateTable(text, k)
    T = convertFreqIntoProb(T)
    return T
