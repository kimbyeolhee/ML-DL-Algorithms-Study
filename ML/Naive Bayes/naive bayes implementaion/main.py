# module
import dataset
import model
import visualization

def main(input):
    training_sentence, testing_sentence = dataset.load_data(), input
    prob_pair = model.naive_bayes(training_sentence, testing_sentence)
    visualization.boxplot(prob_pair)

if __name__ == '__main__':
    main('어설픈 연기가 너무 형편없어요')

