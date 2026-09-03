# 📚 Book Recommendation System

A machine learning-based **Book Recommendation System** that recommends books to users based on their interests and book similarity.

The project uses a dataset obtained from **Kaggle** and implements recommendation techniques using preprocessed book data and similarity scores. The application provides an easy-to-use web interface where users can explore popular books and get book recommendations.

## 🚀 Live Demo

🔗 **[Book Recommendation System – Live Application](https://book-recommendation-chi-swart.vercel.app/)**

---

## ✨ Features

- 📚 Recommend books based on similarity
- 🔍 Search and explore books
- ⭐ Display popular books
- 📖 Get personalized book recommendations
- 🧠 Machine learning-based recommendation approach
- ⚡ Fast recommendations using precomputed similarity scores
- 🌐 Web-based user interface
- 📱 Responsive and easy-to-use design
- ☁️ Deployed online for easy access

---

## 🧠 Recommendation Approach

The system uses a **content-based recommendation approach**.

Book information is processed and transformed into a format that can be used to calculate similarity between books. Precomputed similarity scores are stored in `.pkl` files, allowing the application to quickly find and recommend books without recalculating similarities every time.

### Workflow

```text
Book Dataset
     ↓
Data Preprocessing
     ↓
Feature Extraction
     ↓
Similarity Calculation
     ↓
Similarity Scores
     ↓
Recommendation Model
     ↓
Web Application
     ↓
Book Recommendations
```

---

## 🛠️ Technologies Used

- **Python** – Core programming language
- **Flask** – Web application framework
- **HTML5** – Frontend structure
- **CSS3** – Styling and responsive design
- **Machine Learning** – Recommendation system
- **Pandas** – Data processing
- **NumPy** – Numerical operations
- **Pickle** – Saving and loading trained/preprocessed data
- **Kaggle Dataset** – Source of book data
- **Vercel** – Deployment

---

## 📊 Dataset

The book dataset used in this project was obtained from **Kaggle**.

The dataset was processed and used to build the recommendation system and generate the required similarity scores.

> Dataset Source: **Kaggle**

---

## 📁 Project Structure

```text
Book-Recommendation-System/
│
├── templates/
│   └── HTML template files
│
├── .gitignore
├── Dockerfile
├── Procfile
├── README.md
├── app.py
├── books.pkl
├── popular.pkl
├── pt.pkl
├── similarity_scores.pkl
└── requirements.txt
```

### 📌 Important Files

| File | Description |
|---|---|
| `app.py` | Main Flask application |
| `templates/` | Contains the frontend HTML templates |
| `books.pkl` | Stored book data |
| `popular.pkl` | Popular books data |
| `pt.pkl` | Processed data used by the recommendation system |
| `similarity_scores.pkl` | Precomputed similarity scores |
| `requirements.txt` | Python dependencies |
| `Dockerfile` | Configuration for containerized deployment |
| `Procfile` | Deployment configuration |
| `.gitignore` | Specifies files ignored by Git |

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
```

### 2. Navigate to the Project Directory

```bash
cd Book-Recommendation-System
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

### 5. Run the Application

```bash
python app.py
```

The application will start on the local Flask development server.

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

---

## 🔄 How the System Works

The recommendation system follows these general steps:

1. 📊 Book data is collected from Kaggle.
2. 🧹 The dataset is processed and prepared.
3. 🔢 Relevant book information is transformed into usable features.
4. 🧠 Similarity between books is calculated.
5. 💾 Processed data and similarity scores are stored using Pickle.
6. 🔍 When a user selects a book, the system searches for similar books.
7. 📚 The most relevant books are returned as recommendations.
8. 🌐 Recommendations are displayed through the Flask web application.

---

## 🌐 Live Application

Try the Book Recommendation System online:

🔗 **https://book-recommendation-chi-swart.vercel.app/**

---

## 🐳 Docker Support

The project also includes a `Dockerfile`, allowing the application to be containerized.

Build the Docker image:

```bash
docker build -t book-recommendation-system .
```

Run the container:

```bash
docker run -p 5000:5000 book-recommendation-system
```

Then open:

```text
http://localhost:5000
```

---

## 📌 Future Improvements

Some possible improvements for the project include:

- 👤 User-based personalized recommendations
- ⭐ User rating and review system
- 🔐 User authentication
- 📚 Larger and more diverse datasets
- 🎯 Improved recommendation accuracy
- 🔎 Advanced book search and filtering
- 📖 Book details and descriptions
- ❤️ Save favorite books
- 📊 Recommendation analytics

---

## 👨‍💻 Author

**Md Irshad Alam**

---

## ⭐ Support

If you found this project useful or interesting, consider giving the repository a ⭐ **star** on GitHub.

---

### 🔗 Project Link

**Live Demo:**  
https://book-recommendation-chi-swart.vercel.app/
