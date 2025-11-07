# (1) Data Science Project on President Heights
Link reference: https://amanxai.com/2020/05/08/data-science-project-on-president-heights/
____________________________________________________________________________________________________________________________________________________________
In this repository we will work with data to analyse the President Heights around the world using some basics concepts.
The dataset is available in the file president_heights.csv and its values:
* **order:** index from 1 to n.
* **name:** name of each president.
* **height (cm):** height of each president.
  
### Extraction and pre-process of information
We'll use the Pandas package to read the file, extract and save as an array this information. The only feature we need to use for prediction is **the heights**.

### Summary statistics
We calculate the summary statistics to **better understand the data before applying Machine Learning models**. This helps us see the distribution, detect outliers, and identify the main characteristics of the presidents’ heights.

Statistics values we will need to evaluate are:
1. **Mean:** gives a general idea of the typical height in the dataset.
2. **Standard deviation:** tells us if the heights are similar or very spread out.
3. **Maximum:** helps identify the upper extreme of the data.
4. **Minimum:** helps identify the lower extreme of the data.
5. **Percentiles:** how how data points are spread across the range (e.g., the 25th, 50th, and 75th percentiles show where most heights fall).
6. **Median:** useful when the data has outliers, since it’s not affected by extremely high or low values.


### Results and interpretations

