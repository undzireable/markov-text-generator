from generator import generateText
from training import load_text
from markov import MarkovChain

text=load_text("trainingData.txt")
model=MarkovChain(text,4)
print(generateText("coun",model,4,6))

