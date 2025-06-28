# ./otros/calcf1.py

from sklearn.metrics import f1_score
import pandas as pd

# Hidden ground truth
_true_labels = [4,1,4,2,4,1,2,4,5,3,2,4,3,3,5,5,1,1,5,4,5,4,3,4]

def evaluate_f1(predictions):
    """
    Receives a list of predicted labels and returns the F1 score
    comparing against hidden true labels.
    
    Args:
        predictions (list or array-like): predicted labels
    
    Returns:
        float: macro F1 score
    """
    df = pd.read_csv(predictions)
    pred = df['label'].to_list()
    if len(pred) != len(_true_labels):
        raise ValueError(f"Expected {len(_true_labels)} predictions, got {len(pred)}")
    return f1_score(_true_labels, pred, average='macro')
