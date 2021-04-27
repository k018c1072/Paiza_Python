import pandas as pd
import numpy as np

l_complex = [{'label': 'X',
              'info': {'n': 'nx', 'm': 'mx'},
              'data': [{'a': 1, 'b': 2},
                       {'a': 3, 'b': 4}]},
             {'label': 'Y',
              'info': {'n': 'ny', 'm': 'my'},
              'data': [{'a': 10, 'b': 20},
                       {'a': 30, 'b': 40}]}]

print(pd.json_normalize(l_complex))

print(pd.json_normalize(l_complex, record_path='data'))

print(pd.json_normalize(
    l_complex, record_path='data', record_prefix='data_'))
