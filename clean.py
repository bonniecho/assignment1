import pandas as pd
import sys

def clean_data(input1, input2, output):
    # Merge the input data files based on ID value
    df1 = pd.read_csv(input1)
    df2 = pd.read_csv(input2)
    merged_df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')

    # Remove redundant column after merging
    merged_df.drop('id', axis=1, inplace=True)

    # Drop rows with missing values
    merged_df.dropna(inplace=True)

    # Drop rows if job value contains 'insurance' or 'Insurance'
    job_filter = ~merged_df['job'].str.contains('insurance|Insurance', case=False)
    cleaned_df = merged_df[job_filter]

    # Select the desired columns
    cleaned_df = cleaned_df[['respondent_id', 'name', 'address', 'phone', 'job', 'company', 'birthdate']]

    # Reset the index
    cleaned_df.reset_index(drop=True, inplace=True)

    # Save the cleaned data to the output file
    cleaned_df.to_csv(output, index=False)

    # Print the shape of the output file
    output_df = pd.read_csv(output)
    num_rows, num_columns = output_df.shape
    print("Shape of the output file: ", num_rows, "rows", num_columns, "columns")

if __name__ == "__main__":
    # Specify the file paths
    # input1 = r"C:\Users\11951\Desktop\Assignments\assignment1\respondent_contact.csv"
    # input2 = r"C:\Users\11951\Desktop\Assignments\assignment1\respondent_other.csv"
    # output = r"C:\Users\11951\Desktop\Assignments\assignment1\respondent_cleaned.csv"
    # Call the clean_data function
    # clean_data(input1, input2, output)

    # get input1, input2, output from user using sys.argv
    input1 = sys.argv[1]
    input2 = sys.argv[2]
    output = sys.argv[3]
    clean_data(input1, input2, output)

    


