# ComplaintIQ – Consumer Complaint Classification System

An NLP-powered machine learning application that automatically classifies consumer financial complaints into relevant product categories using Natural Language Processing (NLP) and Machine Learning.

## Overview

ComplaintIQ is a text classification project developed using the Consumer Financial Protection Bureau (CFPB) consumer complaint dataset.

The application accepts a consumer complaint as text, processes the input, and predicts the most relevant financial product category using a trained Machine Learning model.

The project aims to simplify complaint categorization and demonstrate an end-to-end NLP and Machine Learning workflow.

## Key Features

- **Complaint Classification:** Predicts the product category of a consumer complaint.
- **Text Processing:** Processes complaint text before classification.
- **Machine Learning:** Uses a trained Linear Support Vector Classifier.
- **TF-IDF Vectorization:** Converts textual data into numerical features.
- **Model Performance:** Displays evaluation metrics of the trained model.
- **Interactive Dashboard:** Provides a user-friendly interface.
- **Light and Dark Mode:** Supports theme switching.
- **Responsive Design:** Works on desktop and mobile devices.
- **Input Validation:** Handles empty inputs and invalid submissions.
- **Prediction Results:** Displays the predicted category and processed text.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| NLP | NLTK, Scikit-learn |
| Feature Extraction | TF-IDF Vectorizer |
| Machine Learning | Naive Bayes, Logistic Regression, Linear SVC |
| Backend | Flask |
| Frontend | HTML, CSS, JavaScript |
| Model Serialization | Joblib |
| Development Environment | Jupyter Notebook, Google Colab |

## Dataset

**Source:** Consumer Financial Protection Bureau (CFPB) Consumer Complaints Dataset.

The dataset contains consumer complaints related to various financial products and services.

### Dataset Information

| Description | Details |
|---|---:|
| Original records | 3,093,136 |
| Records with narratives | 1,111,330 |
| Final cleaned records | 970,109 |
| Product categories | 18 |

The project focuses on two primary columns:

- `Consumer complaint narrative` – Text describing the consumer's complaint.
- `Product` – Category associated with the complaint.

## Project Workflow

The project follows an end-to-end NLP and Machine Learning workflow.

1. **Data Collection:** Collected consumer complaint data from the CFPB dataset.
2. **Exploratory Data Analysis:** Analyzed dataset structure, missing values, duplicate records, class distribution, and text characteristics.
3. **Text Preprocessing:** Cleaned and prepared complaint narratives for NLP tasks.
4. **Feature Extraction:** Converted text into numerical representations using Bag of Words and TF-IDF.
5. **Model Training:** Trained and evaluated multiple machine learning classification algorithms.
6. **Class Imbalance Handling:** Applied class weighting to improve minority-class performance.
7. **Model Evaluation:** Compared models using accuracy, precision, recall, F1-score, and other evaluation metrics.
8. **Model Saving:** Saved the selected trained model and TF-IDF vectorizer.
9. **Web Application Development:** Integrated the trained model into a Flask application.

## Machine Learning Models

The following models were experimented with:

- Multinomial Naive Bayes
- Logistic Regression
- Linear Support Vector Classifier (Linear SVC)

### Final Model

**Selected Model:** Balanced Linear SVC

**Feature Representation:** TF-IDF Unigram

Class weighting was used to address class imbalance during model training.

### Model Performance

| Evaluation Metric | Score |
|---|---:|
| Accuracy | 82.945% |
| Macro Precision | 48.514% |
| Macro Recall | 45.821% |
| Macro F1-Score | 44.369% |
| Weighted F1-Score | 83.427% |

**Observation:** The model achieves a good overall accuracy and weighted F1-score. However, the lower macro F1-score indicates that classification performance varies across product categories, particularly for minority classes.

## Project Structure

```text
ComplaintIQ/
│
├── app.py
│
├── final_svc_model.pkl
├── tfidf_unigram.pkl
│
├── templates/
│   ├── index.html
│   ├── classify.html
│   ├── performance.html
│   └── about.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       ├── script.js
│       └── classify.js
│
├── notebooks/
│   ├── Data_collection_EDA.ipynb
│   ├── Text_Preprocessing.ipynb
│   ├── Text_feature_extraction.ipynb
│   └── Machine_Learning_Model_Training.ipynb
│
├── requirements.txt
│
└── README.md
```

*Note: Update the structure if your actual filenames or folder organization differ.*

## Installation and Setup

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ComplaintIQ.git
```

### 2. Navigate to the Project Directory

```bash
cd ComplaintIQ
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Model Files

Ensure the following trained model files are available in the project directory:

```text
final_svc_model.pkl
tfidf_unigram.pkl
```

### 6. Run the Flask Application

```bash
python app.py
```

### 7. Open the Application

Open your browser and navigate to:

```text
http://127.0.0.1:5000/
```

## Application Pages

### 1. Dashboard

Provides an overview of the ComplaintIQ application and its purpose.

### 2. Classify Complaint

Allows users to enter consumer complaint text and receive a predicted financial product category.

### 3. Model Performance

Displays the evaluation metrics of the selected machine learning model.

### 4. About Project

Provides information about the project, technologies, dataset, and development workflow.

## Testing

The application can be tested using the following scenarios:

- Valid consumer complaints.
- Empty text submissions.
- Complaints containing special characters.
- Complaints containing spelling mistakes.
- Very short and long complaint narratives.
- Repeated classification requests.
- Light and dark theme switching.
- Mobile navigation and responsive layout.

## Future Improvements

- Experiment with advanced deep learning architectures such as LSTM, GRU, and Transformer-based models.
- Improve minority-class classification performance.
- Explore advanced text representation techniques.
- Add complaint sentiment analysis.
- Implement confidence-based prediction insights.
- Deploy the application to a cloud platform.

## Author

**Sujith Karnati**

B.Tech – Computer Science and Engineering (Artificial Intelligence and Machine Learning)

**Areas of Interest:** Machine Learning | Natural Language Processing | Data Science | Artificial Intelligence

## License

This project is developed for educational and learning purposes.
