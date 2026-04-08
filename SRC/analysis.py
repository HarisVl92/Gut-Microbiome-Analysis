import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

PROJECT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = PROJECT_DIR / "Data" / "joined_MI_ready.csv"
PLOTS_DIR = PROJECT_DIR / "Plots"
OUTPUTS_DIR = PROJECT_DIR / "Outputs"

PLOTS_DIR.mkdir(exist_ok=True)
OUTPUTS_DIR.mkdir(exist_ok=True)

# Load Dataset

Data = pd.read_csv(DATA_PATH)

#First Inspection

print ("First 10 rows:")
print (Data.head())

print ("\nShape:")
print (Data.shape)

print ("\nColumns:")
print (Data.columns.tolist())

# Inspection for missing values and data types

print ("\nMissing Values Per Column:")
print (Data.isnull().sum())

print ("\nData Types:")
print (Data.dtypes)

# Data Type Separation into Corresponding Columns

metadata_cols = ["tube_id", "Diagnosis"]

taxa_cols = []
for col in Data.columns:
    if col not in metadata_cols:
        taxa_cols.append(col)
    

print("\nMetadata Columns:")
print(metadata_cols)

print("\nTaxa Columns:")
print(taxa_cols)

# Taxa Column Numeric Conversion

Data[taxa_cols] = Data[taxa_cols].apply(pd.to_numeric, errors = "coerce")

print ("\nData After Conversion:")
print (Data[taxa_cols].dtypes)

print ("\nMissing Values After Conversion:")
print (Data[taxa_cols].isnull().sum())

# Relative Abundance Check

print ("\nSummary Statistics for taxa:")
print (Data[taxa_cols].describe())

mean_abundance = Data[taxa_cols].mean().sort_values(ascending = False)
print ("\nMean Abundance of taxa:")
print (mean_abundance)

# Mean Relative ABundance Per Taxon Plot
plt.figure(figsize=(10, 6))
mean_abundance.plot(kind="bar")
plt.title("Mean Relative Abundance of Selected Gut Bacteria")
plt.xlabel("Taxa")
plt.ylabel("Mean Relative Abundance")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "mean_abundance_taxa.png", dpi=300)
plt.show()

# Comparison between healthy individuals and individuals with Crohn's disease

group_means = Data.groupby("Diagnosis")[taxa_cols].mean()
print ("\nMean Abundance Per Group:")
print (group_means)

# Group Comparison Plot

group_means.T.plot(kind="bar", figsize=(12,7))
plt.title("Mean Relative Abundance of Selected Gut Bacteria by Diagnosis Group")
plt.xlabel("Taxa")
plt.ylabel("Mean Relative Abundance")
plt.xticks(rotation=45, ha="right")
plt.legend(title="Diagnosis")
plt.tight_layout()
plt.savefig(PLOTS_DIR / "group_comparison_taxa.png", dpi=300)
plt.show()

# Presence-based richness among selected taxa

Data["Selected_Taxa_Richness"] = (Data[taxa_cols] > 0).sum(axis=1)
print ("\nRichness per sample:")
print (Data[["tube_id", "Diagnosis", "Selected_Taxa_Richness"]].head())

# Mean Richness by Group

richness_by_group = Data.groupby("Diagnosis")["Selected_Taxa_Richness"].mean()
print ("\nMean Selected-Taxa Richness by Group:")
print (richness_by_group)

# Mean Selected Taxa Richness by Group Plot

plt.figure(figsize=(7,5))
richness_by_group.plot(kind="bar")
plt.title("Mean Selected Taxa Richness by Diagnosis Group")
plt.xlabel("Diagnosis")
plt.ylabel("Mean Number of Detected Selected Taxa")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(PLOTS_DIR / "richness_by_Diagnosis_group.png", dpi=300)
plt.show()

# Absolute Difference Between Groups

if "Crohn" in group_means.index and "Healthy" in group_means.index:
    diff = group_means.loc["Crohn"] - group_means.loc["Healthy"]
    diff_absolute = diff.abs().sort_values(ascending=False)

    print("\nAbsolute Difference Between Groups:")
    print(diff_absolute)

# Data Save

mean_abundance.to_csv(OUTPUTS_DIR / "mean_abundances.csv",header=["Mean_Relative_Abundance"])

Data[["tube_id", "Diagnosis", "Selected_Taxa_Richness"]].to_csv(OUTPUTS_DIR / "sample_richness.csv",index=False)




