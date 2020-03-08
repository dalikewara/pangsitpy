import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler


def min_max_scaler(data_to_scale, fit_from_data=None, fit_from_file=None,
                   drop_columns=None):
    scaler = MinMaxScaler()
    if fit_from_data:
        scaler.fit(fit_from_data)
    elif fit_from_file:
        df = pd.read_csv(fit_from_file, engine='python', encoding='latin-1', skipinitialspace=True)
        if drop_columns:
            df.drop(drop_columns, axis=0, inplace=True)
        scaler.fit(df.values)
    else:
        scaler.fit(data_to_scale)
    result = scaler.transform(data_to_scale)
    return {
        "scaler": scaler,
        "result": result
    }


def standart_scaler(data_to_scale, fit_from_data=None, fit_from_file=None,
                    drop_columns=None):
    scaler = StandardScaler()
    if fit_from_data:
        scaler.fit(fit_from_data)
    elif fit_from_file:
        df = pd.read_csv(fit_from_file, engine='python', encoding='latin-1', skipinitialspace=True)
        if drop_columns:
            df.drop(drop_columns, axis = 0, inplace = True)
        scaler.fit(df.values)
    else:
        scaler.fit(data_to_scale)
    result = scaler.transform(data_to_scale)
    return {
        "scaler": scaler,
        "result": result
    }
