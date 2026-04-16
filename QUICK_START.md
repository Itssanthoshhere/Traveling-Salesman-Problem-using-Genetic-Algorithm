# 🚀 TSP Optimizer - Quick Start Guide

## Installation

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the App
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 📋 What's New in v2.0

### ✨ Major UI Upgrades
- **Modern Dashboard Layout** with professional color scheme (purple gradients)
- **Side-by-side Route Comparison** (Initial vs Optimized)
- **Interactive Folium Maps** showing city locations and routes
- **Real-time Progress Tracking** with generation counter
- **Convergence Analysis Graph** showing improvement over generations
- **4 Organized Tabs**: Visualization, Convergence, Map, Details

### 📊 Enhanced Visualizations
- Better matplotlib styling with improved colors and readability
- Start/End city highlighted in green
- City nodes with ID labels
- Grid background for reference
- Gradient fills and annotations

### 🎯 New Features
- **Metrics Dashboard**: 4-column card layout showing key stats
- **Detailed Statistics**: Population size, generations, mutation rate
- **Download Options**:
  - 📸 PNG image of route
  - 📄 JSON export with full results
  - 📊 CSV convergence data
- **Interactive Map**: Pan, zoom, and explore city routes
- **Algorithm Statistics**: Real-time generation progress

### 🛠️ Code Quality
- Modular, well-organized functions
- Session state management to prevent data loss
- Input validation and error handling
- Comprehensive docstrings

---

## 🎮 How to Use

### 1. Configure Your Problem
- **Sidebar > Input Mode**: Choose "Random Cities" or "Manual Input"
  - Random: Use slider to select 5-30 cities
  - Manual: Paste coordinates as `x,y` format

### 2. Set GA Parameters
- **Population Size**: 20-200 (default 100)
- **Generations**: 50-500 (default 200)
- **Mutation Rate**: 0.01-0.3 (default 0.1)

### 3. Run Optimization
- Click **"🚀 Run Optimization"** button
- Watch the progress bar as generations complete
- Results appear automatically in tabs below

### 4. Explore Results
- **📊 Visualization Tab**: Compare routes side-by-side
- **📈 Convergence Tab**: See improvement over generations
- **🗺️ Map Tab**: Interactive map of cities and routes
- **📋 Details Tab**: Route orders and statistics

### 5. Download Results
- Choose from PNG, JSON, or CSV format
- Automatically named with timestamp

---

## 📁 File Structure

```
.
├── app.py                          # Main Streamlit app (completely redesigned)
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── render.yaml                     # Render deployment config
├── README.md                       # Project overview
└── REDESIGN_DOCUMENTATION.md      # Detailed improvement docs
```

---

## 🎨 Color Scheme

- **Primary Purple**: #667eea
- **Secondary Violet**: #764ba2
- **Success Green**: #00d084
- **Background**: #ffffff, #f8f9fa
- **Text**: #333333, #888888

Used in:
- Header text (gradient)
- Route lines and markers
- UI components and cards
- Success indicators

---

## ⚙️ Advanced Usage

### Custom GA Parameters for Different Problems
```
Small problem (5-10 cities):
- Population: 50
- Generations: 100
- Mutation: 0.15

Medium problem (10-20 cities):
- Population: 100
- Generations: 200
- Mutation: 0.1

Large problem (20-30 cities):
- Population: 150-200
- Generations: 300-500
- Mutation: 0.05-0.08
```

### JSON Export Format
```json
{
  "timestamp": "2024-04-16T...",
  "cities_count": 10,
  "cities": [[10, 20], [30, 40], ...],
  "initial_distance": 250.5,
  "optimized_distance": 150.3,
  "improvement_percentage": 40.0,
  "initial_route": [0, 1, 2, ...],
  "optimized_route": [0, 5, 2, ...],
  "ga_generations": 200,
  "population_size": 100,
  "mutation_rate": 0.1
}
```

---

## 🚀 Deployment

### Streamlit Cloud
1. Push code to GitHub
2. Go to `share.streamlit.io`
3. Deploy from repository
4. Add `.streamlit/config.toml` for theme customization

### Render
```bash
# render.yaml is already configured
# Just connect your GitHub repo to Render
```

### Local Deployment
```bash
# Development mode with debugging
streamlit run app.py --logger.level=debug

# Production mode
streamlit run app.py --client.toolbarMode="viewer"
```

---

## 🐛 Troubleshooting

### Issue: "No module named 'folium'"
**Solution**: 
```bash
pip install folium streamlit-folium
```

### Issue: Slow on large cities (30+)
**Solution**:
- Reduce population size to 50-75
- Reduce generations to 100-150
- Increase mutation rate to 0.15-0.2

### Issue: Map not displaying
**Solution**:
- Ensure `streamlit-folium` is installed
- Clear Streamlit cache: `streamlit cache clear`
- Check internet connection (map uses OpenStreetMap)

### Issue: Results disappear after refresh
**Solution**:
- App uses session state (won't persist on page reload)
- Re-run optimization to regenerate results
- Use JSON download to save results between sessions

---

## 📈 Performance Notes

- **5-10 cities**: ~2-5 seconds
- **10-20 cities**: ~5-15 seconds
- **20-30 cities**: ~15-30 seconds

Timing depends on:
- Population size
- Number of generations
- Your computer's processing power

---

## 🎓 About Genetic Algorithms

### How It Works
1. **Initialization**: Create random routes (population)
2. **Evaluation**: Calculate fitness (inverse of distance)
3. **Selection**: Choose best routes for breeding
4. **Crossover**: Combine two routes to create offspring (Order Crossover)
5. **Mutation**: Randomly swap cities (Swap Mutation)
6. **Repeat**: For N generations until convergence

### Why It's Good for TSP
- Finds **near-optimal solutions** quickly
- Better than random or greedy approaches
- Scalable to many cities
- Can escape local optima

---

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Folium Documentation](https://python-visualization.github.io/folium/)
- [Genetic Algorithms (Wikipedia)](https://en.wikipedia.org/wiki/Genetic_algorithm)
- [TSP Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

---

## 📝 Customization Ideas

### Add Custom Theme
Create `.streamlit/config.toml`:
```toml
[theme]
primaryColor = "#667eea"
backgroundColor = "#ffffff"
secondaryBackgroundColor = "#f8f9fa"
textColor = "#333333"
font = "sans serif"
```

### Modify Colors in Code
Search for `#667eea` and `#764ba2` in `app.py` to change the gradient colors throughout.

### Add Dark Mode
Wrap styling in:
```python
if st.get_option("theme.base") == "dark":
    # Apply dark theme CSS
else:
    # Apply light theme CSS
```

---

## ❓ FAQ

**Q: Can I use real-world city coordinates?**  
A: Yes! Use "Manual Input" and paste coordinates. The map will show them using OpenStreetMap.

**Q: How much improvement can I expect?**  
A: Typically 40-50% over random routes. More generations = better results (with diminishing returns).

**Q: Can I run it on my phone?**  
A: Yes, via Streamlit Cloud or Render deployment. The UI is responsive.

**Q: Is it always finding the optimal route?**  
A: No, TSP is NP-hard. GA finds near-optimal solutions fast, not necessarily the absolute best.

**Q: How can I make it faster for 30+ cities?**  
A: Reduce generations, use smaller population, increase mutation rate, or implement advanced crossover (EAX).

---

**Last Updated**: April 2026  
**Version**: 2.0 (Redesigned)  
**Status**: ✅ Production Ready
