import pandas as pd
import numpy as np
import random
import string
import datetime
from datetime import timedelta

nRows = 1000

choices = ['apple','banana','orange','lemon']

pdf = pd.DataFrame(
  {'id': range(nRows),
   'date': [(datetime.datetime.now() + timedelta(-1 * np.random.randint(1,365))).strftime('%Y-%m-%d') for i in range(nRows)],
   'stores': ["stores "+random.choice(string.ascii_letters.upper()) for i in range(nRows)],
   'customers': ["customer "+random.choice(string.ascii_letters.upper())+str(random.randint(1,1000)) for i in range(nRows)],
   'value': [round(np.random.uniform(0,1000),2) for i in range(nRows)],
   'products': ["product "+random.choice(string.ascii_letters.upper()) for i in range(nRows)],
   'choices': [random.choice(choices) for i in range(nRows)],
   'discount_rate': [np.random.random() for i in range(nRows)]  
  }
)
print(pdf)