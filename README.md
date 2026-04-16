
# 🚀 Traveling Salesman Problem using Genetic Algorithm

## 📌 Overview
This project solves the **Traveling Salesman Problem (TSP)** using a **Genetic Algorithm (GA)**.  
The goal is to find the shortest possible route that visits all cities exactly once and returns to the starting point.

An interactive web application is built using **Streamlit**, allowing users to visualize optimized routes.

---

## 🧠 Key Concepts
- Genetic Algorithm (Selection, Crossover, Mutation)
- NP-hard Optimization Problem
- Euclidean Distance Calculation
- Route Optimization & Visualization

---

## ⚙️ Features
- 📍 Random city generation (5–30 cities)
- ✍️ Manual coordinate input
- 📊 Real-time route optimization
- 📈 Distance comparison (initial vs optimized)
- 🖼️ Graphical visualization of route

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **NumPy**
- **Matplotlib**

---

## 📂 Project Structure
```

.
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

````

---

## 🚀 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Itssanthoshhere/Traveling-Salesman-Problem-using-Genetic-Algorithm.git
cd Traveling-Salesman-Problem-using-Genetic-Algorithm
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This project can be deployed using:

* Streamlit Cloud
* Render

---

## 📊 How It Works

1. Generate an initial population of random routes
2. Evaluate fitness (based on total distance)
3. Select best routes
4. Apply crossover and mutation
5. Repeat for multiple generations
6. Output the best optimized route

---

## 📈 Results

* Achieves **~40–50% improvement** over random routes
* Efficient for up to **30 cities**
* Provides near-optimal solutions quickly

---

## 🔮 Future Improvements

* Implement advanced crossover (PMX, EAX)
* Add 2-opt / 3-opt optimization
* Use real-world datasets (maps, GPS)
* Improve scalability with parallel processing

---

## 📚 References

* Holland, J.H. (1975)
* Goldberg, D.E. (1989)
* Lin & Kernighan (1973)

---

## 👨‍💻 Contributors

* V S Santhosh
* Riti Dubey
* Tanistha Keshri
* Anarghya Singh

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!

---