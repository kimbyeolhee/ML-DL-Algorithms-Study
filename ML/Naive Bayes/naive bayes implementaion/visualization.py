import matplotlib.pyplot as plt

def boxplot(values, labels=['Neg','Pos']):
    plt.figure(figsize=(10,5))
    plt.bar(labels, values)
    plt.show()