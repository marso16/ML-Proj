import numpy as np
import pandas as pd
from itertools import combinations

class Ramco:
    def __init__(self, df) -> None:
        self.df = df

    def replace_negatives_with_zeros(self):
        num = self.df._get_numeric_data()
        num[num < 0] = 0

    def drop_zero_variance_columns(self):
        zero_variance_cols=[]
        for col in self.df.columns:
            if len(self.df[col].unique()) == 1:
                zero_variance_cols.append(col)
        self.df.drop(columns = zero_variance_cols, axis = 1, inplace = True)
        return zero_variance_cols

    def drop_infinite_and_nan(self):
        self.df.replace([np.inf,-np.inf],np.nan,inplace=True)
        print(self.df.isna().any(axis = 1).sum(),"rows dropped")
        self.df.dropna(inplace = True)
        print("Shape after Removing NaN: ", self.df.shape)

    def drop_identical_columns(self):
        column_pairs = [(i,j) for i,j in combinations(self.df,2) if self.df[i].equals(self.df[j])]
        ide_cols=[]
        for col_pair in column_pairs:
            ide_cols.append(col_pair[1])
        self.df.drop(columns=ide_cols,axis=1,inplace=True)
        return column_pairs
    
    def data_cleaning(self):
        self.df.columns=self.df.columns.str.strip()
        print("Dataset Shape: ",self.df.shape)
        self.replace_negatives_with_zeros()
        
        # dropping the zero variance columns to eliminate its negative impacts on the model
        zero_variance_cols = self.drop_zero_variance_columns()
        print("Zero Variance Columns: ", zero_variance_cols, "are dropped.")
        print("Shape after removing the zero variance columns: ", self.df.shape)
        
        # cleaning all infinite and non-numeric values
        self.drop_infinite_and_nan()
        
        # removing duplicates
        self.df.drop_duplicates(inplace=True)
        print("Shape after dropping duplicates: ", self.df.shape)
        
        # eliminating columns with identical values if any
        column_pairs = self.drop_identical_columns()
        print("Columns which have identical values: ",column_pairs," dropped!")
        print("Shape after removing identical value columns: ",self.df.shape)
        return self.df
