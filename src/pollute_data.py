# This module is used to pollute the data by adding noise to the data
import pandas as pd
import numpy as np
import random
import string

def duplicate_primary_key(df:pd.DataFrame, primary_key_id:str, duplicate_percentage:float = 0.5) -> pd.DataFrame:
    """
    This function duplicates the primary key ids in the data frame. 

    Args:
        df (pd.DataFrame): Dataframe to be polluted
        primary_key_id (str): Primary key id to be duplicated
        duplicate_percentage (float): Percentage of primary key ids to be duplicated

    Returns:
        pd.DataFrame: Polluted dataframe
    """
    # check if duplicate percentage is valid
    if duplicate_percentage < 0 or duplicate_percentage > 1:
        raise ValueError("Duplicate percentage should be between 0 and 1")
    
    
    # get the number of primary keys to be duplicated
    num_primary_keys = int(len(df) * duplicate_percentage)

    duplicate_primary_keys = df.sample(num_primary_keys)[primary_key_id].values

    # add the duplicate primary keys to the dataframe
    duplicate_df = df[df[primary_key_id].isin(duplicate_primary_keys)]

    # use concat to add the duplicate rows to the dataframe
    df = pd.concat([df, duplicate_df])

    return df

def add_nulls(df:pd.DataFrame, columns:list, null_percentage:float = 0.5) -> pd.DataFrame:
    """
    This function adds null values to the columns in the dataframe

    Args:
        df (pd.DataFrame): Dataframe to be polluted
        columns (list): List of columns to be polluted
        null_percentage (float): Percentage of null values to be added

    Returns:
        pd.DataFrame: Polluted dataframe
    """
    # check if null percentage is valid
    if null_percentage < 0 or null_percentage > 1:
        raise ValueError("Null percentage should be between 0 and 1")

    # get the number of null values to be added
    num_nulls = int(len(df) * null_percentage)
    if not isinstance(columns, list):
        columns = [columns]
    for column in columns:
        # get a random sample of rows to be nullified
        null_rows = df.sample(num_nulls)

        # use np.where to add null values to the dataframe
        df[column] = np.where(df['id'].isin(null_rows['id']), np.nan, df[column])

    return df

def add_non_numerical_value_to_numerical_column(df:pd.DataFrame, 
                                                columns:list,
                                                  non_numerical_percentage:float = 0.5) -> pd.DataFrame:
    """
    This function adds non numerical values to the numerical columns in the dataframe

    Args:
        df (pd.DataFrame): Dataframe to be polluted
        columns (list): List of columns to be polluted
        non_numerical_value (str): Non numerical value to be added
        non_numerical_percentage (float): Percentage of non numerical values to be added

    Returns:
        pd.DataFrame: Polluted dataframe
    """
    # check if non numerical percentage is valid
    if non_numerical_percentage < 0 or non_numerical_percentage > 1:
        raise ValueError("Non numerical percentage should be between 0 and 1")

    # get the number of non numerical values to be added
    num_non_numerical_values = int(len(df) * non_numerical_percentage)
    if not isinstance(columns, list):
        columns = [columns]
    for column in columns:
        # get a random sample of rows to be polluted
        non_numerical_rows = df.sample(num_non_numerical_values)
        # randomlmy generate some non numerical values it need to consist some digits as well as alphabets
        non_numerical_value = ''.join(random.choice(string.ascii_letters + string.digits+ string.punctuation) for _ in range(10))
        # use np.where to add non numerical values to the dataframe
        df[column] = np.where(df['id'].isin(non_numerical_rows['id']), non_numerical_value, df[column])

    return df


def add_invalid_dates(df:pd.DataFrame, columns:list, invalid_date:str = "abc",
                                                  invalid_date_percentage:float = 0.5) -> pd.DataFrame:
    """
    This function adds invalid dates to the date columns in the dataframe

    Args:
        df (pd.DataFrame): Dataframe to be polluted
        columns (list): List of columns to be polluted
        invalid_date (str): Invalid date to be added
        invalid_date_percentage (float): Percentage of invalid dates to be added

    Returns:
        pd.DataFrame: Polluted dataframe
    """
    # check if invalid date percentage is valid
    if invalid_date_percentage < 0 or invalid_date_percentage > 1:
        raise ValueError("Invalid date percentage should be between 0 and 1")

    # get the number of invalid dates to be added
    num_invalid_dates = int(len(df) * invalid_date_percentage)
    if not isinstance(columns, list):
        columns = [columns]
    for column in columns:
        # get a random sample of rows to be polluted
        invalid_date_rows = df.sample(num_invalid_dates)
        # randomlmy generate some invalid dates
        invalid_date = ''.join(random.choice(string.digits+ '/- :') for _ in range(10))
        # use np.where to add invalid dates to the dataframe
        df[column] = np.where(df['id'].isin(invalid_date_rows['id']), invalid_date, df[column])

    return df


def add_noise_to_numerical_columns(df:pd.DataFrame, 
                                   columns:list, 
                                   noise_scale:int = 1,
                                   noise_percentage:float = 0.5) -> pd.DataFrame:
    """
    This function adds noise to the numerical columns in the dataframe

    Args:
        df (pd.DataFrame): Dataframe to be polluted
        columns (list): List of columns to be polluted
        noise_scale (int): Scale of the noise to be added
        noise_percentage (float): Percentage of noise to be added

    Returns:
        pd.DataFrame: Polluted dataframe
    """
    # check if noise percentage is valid
    if noise_percentage < 0 or noise_percentage > 1:
        raise ValueError("Noise percentage should be between 0 and 1")

    # get the number of noise to be added
    num_noise = int(len(df) * noise_percentage)
    if not isinstance(columns, list):
        columns = [columns]
    for column in columns:
        # get a random sample of rows to be polluted
        noise_rows = df.sample(num_noise)
        # randomlmy generate some noise
        noise = np.random.normal(0, 1, num_noise)*noise_scale
        # use np.where to add noise to the dataframe
        df[column] = np.where(df['id'].isin(noise_rows['id']), noise, df[column])

    return df


def randomise_character_case(df: pd.DataFrame, column: str, randomise_percentage: float = 0.5) -> pd.DataFrame:
    """
    This function randomises the case of the characters in the column

    Args:
        df (pd.DataFrame): Dataframe to be polluted
        column (str): Column to be polluted
        randomise_percentage (float): Percentage of characters to be randomised

    Returns:
        pd.DataFrame: Polluted dataframe
    """
    # check if randomise percentage is valid
    if randomise_percentage < 0 or randomise_percentage > 1:
        raise ValueError("Randomise percentage should be between 0 and 1")

    # get the number of characters to be randomised
    num_randomise = int(len(df) * randomise_percentage)

    # get a random sample of rows to be polluted
    randomise_rows = df.sample(num_randomise)

    # randomise the case of the characters in the column
    df[column] = df[column].apply(lambda x: ''.join(random.choice([i.upper(), i.lower()]) for i in x) if x in randomise_rows[column].values else x)

    return df