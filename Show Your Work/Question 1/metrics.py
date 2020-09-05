import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


class Metrics:
    """ 
    This is a class for analysis of metrics for ecommerce. 
      
    Attributes
    ==========
    df (DataFrame): Dataframe for analysis.
    column (str): Column name for analysis.
    """
    
    def __init__(self, df, column):
        '''
        Constructor for Metrics class.

        Parameters
        ==========
        df (DataFrame): Dataframe for analysis.
        column (str): Column name for analysis.
        '''
        
        self.df = df
        self.column = column

        
    def stats(self, df=None):
        '''
        Calculates basic descriptive statistics about the column for analysis.

        Parameters
        ==========
        df (DataFrame): DataFrame for analysis.

        Returns
        =======
        stats (Series): Series of descriptive statistics.
        '''
        
        if df is None:
            count = len(self.df)
            mean = self.df[self.column].sum() / len(self.df)
            median = self.df[self.column].median()
            std = self.df[self.column].std()
            skewness = self.df[self.column].skew()
            kurtosis = self.df[self.column].kurtosis()
            data = {
                'count': count,
                'mean': mean,
                'median': median,
                'std': std,
                'skewness': skewness,
                'kurtosis': kurtosis
            }
            
            stats = pd.Series(data)
        
        else:
            count = len(df)
            mean = df[self.column].sum() / len(df)
            median = df[self.column].median()
            std = df[self.column].std()
            skewness = df[self.column].skew()
            kurtosis = df[self.column].kurtosis()
            data = {
                'count': count,
                'mean': mean,
                'median': median,
                'std': std,
                'skewness': skewness,
                'kurtosis': kurtosis
            }
            
            stats = pd.Series(data) 
        
        return stats
        
    
    def outliers(self):
        '''
        Creates a DataFrame of outliers.
        
        Returns
        =======
        outliers (DataFrame): DataFrame with all outliers.
        '''
        
        Q1 = self.df[self.column].quantile(0.25)
        Q2 = self.df[self.column].quantile(0.5)
        Q3 = self.df[self.column].quantile(0.75)
        IQR = Q3 - Q1
        lower_limit = Q1 - IQR
        upper_limit = Q3 + IQR
        outliers = self.df[(self.df[self.column] < lower_limit)\
             | (self.df[self.column] > upper_limit)]

        return outliers

    
    def num_outliers(self):
        '''
        Calculates number of outliers found.
        
        Returns
        =======
        num_outliers (int): Number of outliers.
        '''

        outliers = self.outliers()
        num_outliers = len(outliers)

        return num_outliers

       
    def percent_outliers(self):
        '''
        Calculates percentage of outliers compared to total records.
        
        Returns
        =======
        percent_outliers (float): Percentage of dataset that makes up outliers.
        '''

        num_outliers = self.num_outliers()
        percent_outliers = num_outliers / len(self.df) * 100

        return percent_outliers

    
    def remove_outliers(self):
        '''
        Removes outliers from DataFrame.

        Returns
        =======
        no_outliers_df (DataFrame): DataFrame with outliers removed.
        '''

        outliers = self.outliers()
        no_outliers_df = self.df[(~self.df[self.column].isin(outliers[self.column]))]\
            .reset_index(drop=True)
      
        return no_outliers_df

    
    def replace_outliers(self):
        '''
        Replaces outliers with median value.

        Returns
        =======
        replace_outliers_df (DataFrame): DataFrame with outliers replaced by median.
        '''

        replace_outliers_df = self.df.copy()
        outliers = self.outliers()
        Q2 = replace_outliers_df[self.column].quantile(0.5)
        replace_outliers_df[self.column] = np.where(replace_outliers_df[self.column]\
            .isin(outliers[self.column]), Q2, replace_outliers_df[self.column])
        
        return replace_outliers_df


    def aov(self, df=None):
        '''
        Calculates the average order value (AOV).
    
        Parameters
        ==========
        df (DataFrame): DataFrame for analysis.
        
        Returns
        =======
        aov (float): Average order value (AOV).
        '''
        if df is None:
            aov = self.df[self.column].sum()/len(self.df)

        else:   
            aov = df[self.column].sum()/len(df)
        
        return aov


    def mov(self, df=None):
        '''
        Calculates the median order value (MOV).
    
        Parameters
        ==========
        df (DataFrame): DataFrame for analysis.
        
        Returns
        =======
        mov (float): Median order value (MOV).
        '''
        if df is None:
            mov = self.df[self.column].median()

        else:   
            mov = df[self.column].median()
        
        return mov

    
    def plot_distribution(self, df):
        '''
        Creates distribution plots of the column analyzed.
    
        Parameters
        ==========
        df (DataFrame): DataFrame for analysis.
        
        Returns
        =======
        Histogram with kernel density and box plot.
        '''

        fig, (ax_box, ax_hist) = plt.subplots(2,
                            figsize=(10, 4),
                            gridspec_kw={'height_ratios': (.15, .85)})
        fig.suptitle('Distribution of ' + self.column.replace('_', ' ')\
            .title(), fontsize=22)
        sns.boxplot(df[self.column], ax=ax_box)
        sns.distplot(df[self.column], ax=ax_hist)
        ax_hist.set_xlabel(self.column.replace('_', ' ').title(), fontsize=14)
        ax_box.set_xlabel('')
        ax_box.set_xticks([], [])
        ax_box.set_yticks([], [])
        