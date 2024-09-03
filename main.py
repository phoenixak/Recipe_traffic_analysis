from data.data_loader import load_data
from data.data_cleaning import clean_data
from data.data_analysis import analyze_data
from models.model_training import train_models
from models.kpi import calculate_kpi
from utils.logger import setup_logger

def main():
    # Set up logging
    logger = setup_logger()

    try:
        # Load data
        logger.info("Loading data...")
        df = load_data()

        # Clean data
        logger.info("Cleaning data...")
        df_cleaned = clean_data(df)

        # Analyze data
        logger.info("Analyzing data...")
        analyze_data(df_cleaned)

        # Train models
        logger.info("Training models...")
        model_metrics = train_models(df_cleaned)

        # Calculate KPIs
        logger.info("Calculating KPIs...")
        for model_name, metrics in model_metrics.items():
            calculate_kpi(metrics, model_name)
    
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
