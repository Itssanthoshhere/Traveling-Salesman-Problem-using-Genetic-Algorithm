import streamlit as st
import matplotlib.pyplot as plt
import random
import numpy as np

st.title("Traveling Salesman Problem using Genetic Algorithm")

# -------------------------------
# INPUT MODE
# -------------------------------
mode = st.radio("Select Input Mode", ["Random Cities", "Manual Input"])

if mode == "Random Cities":
    num_cities = st.slider("Number of Cities", 5, 30, 10)
    cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(num_cities)]

else:
    input_text = st.text_area(
        "Enter coordinates (x,y) one per line",
        "10,20\n30,40\n50,60\n70,80"
    )

    cities = []
    if input_text:
        try:
            for line in input_text.strip().split("\n"):
                x, y = map(int, line.split(","))
                cities.append((x, y))
        except:
            st.error("Invalid format! Please enter like: 10,20")

# -------------------------------
# GA FUNCTIONS
# -------------------------------
def distance(a, b):
    return np.linalg.norm(np.array(a) - np.array(b))

def total_distance(route, cities):
    return sum(
        distance(cities[route[i]], cities[route[(i + 1) % len(route)]])
        for i in range(len(route))
    )

def fitness(route, cities):
    return 1 / total_distance(route, cities)

def create_route(n):
    route = list(range(n))
    random.shuffle(route)
    return route

def crossover(p1, p2):
    start, end = sorted(random.sample(range(len(p1)), 2))
    child = [-1] * len(p1)
    child[start:end] = p1[start:end]

    ptr = 0
    for city in p2:
        if city not in child:
            while child[ptr] != -1:
                ptr += 1
            child[ptr] = city

    return child

def mutate(route):
    i, j = random.sample(range(len(route)), 2)
    route[i], route[j] = route[j], route[i]

def genetic_algorithm(cities):
    pop = [create_route(len(cities)) for _ in range(100)]

    for _ in range(200):
        pop = sorted(pop, key=lambda x: fitness(x, cities), reverse=True)
        selected = pop[:len(pop)//2]

        children = []
        while len(children) < 100:
            p1, p2 = random.sample(selected, 2)
            child = crossover(p1, p2)

            if random.random() < 0.1:
                mutate(child)

            children.append(child)

        pop = children

    best = min(pop, key=lambda x: total_distance(x, cities))
    return best, total_distance(best, cities)

# -------------------------------
# RUN BUTTON
# -------------------------------
if st.button("Run Optimization"):

    if len(cities) < 3:
        st.error("Need at least 3 cities!")
    else:
        # 🔹 Initial random route (baseline)
        initial_route = create_route(len(cities))
        initial_dist = total_distance(initial_route, cities)

        # 🔹 Run GA
        route, final_dist = genetic_algorithm(cities)

        # 🔹 Improvement %
        improvement = ((initial_dist - final_dist) / initial_dist) * 100

        # -------------------------------
        # RESULTS DISPLAY
        # -------------------------------
        st.subheader("Results")
        st.write(f"Initial Distance: {initial_dist:.2f}")
        st.write(f"Optimized Distance: {final_dist:.2f}")
        st.write(f"Improvement: {improvement:.2f}%")

        # -------------------------------
        # PLOT
        # -------------------------------
        x = [cities[i][0] for i in route] + [cities[route[0]][0]]
        y = [cities[i][1] for i in route] + [cities[route[0]][1]]

        fig, ax = plt.subplots()
        ax.plot(x, y, marker='o')
        ax.set_title("Optimized Route")

        st.pyplot(fig)

        # -------------------------------
        # SHOW CITIES
        # -------------------------------
        st.subheader("Cities Used")
        st.write(cities)
        
#testing: python -m streamlit run app.py 