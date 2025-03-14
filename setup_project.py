import os
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define the project structure
list_of_files = [
    # Python package structure
    'src/__init__.py',
    'src/data/__init__.py',
    'src/data/make_dataset.py',
    'src/data/preprocess.py',
    'src/features/__init__.py',
    'src/features/build_features.py',
    'src/models/__init__.py',
    'src/models/train_model.py',
    'src/models/evaluate_model.py',
    'src/visualization/__init__.py',
    'src/visualization/visualize.py',

    # Data directories
    'data/raw/.gitkeep',
    'data/processed/.gitkeep',

    # Notebooks
    'notebooks/exploratory.ipynb',

    # Project files
    '.env',
    'requirements.txt',
    'setup.py',
    'README.md',
    '.gitignore'
]

# Create the directories and files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create the directory if it doesn't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            if filename == '.gitignore':
                f.write(
                    """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
dist/
build/
*.egg-info/

# Virtual environments
venv/
env/
ENV/

# Jupyter Notebook
.ipynb_checkpoints

# VS Code
.vscode/

# Data files (optional, if you don't want to track large data files)
*.csv
*.json
*.txt
!requirements.txt

# Conda
.conda/
""")
            elif filename == 'requirements.txt':
                f.write(
                    """numpy==1.24.3
pandas==2.0.2
matplotlib==3.7.1
seaborn==0.12.2
scikit-learn==1.2.2
nltk==3.8.1
textblob==0.17.1
tweepy==4.14.0
""")
            elif filename == 'README.md':
                f.write(
                    """# Social Media Sentiment Analysis

A machine learning project to analyze sentiment in social media posts.

## Project Structure

- `data/`: Contains raw and processed datasets
- `notebooks/`: Jupyter notebooks for exploration
- `src/`: Source code organized in modules
  - `data/`: Data processing scripts
  - `features/`: Feature engineering
  - `models/`: Model training and evaluation
  - `visualization/`: Visualization scripts

## Setup
""")
        logging.info(f"Created file: {filepath}")
