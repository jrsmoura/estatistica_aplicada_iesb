import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    raw_df = pd.read_csv('./data/VarQuanti.csv')
    print(raw_df.head())
    print(raw_df.describe())
    raw_df['Idade'].hist(color='blue', alpha=0.7)
    raw_df['Altura'].hist(color='red', alpha=0.7)
    raw_df['Peso'].hist(color='green', alpha=0.7)
    plt.show()
