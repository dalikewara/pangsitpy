import os
import pandas as pd
from pangsitpy.scaling import min_max_scaler

data_to_scale = [[34, 4]]
fit_from_data = [[-1, 2], [-0.5, 6], [0, 10], [1, 18], [29, 4]]
fit_from_file =os.path.join(os.path.dirname(__file__), 'files/audio.csv')
df = pd.read_csv(fit_from_file, engine='python', encoding='latin-1', skipinitialspace=True)
data_scale = min_max_scaler(data_to_scale)
print(data_scale['result'])
print('=====')
data_scale = min_max_scaler(data_to_scale, fit_from_data=fit_from_data)
print(data_scale['result'])
print('=====')
data_scale = min_max_scaler(df.values, fit_from_file=fit_from_file)
print(data_scale['result'])
print('=====')