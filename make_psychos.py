""" Make Psychopath csv file
"""

import pandas as pd

psychopathy = [11.416,   4.514,  12.204,  14.835,
                8.416,   6.563,  17.343, 13.02,
               15.19 ,  11.902,  22.721,  22.324]

clammy = [0.389,  0.2  ,  0.241,  0.463,
          4.585,  1.097,  1.642,  4.972,
          7.957,  5.585,  5.527,  6.964]

university = ['Berkeley'] * 4 + ['Stanford'] * 4 + ['MIT'] * 4

df = pd.DataFrame.from_items([
    ('psychopathy', psychopathy),
    ('clammy', clammy),
    ('university', university)])

df.to_csv('psycho_students.csv', index=False)
