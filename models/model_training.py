import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

def train_models(df):
    """Train and evaluate multiple models."""
    
    # One-hot encode 'category' and prepare X and y
    df_encoded = pd.get_dummies(df, columns=['category'], drop_first=True)
    X = df_encoded.drop('high_traffic', axis=1)
    y = df_encoded['high_traffic']
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=7)
    
    # Models to evaluate
    models = {
        "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=2000, solver='lbfgs')),
        "Decision Tree": DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(),
        "Support Vector Machines": make_pipeline(StandardScaler(), SVC(probability=True))
    }
    
    model_metrics = {}
    
    for model_name, model in models.items():
        with mlflow.start_run(run_name=model_name):
            # Train model
            model.fit(X_train, y_train)
            y_pred_train = model.predict(X_train)
            y_pred_test = model.predict(X_test)
            
            # Compute confusion matrices
            conf_matrix_train = confusion_matrix(y_train, y_pred_train)
            conf_matrix_test = confusion_matrix(y_test, y_pred_test)
            
            # Evaluation metrics
            metrics = {
                'train': {
                    'accuracy': accuracy_score(y_train, y_pred_train),
                    'precision': precision_score(y_train, y_pred_train),
                    'recall': recall_score(y_train, y_pred_train),
                    'f1': f1_score(y_train, y_pred_train),
                    'confusion_matrix': conf_matrix_train
                },
                'test': {
                    'accuracy': accuracy_score(y_test, y_pred_test),
                    'precision': precision_score(y_test, y_pred_test),
                    'recall': recall_score(y_test, y_pred_test),
                    'f1': f1_score(y_test, y_pred_test),
                    'confusion_matrix': conf_matrix_test
                }
            }
            
            model_metrics[model_name] = metrics
            
            # Log parameters and metrics to MLflow
            mlflow.log_param("model_type", model_name)
            mlflow.log_metric("train_accuracy", metrics['train']['accuracy'])
            mlflow.log_metric("test_accuracy", metrics['test']['accuracy'])
            mlflow.log_metric("train_precision", metrics['train']['precision'])
            mlflow.log_metric("test_precision", metrics['test']['precision'])
            mlflow.log_metric("train_recall", metrics['train']['recall'])
            mlflow.log_metric("test_recall", metrics['test']['recall'])
            mlflow.log_metric("train_f1", metrics['train']['f1'])
            mlflow.log_metric("test_f1", metrics['test']['f1'])
            
            # Infer model signature
            signature = infer_signature(X_train, model.predict(X_train))
            
            # Log the model with signature and input example
            mlflow.sklearn.log_model(model, model_name, signature=signature, input_example=X_train.iloc[:5])
            
    return model_metrics
