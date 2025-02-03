# Bank Data Cleaning

This project involves subsetting, cleaning, and reformatting the `bank-full.csv` dataset to create and store three new files based on the requirements detailed in the notebook.

## Steps

1. **Split and Tidy Data**:
    - The `bank_marketing.csv` dataset is split into three DataFrames: `client`, `campaign`, and `economics`.
    - Each DataFrame contains the columns outlined in the notebook and is formatted to the specified data types.

2. **Save DataFrames to CSV**:
    - The `client` DataFrame is saved as `client.csv` without an index.
    - The `campaign` DataFrame is saved as `campaign.csv` without an index.
    - The `economics` DataFrame is saved as `economics.csv` without an index.

## Files

- `client.csv`: Contains client-related data.
- `campaign.csv`: Contains campaign-related data.
- `economics.csv`: Contains economic-related data.

## Usage

To run the data cleaning process, follow the steps in the provided notebook. Ensure that the `bank_marketing.csv` file is in the same directory as the notebook.
