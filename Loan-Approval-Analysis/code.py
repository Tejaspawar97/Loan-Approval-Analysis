# --------------
import numpy as np
import pandas as pd 
from scipy.stats import mode

bank=pd.read_csv(path)

categorical_var = bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var = bank.select_dtypes(include = 'number')
print(numerical_var)

banks = bank.drop(columns='Loan_ID')
print(banks.isnull().sum())

bank_mode = banks.mode().iloc[0]
print('bank mode is in: ',bank_mode)

banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())

avg_loan_amount = pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')


loan_approved_se =len(banks[(banks['Self_Employed']=='Yes')&(banks['Loan_Status']=='Y')])

loan_approved_nse=len(banks[(banks['Self_Employed']=='No')&(banks['Loan_Status']=='Y')])

percentage_se =(loan_approved_se* 100)/614

percentage_nse = (loan_approved_nse* 100)/614


loan_term = banks['Loan_Amount_Term'].apply(lambda x: (x/12))

big_loan_term = len(loan_term[loan_term >= 25])

loan_groupby= banks.groupby('Loan_Status')

loan_groupby= loan_groupby['ApplicantIncome','Credit_History']

mean_values = loan_groupby.mean()

print(mean_values)









