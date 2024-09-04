# Recipe Site Traffic Analysis & Prediction

This project uses advanced language models to analyze car reviews. It includes tasks such as sentiment analysis, translation, question answering, and summarization. The project is modularized, and integrates MLflow for experiment tracking and Docker for containerization.

## Project Overview

The objective of this project is to analyze the traffic patterns of a recipe site and develop predictive models to forecast future traffic. By leveraging historical data and applying various machine learning algorithms, we aim to provide actionable insights that can help in optimizing content strategy, enhancing user engagement, and improving the overall user experience on the site.

Key Aspects
Sentiment Analysis: Determine the sentiment of car reviews.
Translation: Translate reviews into different languages.
Question Answering: Answer questions based on the review content.
Summarization: Summarize the reviews to capture key points.
Containerization: Docker is used to encapsulate the project environment.
Experiment Tracking: MLFlow is integrated for tracking experiments and model versions.

Features
Advanced Language Models: Implementation of LLMs for diverse NLP tasks.
Modular Architecture: The project is structured to allow easy integration and modification.
Experiment Tracking: MLFlow tracks different model versions and experiments.
Containerized Environment: Reproducible environment using Docker.

### Prerequisites

To run this project, you'll need to have the following software installed:

- Python 3.9 or higher
- pip (Python package installer)

You can install Python and pip by following the instructions [here](https://www.python.org/downloads/).

### Installing

Follow these steps to set up the project on your local machine:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/phoenixak/recipe-traffic-analysis.git
   cd recipe-traffic-analysisd

2. **Create a virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
Or 

1. **Build the Docker image:**

   ```bash
   docker build -t recipe_traffic_analysis.
  
   Run the Docker container:
2. **Run the Docker container:**

   ```bash
   Copy code
   docker run -v "$(pwd)/dataset":/app/dataset -it recipe_traffic_analysis

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any feature requests or bugs.


