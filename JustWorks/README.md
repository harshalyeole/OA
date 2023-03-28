## JustWorks TakeHome Assessment

This code takes in the given input file and calculates expenses (Ending Balance, Maximum Balance, Minimum Balance ) for each CustomerID for each particular month.

## Tool Overview

The Tool consists of 4 functions, overview of these functions is as mentioned below:

1. input_file_formatting(input_file) : This function requires the location of input file as a parameter. If the file exists, we extract the value of Month/Year from Date column and add it to a new column in the dataframe. We also drop rows with None/NaN values in CustomerId column and return the dataframe. 

2. calculate_expenses(datafame, id) : This function requires formatted dataframe and the CustomerID. It then finds all the entries for that particular CustomerID, and finds all the different Month/YYYY entries for this particular customer. It then calculates the expense values for each of the months, format these values in the form of a dictionary. For all the months in which customer did any transaction, we append the dictionary for that month to a list. This list of dictionary is then used to create a dataframe and return it.

3. create_output_file(output_file) : This function is used to create an output file. It takes the parameter of desired location of the output file

4. append_to_output_file(dataframe) : This function is used to append the dataframe calculated to the already created output file.


## Instructions to Run

1. Inorder to run the code, install the required packages mentioned in requirements.txt
2. Edit input_file and output_file variable value in justworks.py code to indicate the location of the input file and the desired location of the output file.

## Tests

The given dataset was tested with the tool, and it executed successfully in 0.3 seconds. I also tested another dataset with ~2000 test cases, in this case the tool was able to create output file in under ~1 seconds. The tool also has capability to handle edge cases such as Input File location error, None or NaN values present in the dataset.


