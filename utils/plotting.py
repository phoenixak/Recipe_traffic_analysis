import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograms(df, columns):
    """Plot histograms for specified columns."""
    for column in columns:
        sns.histplot(data=df, x=column, kde=True)
        plt.title(f"Distribution of {column.capitalize()}")
        plt.show()

def plot_boxplots(df, columns):
    """Plot boxplots for specified columns."""
    for column in columns:
        sns.boxplot(data=df, x=column)
        plt.title(f"Boxplot of {column.capitalize()}")
        plt.show()
