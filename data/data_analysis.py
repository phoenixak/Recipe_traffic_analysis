import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data(df):
    """Perform exploratory data analysis."""
    sns.pairplot(df, hue='high_traffic')
    plt.show()

    # Histograms and boxplots
    numerical_columns = df.select_dtypes(include='float').columns
    for column in numerical_columns:
        plt.figure(figsize=(10, 4))

        # Histogram with KDE
        plt.subplot(1, 2, 1)
        sns.histplot(data=df, x=column, kde=True)
        plt.title(f"Distribution of {column.capitalize()}")

        # Boxplot
        plt.subplot(1, 2, 2)
        sns.boxplot(data=df, x=column)
        plt.title(f"Boxplot of {column.capitalize()}")

        plt.tight_layout()
        plt.show()
