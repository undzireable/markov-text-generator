from sampling import sample_next

def generateText(starting_sent,model, k=4, maxLen=1000):
    sentence = starting_sent
    ctx = starting_sent[-k:]

    for ix in range(maxLen):
        next_prediction = sample_next(ctx, model, k)
        sentence += next_prediction
        ctx = sentence[-k:]
    return sentence
