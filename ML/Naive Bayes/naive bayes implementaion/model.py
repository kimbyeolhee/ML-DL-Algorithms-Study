import math
import preprocess

def calculate_doc_prob(training_sentence, testing_sentence, alpha):
    logprob = 0

    training_model = preprocess.create_BOW(training_sentence)
    testing_model = preprocess.create_BOW(testing_sentence)

    for word in testing_model.keys():
        if word in training_model.keys():
            print(word, math.log(training_model[word] / sum(training_model.values())))
            logprob += math.log(training_model[word] / sum(training_model.values()))
        else:
            logprob += math.log(alpha / sum(training_model.values()))
            print('없는 단어:',word, math.log(alpha / sum(training_model.values())))
    return logprob

def normalize_log_prob(prob0, prob1):
    maxprob = max(prob0, prob1)

    print(prob0, prob1)

    prob0 = prob0 - maxprob
    prob1 = prob1 - maxprob
    prob0 = math.exp(prob0)
    prob1 = math.exp(prob1)

    normalize_constant = 1.0 / float(prob0 + prob1)
    prob0 = prob0 * normalize_constant
    prob1 = prob1 * normalize_constant

    print(2,prob0, prob1)

    return (prob0, prob1)

def naive_bayes(training_sentence, testing_sentence):
    log_prob_negative = calculate_doc_prob(training_sentence[0], testing_sentence, 0.1) + math.log(0.5)
    log_prob_positive = calculate_doc_prob(training_sentence[1], testing_sentence, 0.1) + math.log(0.5)
    prob_pair = normalize_log_prob(log_prob_negative, log_prob_positive)

    return prob_pair

