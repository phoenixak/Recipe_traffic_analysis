def calculate_kpi(model_metrics, model_name):
    """Calculate and print the High Traffic Conversion Rate KPI."""
    train_conf_matrix = model_metrics['train']['confusion_matrix']
    test_conf_matrix = model_metrics['test']['confusion_matrix']
    
    # Assuming the confusion matrix layout is:
    # [[TN, FP],
    #  [FN, TP]]
    
    train_tp = train_conf_matrix[1, 1]
    train_fp = train_conf_matrix[0, 1]
    test_tp = test_conf_matrix[1, 1]
    test_fp = test_conf_matrix[0, 1]
    
    # Handle division by zero
    train_conversion_rate = train_tp / (train_tp + train_fp) if (train_tp + train_fp) > 0 else 0
    test_conversion_rate = test_tp / (test_tp + test_fp) if (test_tp + test_fp) > 0 else 0
    
    print(f"{model_name} - High Traffic Conversion Rate:")
    print(f"Train: {train_conversion_rate:.2f}")
    print(f"Test: {test_conversion_rate:.2f}")
    print("-----------------------------------------------------------------------------------")
