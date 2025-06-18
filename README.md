# End-to-End Insurance Risk Analytics & Predictive Modeling for AlphaCare Insurance Solutions

## Project Overview

This project delivers a comprehensive risk analytics and predictive modeling solution for **AlphaCare Insurance Solutions (ACIS)**, focusing on their car insurance portfolio in South Africa. By analyzing historical claim data, we've developed actionable insights and a robust machine learning model to optimize marketing strategies and identify "low-risk" client segments. Our aim is to enable ACIS to reduce premiums for these desirable segments, thereby attracting new clients and enhancing market share.

---

## Business Objectives Achieved

This initiative successfully addresses ACIS's commitment to cutting-edge risk and predictive analytics by:

- **Optimizing Marketing Strategy:** Insights derived from extensive data analysis provide a clear understanding of risk profiles across various demographics and locations, enabling targeted and efficient marketing campaigns.
- **Identifying "Low-Risk" Targets:** We've successfully pinpointed client segments exhibiting significantly lower claim risks. This allows ACIS to offer competitive, reduced premiums, creating a compelling value proposition for new customers.

Our findings and model empower ACIS to tailor their insurance products more effectively, meeting evolving consumer needs and preferences while maintaining profitability.

---

## Key Achievements & Methodologies

This project involved a full end-to-end analytics pipeline, from data engineering to advanced predictive modeling.

### Insurance Domain Understanding

A foundational understanding of **insurance terminology** and how the insurance business operates was crucial. This informed every stage of the analysis, from feature engineering to model interpretation.

### A/B Hypothesis Testing

Rigorous **A/B hypothesis testing** was conducted to validate key assumptions about risk distribution. We specifically investigated and made conclusions on the following hypotheses:

- **Risk Differences Across Provinces:** Analyzed claim data to determine if statistically significant differences in risk exist between various provinces.
- **Risk Differences Between Zip Codes:** Explored variations in risk profiles at a granular level, identifying high and low-risk **zip codes**.
- **Margin (Profit) Differences Between Zip Codes:** Assessed the profitability landscape across different geographical areas to inform premium adjustments.
- **Risk Differences Between Genders:** Examined whether there are statistically significant disparities in risk between women and men.

These tests provide a data-driven basis for differential pricing and targeted marketing efforts.

### Machine Learning & Statistical Modeling

Our core deliverables include:

- **Total Claims Prediction (Linear Regression):** For each unique zip code, a **linear regression model** was fitted to predict total claims. This provides localized insights into expected claim costs.
- **Optimal Premium Prediction (Machine Learning Model):** A sophisticated **machine learning model** was developed to predict optimal premium values. This model incorporates a rich set of features, including:
  - **Car Features:** Details about the insured vehicle (e.g., make, model, registration year, custom value).
  - **Owner Features:** Information about the policyholder (e.g., gender, marital status, citizenship).
  - **Location Features:** Data related to the owner's geographical location (e.g., province, postal code, Cresta zones).
  - **Other Relevant Features:** Additional variables identified during exploratory data analysis that significantly influence risk and premium calculation.

The model's **explaining power** of important features has been thoroughly analyzed and reported, providing transparency and interpretability to the premium prediction process. This ensures that premium adjustments are justifiable and data-backed.

---

## Technical Stack & Practices

- **Data Engineering:** Processes for data cleaning, transformation, and feature engineering from raw historical claim data (Feb 2014 - Aug 2015).
- **Programming Language:** Python, with a strong emphasis on **modular and object-oriented code** for maintainability and scalability.
- **Statistical Analysis:** Leveraging libraries for hypothesis testing and statistical modeling.
- **Machine Learning:** Utilizing various machine learning frameworks for model development, training, and evaluation.
- **Version Control:** Comprehensive use of **Git and GitHub** for source code management, ensuring traceability and collaborative development. This includes a robust **CI/CD pipeline with GitHub Actions** for automated testing and deployment validation.
- **Data Versioning:** Methodologies implemented to manage and document different versions of datasets and analysis results, ensuring reproducibility.

---

## Impact & Recommendations

This project provides ACIS with a powerful analytical framework to:

- **Tailor Product Offerings:** Design insurance products that precisely match the risk profiles and preferences of various customer segments.
- **Optimize Pricing:** Implement data-driven premium adjustments that attract low-risk clients without compromising overall profitability.
- **Enhance Marketing Efficiency:** Direct marketing efforts towards the most promising client segments, maximizing return on investment.

Our recommendations will detail specific plan features that can be modified or enhanced based on the insights gained from the A/B tests and predictive models. This strategic approach will enable ACIS to grow its client base and solidify its position as an innovative leader in the South African insurance market.

## Installation and Setup

To set up the project environment, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/dagmaros27/Insurance-Risk-Analytics-Predictive-Modeling
   cd Insurance-Risk-Analytics-Predictive-Modeling
   ```
2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies:**

   ```bash
    pip install -r requirements.txt
   ```

4. **Add Data to the Data Folder:**

   - Download the dataset from the provided source.
   - Place the dataset files in the `data` directory of the project.

5. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add the necessary environment variables. For example:

Here’s a section you can copy into your `README.md` under a new heading called **🔁 Reproducibility with DVC**:

---

6. Reproducibility with DVC

To ensure our insurance risk analytics pipeline is fully reproducible and auditable, we use [Data Version Control (DVC)](https://dvc.org/) to track dataset versions.

### 🔧 Prerequisites

- Python ≥ 3.8
- Git
- DVC: Install using

```bash
pip install dvc
```

---

### 📂 Directory Structure

```
project-root/
├── data/
│   └── insurance_data.csv       ← Tracked via DVC
├── .dvc/
├── .dvcignore
├── data/insurance_data.csv.dvc  ← Metadata for dataset
├── scripts/
├── insurance_eda_analysis.ipynb
├── requirements.txt
├── README.md
```

---

- **Pull the Dataset via DVC**

```bash
dvc pull
```

This command will fetch the latest version of `data/insurance_data.csv` from the configured remote DVC storage.

---

## 📊 New Analyses: Hypothesis Testing & Statistical Modeling

### Hypothesis Testing

- Conducted rigorous A/B hypothesis tests using [notebooks/hypotesis_testing.ipynb](notebooks/hypotesis_testing.ipynb).
- Tested for statistically significant differences in risk and margin across provinces, zip codes, and genders.
- Key finding: Policies in zip code 1619 have a significantly lower average margin than those in 1625 (p-value = 0.022), indicating regional profitability differences.
- Visualized margin distributions by zip code to support business insights.

### Statistical Modeling

- Developed and evaluated predictive models in [notebooks/statistical_modeling.ipynb](notebooks/statistical_modeling.ipynb).
- Used a Random Forest Regressor to predict total claims, with performance metrics such as RMSE and R² reported.
- Interpreted model results using SHAP values to identify the most influential features in claim prediction.
- Ensured reproducibility and modularity by leveraging scripts in the [`scripts/`](scripts/) directory.

For detailed code, results, and visualizations, see the respective Jupyter notebooks in the [`notebooks/`](notebooks/) folder.
