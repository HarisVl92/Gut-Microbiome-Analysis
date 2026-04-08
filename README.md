COMPARATIVE ANALYSIS OF GUT MICROBIOME COMPOSITION IN CROHN'S DISEASE AND HEALTHY CONTROLS

Project Abstract

This project presents a comparative analysis of gut microbiome
composition in individuals with Crohn's disease and healthy controls,
using Python for data preprocessing, exploratory analysis,
visualization, and result export.

The analysis focuses on relative abundance profiles of selected
bacterial taxa and aims to identify descriptive compositional
differences associated with Crohn's disease.

Dataset Description

The dataset includes microbiome samples labeled by diagnosis:

- Crohn

- Healthy

Each sample contains:

- metadata (\`tube_id\`, \`Diagnosis\`)

- relative abundance values for selected gut bacterial taxa:

 - \`Escherichia_coli\`

 - \`Bacteroides_fragilis\`

 - \`Akkermansia_muciniphila\`

 - \`Faecalibacterium_prausnitzii\`

 - \`Bifidobacterium\`

 - \`Coprococcus\`

 - \`Faecalibacterium\`

 - \`Roseburia\`

 - \`Veillonella\`


Analysis Workflow

The script performs the following steps:

1. Loads the dataset

2. Inspects structure, missing values, and data types

3. Separates metadata from taxa columns

4. Converts taxa values to numeric format

5. Computes summary statistics and mean abundances

6. Compares mean taxon abundance between diagnosis groups

7. Estimates presence-based richness across selected taxa

8. Generates plots and exports summary tables

Main Findings

The analysis reveals clear descriptive differences between Crohn's
disease samples and healthy controls.

Key observations

I) Escherichia coli is more abundant in the Crohn's disease group.
II) Faecalibacterium prausnitzii, Faecalibacterium, and Roseburia are reduced in Crohn's disease samples.
III) Bifidobacterium and Coprococcus also show lower mean abundance in Crohn's disease.
IV) Akkermansia muciniphila remains relatively similar between groups.
V) Presence-based richness differs only modestly between the two groups.
Taken together, these findings suggest a disease-associated shift toward a more dysbiotic microbial composition in Crohn's disease.

Interpretation Note

This project analyzes relative abundance data, NOT absolute bacterial counts.
For that reason, the results should be interpreted as compositional differences between groups, rather than direct changes in total bacterial load.
The analysis is descriptive and biologically suggestive, but not causal.

Author

Haris Vlassakis
