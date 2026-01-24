import os
import pandas as pd

# Define file paths
#file_paths = [
#    'ConstPosFullPathes.csv',
#    'ConstPosOffsetFullPathes.csv',
#    'EventalStopFullPathes.csv',
#    'RandomPosFullPathes.csv',
#    'RandomPosOffsetFullPathes.csv'
#Number of attack samples: 3088653
#Number of non-attack samples: 739710

#]

file_paths =[
'client_data_25_50_100_200_client_1.csv',
'client_data_25_50_100_200_client_2.csv',
'client_data_25_50_100_200_client_3.csv' ,
'client_data_25_50_100_200_client_4.csv',
'client_data_25_50_100_200_client_5.csv'
#Number of attack samples: 70275
#Number of non-attack samples: 165870
#Number of attack samples: 53305
#Number of non-attack samples: 123920
#Percentage of Attack Samples: Approximately 30.1%
#Percentage of Non-Attack Samples: Approximately 69.9%
]
# data IID by sender 200
 #Number of attack samples: 112060
#Number of non-attack samples: 263900
#file_paths = [
#   'client_data_iid_1.csv',
#  'client_data_iid_2.csv',
 # 'client_data_iid_3.csv',
  #  'client_data_iid_4.csv',
 #   'client_data_iid_5.csv'
#]
def load_data(file_path):
    """Load a single CSV file into a DataFrame."""
    try:
        if os.path.exists(file_path):
            df = pd.read_csv(file_path)
            return df if not df.empty else None
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
    return None


def count_attacks_and_non_attacks(df):
    """Count the number of attack and non-attack samples."""
    # Define the mapping
    attack_labels = [1, 2, 3, 4, 9]  # Labels that correspond to attacks
    non_attack_label = 0  # Label that corresponds to non-attack

    # Count attacks and non-attacks
    num_attacks = df[df['label'].isin(attack_labels)].shape[0]
    num_non_attacks = df[df['label'] == non_attack_label].shape[0]

    return num_attacks, num_non_attacks


# Main Execution
for file_path in file_paths:
    data = load_data(file_path)

    if data is not None and 'label' in data.columns:
        # Count attacks and non-attacks
        num_attacks, num_non_attacks = count_attacks_and_non_attacks(data)

        # Print unique labels and their counts
        label_counts = data['label'].value_counts()

        print(f"File: {file_path}")
        print("Unique labels and counts:")
        print(label_counts)
        print(f"Number of attack samples: {num_attacks}")
        print(f"Number of non-attack samples: {num_non_attacks}\n")
    else:
        print(f"Error: No data loaded or 'label' column not found in {file_path}.")