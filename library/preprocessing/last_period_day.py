import pandas as pd

def last_period_day(dataframe:pd.DataFrame, column_date:str, frequency:str) -> pd.DataFrame:
    """
    Description:
        Selects the last day of a given period

    Input:
        @param dataframe: dataframe's name
        @type: pandas.DataFrame

        @param column_date: Date column's name. Column must be in pandas datetime format.
        @type: pandas.core.series.Series

        @param frequency: allowed frequencies -> w, m, Q, Y
        @type: str

    """

    if frequency == 'w':
        dataframe['frequency'] = pd.DatetimeIndex(dataframe[column_date]).strftime('%Y-%W')
        
    elif frequency == 'm':
        dataframe['frequency'] = pd.PeriodIndex(dataframe.date, freq='m')
    
    elif frequency == 'Q':
        dataframe['frequency'] = pd.PeriodIndex(dataframe.date, freq='Q')
    
    elif frequency == 'Y':
        dataframe['frequency'] = pd.PeriodIndex(dataframe.date, freq='Y')
    
    else:
        raise ValueError(f"Invalid frequency: {frequency}")

    
    column_date_filtered = dataframe.groupby('frequency').max()[column_date]
    list_date_filtered = list(column_date_filtered)
    
    df = dataframe[dataframe[column_date].isin(list_date_filtered)]
    
    df = df.set_index(column_date)

    df = df.sort_index(ascending=True)
    
    df.drop('frequency', axis=1, inplace=True)
    
    return df