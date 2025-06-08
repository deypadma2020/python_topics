# from taipy import Gui

# page = '''# Getting started with Taipy'''

# Gui(page = page).run(debug = True, port = 5008)

import numpy  as np
import pandas as pd
from taipy import Gui

x = np.linspace(0, 10, 100)
y = np.sin(x)

df = pd.DataFrame({'x': x, 'y': y})

page = '''#Sign Wave Visualization
<|{df}|chart|type=line|x=x|y=y|>'''

Gui(page = page).run(debug = True, port = 5008)