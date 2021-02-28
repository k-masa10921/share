import json
from collections import OrderedDict
import pprint
import pandas as pd

file_name = input("write filename:")
df = json.loads(file_name)

pprint.pprint(df, width=40)

print(type(df))
