# 🏭 OEE Calculator — Live Manufacturing Analytics Tool

> A live web application that calculates Overall Equipment Effectiveness (OEE) in real time — helping manufacturing teams instantly assess machine performance against world class benchmarks.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live_Demo-red)](YOUR-OEE-STREAMLIT-URL-HERE)
[![Plotly](https://img.shields.io/badge/Visualisation-Plotly-green)](https://plotly.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live-brightgreen)]()

---

## 📌 The Business Problem

Manufacturing teams often lack quick, accessible tools to calculate and interpret OEE — the gold standard metric for measuring production efficiency. Without it, identifying underperforming machines and shifts requires manual calculation and spreadsheet work.

**This app solves that problem** by giving any production manager or operations analyst an instant, visual OEE score — with clear guidance on whether performance is world class, average, or needs immediate attention.

---

## 🎯 Live Demo

👉 **[Click here to try the live OEE Calculator](YOUR-OEE-STREAMLIT-URL-HERE)**

Simply move the sliders and your OEE score updates instantly!

---

## 📊 What is OEE?

OEE stands for **Overall Equipment Effectiveness** — the industry standard for measuring manufacturing productivity.

| Component | Question it answers |
|-----------|-------------------|
| Availability % | Is the machine running when it should be? |
| Performance % | Is it running at the right speed? |
| Quality % | Is it producing good parts? |

**Formula:**
```
OEE = Availability % × Performance % × Quality % ÷ 100
```

**Benchmarks:**

| OEE Score | Performance Level |
|-----------|-----------------|
| 85% and above | World Class |
| 60% — 84% | Average — room for improvement |
| Below 60% | Below average — immediate action needed |

---

## ⚙️ App Features

| Feature | Description |
|---------|-------------|
| Interactive sliders | Adjust Availability, Performance and Quality in real time |
| Live OEE calculation | Score updates instantly as sliders move |
| Visual gauge chart | Colour coded gauge showing performance vs benchmark |
| Performance classification | Instant feedback — World Class, Average or Below Average |
| Individual metric display | Breakdown of all three OEE components |
| World class benchmark line | Red threshold line at 85% for instant reference |

---

## 💡 Real World Application

This tool is directly inspired by production management experience at a wire manufacturing facility where:

- Machine utilisation analysis drove a **25% increase in throughput**
- Downtime tracking enabled a **20% reduction in unplanned stoppages**
- OEE monitoring supported **$50K in annualised cost savings**

The app brings that same analytical approach into an accessible digital tool any operations team can use.

---

## 🛠️ Tools & Technologies

| Category | Tools Used |
|----------|-----------|
| Language | Python 3.11 |
| Web App | Streamlit |
| Visualisation | Plotly (gauge chart) |
| Analytics | OEE calculation, manufacturing KPIs |
| Deployment | Streamlit Cloud |
| Version Control | GitHub |

---

## 🚀 How to Run Locally

**Step 1 — Clone the repository**
```bash
git clone https://github.com/mmandloi1501/oee-calculator.git
cd oee-calculator
```

**Step 2 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 3 — Run the app**
```bash
streamlit run oee_app.py
```

---

## 📁 Project Structure

```
oee-calculator/
│
├── oee_app.py                    # Main Streamlit application
├── requirements.txt              # Python dependencies
└── README.md                     # You are here!
```

---

## 📈 What I Learned

- How to build and deploy a live data application using Python and Streamlit
- How to create interactive gauge visualisations using Plotly
- How to translate real manufacturing domain knowledge into a practical digital tool
- How to deploy a web app to Streamlit Cloud with a shareable public URL
- How OEE benchmarking drives continuous improvement decisions on the factory floor

---

## 🔗 Related Projects

| Project | Description |
|---------|-------------|
| [Smart Factory Analytics Platform]| Multi-module dashboard covering production, sales and recruitment |
| [Supply Chain Delay Predictor](https://supply-chain-delay-predictor-jsugpzbttfwgtnsynmfz7r.streamlit.app) | ML model predicting delivery delays on 100k+ orders |
| [E-Commerce Dashboard](YOUR-ECOMMERCE-URL-HERE) | Sales and RFM customer segmentation dashboard |

---

## 👤 About Me

**Mohit Mandloi** — Business Analyst & Operations Analytics Professional

MSc Business Analytics | TUS Ireland | Production Management | Supply Chain Analytics

[![GitHub](https://img.shields.io/badge/GitHub-Profile-black)](https://github.com/mmandloi1501)
[![Supply Chain](https://img.shields.io/badge/Supply_Chain-Delay_Predictor-orange)](https://supply-chain-delay-predictor-jsugpzbttfwgtnsynmfz7r.streamlit.app)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

*If you found this project useful or interesting, please consider giving it a ⭐ on GitHub!*
