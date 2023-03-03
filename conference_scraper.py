import pandas as pd
from concurrent.futures import ThreadPoolExecutor
from tasks import get_conference_data
chunks = pd.read_csv('conferences', usecols=['URL'], chunksize=50, index_col=False)
for chunk in chunks:
    with ThreadPoolExecutor() as executor:
        executor.map(get_conference_data, chunk.values)
