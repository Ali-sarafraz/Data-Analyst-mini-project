# 🏨 Hotel Bookings — Exploratory Data Analysis

A mini data analysis project exploring hotel booking patterns, cancellation trends, guest origins, and pricing behaviour using Python.

---

## 📌 Project Overview

> *When is the best time of year to book a hotel? What length of stay gets you the best daily rate? Which type of hotel sees the most cancellations?*

This project digs into a real-world hotel bookings dataset to answer these questions through exploratory data analysis (EDA) and visualization. The dataset covers two hotel types — **City Hotel** and **Resort Hotel** — with records spanning multiple years.

---

## 📁 Repository Structure

```
Data-Analyst-mini-project/
│
├── Analysis.ipynb          # Main EDA notebook (9 questions + conclusions)
├── Geo_map.py              # Interactive geographic map of guest origins
├── Hotel_Bookings.csv      # Dataset (119,390 booking records)
└── README.md
```

---

## ❓ Questions Explored

| # | Question |
|---|----------|
| 1 | Which hotel type receives the most bookings? |
| 2 | What percentage of bookings were cancelled overall? |
| 3 | How do cancellation rates differ between hotel types? |
| 4 | Which hotel type was booked most/least in each year? |
| 5 | How does the Average Daily Rate (ADR) change across months? |
| 6 | What are the ADR statistics (mean, std, median, min, max) per hotel? |
| 7 | Which countries do most guests come from? |
| 8 | Which booking channel (market segment) is most popular? |
| 9 | Which meal plan do guests prefer? |

---

## 🔍 Key Findings

- **City Hotels** account for ~66.5% of all bookings but have a notably higher cancellation rate (**41.7%** vs **27.8%** for Resort Hotels).
- **Online Travel Agents (OTAs)** are the dominant booking channel, responsible for ~47% of all reservations.
- Most guests originate from **Portugal**, suggesting the hotels are located there.
- **ADR peaks in July–August** for both hotel types; Resort Hotels see the sharpest seasonal spike.
- **Bed & Breakfast (BB)** is the preferred meal plan across both hotel types.

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Custom visualizations |
| Seaborn | Statistical plots |
| Plotly / Folium | Interactive geo map (`Geo_map.py`) |

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/Ali-sarafraz/Data-Analyst-mini-project.git
cd Data-Analyst-mini-project
```

**2. Install dependencies**
```bash
pip install numpy pandas matplotlib seaborn plotly
```

**3. Run the notebook**
```bash
jupyter notebook Analysis.ipynb
```

**4. (Optional) View the interactive map**
```bash
python Geo_map.py
```

> ⚠️ Make sure `Hotel_Bookings.csv` is in the same directory as the notebook before running.

---

## 📊 Dataset

The dataset is a cleaned version of the [Hotel Booking Demand dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand) originally published by Antonio, Almeida & Nunes (2019).

| Property | Value |
|----------|-------|
| Rows | 119,390 |
| Columns | 32 |
| Hotel types | City Hotel, Resort Hotel |
| Years covered | 2015 – 2017 |

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).