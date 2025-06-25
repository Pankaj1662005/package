# TOPSIS Toolkit 📊

A simple Python package and command-line tool to perform **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** — a popular multi-criteria decision-making method.

---

## 🔧 Features

- Accepts input data via CSV files
- Customizable **weights** and **impacts** for each criterion
- Outputs TOPSIS scores and **ranks** for alternatives
- Can be used both as a **CLI tool** and as a **Python module**
- Lightweight and easy to integrate

---

## 🚀 Installation

You can install the package directly from GitHub using pip:

```bash
pip install git+https://github.com/Pankaj1662005/package.git
````

---

## 📦 Usage

### ✅ 1. As a Command-Line Tool

```bash
topsis-runner <input_file.csv> <weights> <impacts> <output_file.csv>
```

**Arguments:**

* `<input_file.csv>`: Path to the input CSV file (must include a header row)
* `<weights>`: Comma-separated weights for each criterion (e.g., `1,1,1,1,1`)
* `<impacts>`: Comma-separated impacts (`+` for benefit, `-` for cost) (e.g., `+,+,-,-,+`)
* `<output_file.csv>`: Output file path to save results

**Example:**

```bash
topsis-runner funds.csv 1,1,1,1,1 +,+,-,-,+ output.csv
```

---

### ✅ 2. As a Python Module

```python
import pandas as pd
from topsis_toolkit.topsis import topsis

# Load data
df = pd.DataFrame({
    'Fund Name': ['M1','M2','M3','M4','M5','M6','M7','M8'],
    'P1': [0.84,0.91,0.79,0.78,0.94,0.88,0.66,0.93],
    'P2': [0.71,0.83,0.62,0.61,0.88,0.77,0.44,0.86],
    'P3': [6.7,7.0,4.8,6.4,3.6,6.5,5.3,3.4],
    'P4': [42.1,31.7,46.7,42.4,62.2,51.5,48.9,37.0],
    'P5': [12.59,10.11,13.23,12.55,16.91,14.91,13.83,10.55]
})

# Specify weights & impacts
weights = [1, 1, 1, 1, 1]
impacts = [1, 1, -1, -1, 1]  # '+' = benefit, '-' = cost

# Calculate TOPSIS scores & ranks
scores = topsis(df.iloc[:, 1:].values, weights, impacts)
df['Topsis Score'] = scores
df['Rank'] = scores.argsort()[::-1] + 1

# Display or save
print(df)
df.to_csv('topsis_results.csv', index=False)
```

---


## 💡 Output

The tool will generate a file like:

```csv
  Fund Name    P1    P2   P3    P4     P5  Topsis Score  Rank
0        M1  0.84  0.71  6.7  42.1  12.59      0.578909     8
1        M2  0.91  0.83  7.0  31.7  10.11      0.580864     5
2        M3  0.79  0.62  4.8  46.7  13.23      0.581251     3
3        M4  0.78  0.61  6.4  42.4  12.55      0.576470     2
4        M5  0.94  0.88  3.6  62.2  16.91      0.587669     6
5        M6  0.88  0.77  6.5  51.5  14.91      0.580316     1
6        M7  0.66  0.44  5.3  48.9  13.83      0.571918     4
7        M8  0.93  0.86  3.4  37.0  10.55      0.595536     7
```

---

## 📁 Project Structure

```
topsis_toolkit/
├── __main__.py       # CLI entry point
├── topsis.py         # TOPSIS core logic
setup.py              # Installation & packaging
README.md             # This file
```

---

## 🛠️ To-Do

* [ ] Add support for Excel input/output
* [ ] Add unit tests with pytest
* [ ] Add visualizations of scores
* [ ] Publish on PyPI

---

## 👨‍💻 Author

**Pankaj**
Student at Thapar Institute of Engineering and Technology
Elective: Data Science | Language: C++ & Python
🔗 [GitHub Profile](https://github.com/Pankaj1662005)

---

## 📄 License

MIT License

```
