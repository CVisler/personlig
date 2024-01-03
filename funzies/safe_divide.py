import pandas as pd
import numpy as np

def safe_divide(x: int, y: int) -> float:
    result = np.divide(x, y, out=np.nan, where=y != 0)
    return result.item() if not np.isnan(result) else 0

print(safe_divide(5,0))
