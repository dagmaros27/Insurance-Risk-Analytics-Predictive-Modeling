## Exploratory Data Analysis (EDA) Report

A comprehensive exploratory data analysis (EDA) was conducted on the car insurance claims dataset to uncover key patterns, assess data quality, and inform subsequent modeling steps. Below is a summary of the main findings and methodologies:

### 1. Data Loading & Initial Inspection

- The dataset was loaded from `Data/data.csv` with over 1,000,000 records and 52 columns.
- Initial inspection included shape, data types, summary statistics, and missing value counts.
- Only records with valid gender values ("Male", "Female") were retained to ensure consistency in demographic analysis.

### 2. Data Cleaning & Feature Engineering

- The `TransactionMonth` column was converted to datetime format for temporal analysis.
- A new feature, `LossRatio`, was engineered as the ratio of `TotalClaims` to `TotalPremium`, providing a direct measure of insurance risk per policy.

### 3. Descriptive Statistics

- Key numerical columns analyzed: `TotalPremium`, `TotalClaims`, `CustomValueEstimate`, and `LossRatio`.
- Summary statistics (mean, median, std, min, max) were computed to understand central tendencies and dispersion.
- Missing values were quantified, highlighting columns that may require imputation or exclusion.

### 4. Grouped Analysis

- The average `LossRatio` was computed and compared across combinations of `Province`, `VehicleType`, and `Gender`.
- This revealed significant variation in risk profiles by geography, vehicle type, and demographic group.

### 5. Outlier Detection

- Boxplots were generated for `TotalPremium`, `TotalClaims`, and `CustomValueEstimate`.
- These visualizations identified the presence of outliers and skewed distributions, particularly in claim amounts and custom value estimates.

### 6. Distribution Analysis

- Distribution plots for key numerical features highlighted non-normality and the presence of heavy tails in claims and premium data.
- The `LossRatio` distribution indicated that while most policies have low loss ratios, a minority exhibit very high risk.

### 7. Correlation Analysis

- A correlation matrix was plotted for numerical features.
- Strong positive correlation was observed between `TotalPremium` and `TotalClaims`, as expected.
- `LossRatio` showed moderate correlation with both claims and premiums, validating its use as a risk metric.

### 8. Temporal Trends

- Aggregated monthly trends for `TotalClaims` and `TotalPremium` were visualized.
- Time series plots revealed seasonality and potential cyclical patterns in claims and premium collections.

### 9. Vehicle-Level Analysis

- Vehicles were ranked by average claim amounts.
- The top 10 and bottom 10 vehicle makes/models by average claims were identified, providing actionable insights for underwriting and pricing.

### 10. Categorical Visualizations

- Average loss ratios were visualized by `Province` and `Gender`, highlighting regional and demographic risk disparities.
- A heatmap of `LossRatio` by `VehicleType` and `Province` revealed interaction effects between geography and vehicle characteristics.

---

**Conclusion:**  
The EDA uncovered substantial heterogeneity in risk and claims experience across demographic, geographic, and vehicle-related dimensions. These insights directly informed feature selection and model design for subsequent predictive analytics and risk modeling.

For detailed code and visualizations, refer to the Jupyter notebooks in the `notebooks/` directory.
