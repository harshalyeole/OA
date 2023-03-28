import pandas as pd
import time

def input_file_formatting(input_file):
    # In this function we try to format values from input file such as Month/Year value and ignore rows with empty values
    # We also utilize other helper functions to calculate the expenses for each customer to create a dataframe and add it to output file
    try:
        df = pd.read_excel(input_file)
        df = df[df['Customer Id'].notnull()]
        df['month'] = df['Date'].dt.month.astype(str) #Extract Month from Date value
        df['year'] = df['Date'].dt.year.astype(str) # Extract Year from Data value
        df['MM/YYYY'] = df['month'] + '/' + df['year']
        df3 = df['Customer Id'].unique()
        for id in df3: 
            # Iterate over all unique Customer Ids
            df2 = (df[df['Customer Id'] == id])
            output = calculate_expenses(df2, id)
            append_to_output_file(output)
    except OSError:
        print ('Input File not found')

def calculate_expenses(datafame, id): 
    # In this function we calculate the three values for each CustomerId for a particular month   
    months = datafame['MM/YYYY'].unique()
    customerid = id
    rows_list = []
    for month in months:
        # For a particular Customer ID, iterate over all the different months there was a transaction and create temporary dataframe

        df2 = (datafame[datafame['MM/YYYY'] == month])

        # Setting default value for ending balance, maximum balance, minimum balance

        ending_bal = 0
        max_bal = -100000000000 
        min_bal = 1000000000000 

        df2 = df2[df2['Amount'].notnull()] # Remove rows where Amount is NaN or empty
        
        for amount in df2['Amount']:
            ending_bal += amount

            if ending_bal > max_bal:
                max_bal = ending_bal
            
            if ending_bal < min_bal:
                min_bal = ending_bal
        
        dict = {'CustomerID' : customerid, 'MM/YYYY' : month, 'MinBalance' : min_bal, 'MaxBalance' : max_bal,'EndingBalance': ending_bal}
        rows_list.append(dict)  
    
    # Create dataframe for each customer id with all the values calculated for all the months there was a transaction
    output_dataframe = pd.DataFrame(rows_list,columns = ['CustomerID', 'MM/YYYY','MinBalance','MaxBalance','EndingBalance'], index=None)
    
    return output_dataframe
    

def create_output_file(output_file):
    # Create Output file
    try:
        df = pd.DataFrame([], columns=['CustomerID', 'MM/YYYY','MinBalance','MaxBalance','EndingBalance'])  
        with pd.ExcelWriter(output_file) as writer:
            df.to_excel(writer, index=False, sheet_name='finaloutput')  
    except Exception as e:
        print (f'ERROR : {e}')
    

def append_to_output_file(dataframe):
    # Append dataframe with values calculated to the output file
    try:
        with pd.ExcelWriter(output_file,mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:  
            dataframe.to_excel(writer, sheet_name='finaloutput', startrow=writer.sheets['finaloutput'].max_row, header=None, index=False)
    except Exception as e:
        print (f'ERROR : {e}')
    

if __name__ == "__main__":
    
    # Edit the input file and output file location

    input_file = '/Users/abhinavgupta/Downloads/test_data.xlsx'
    output_file = '/Users/abhinavgupta/Downloads/test_output.xlsx'
    create_output_file(output_file)
    input_file_formatting(input_file)
