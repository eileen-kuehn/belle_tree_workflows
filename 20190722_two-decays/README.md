# Distance matrix for two decay modes

This workflow calculates the distances matrices for two different decays of the Belle collaboration.
Both decays include 1.000 decay trees.
Within the workflow, each of the trees is loaded and several distance metrics are applied, to calculate the distance matrices.
The resulat is stored in HDF5 format in folder *final*.
Each of the resulting matrices is stored as a Dataframe named `df_index`. 
The index is increased for each of the applied distance metrics.
So the first matrix can be loaded from the key `df_0`.

To list all keys you can use:

```python
import pandas as pd

filename = "file.h5"  # specify filename here
print(pd.HDFStore(filename).keys())
```

The data itself further contains metadata information on how it was created, including the algorithm and signature used.
These metadata are stored in python dictionary format and can be accessed via:

```python
store = pd.HDFStore(filename)
store.get_storer(df_name).attrs.meta
```

The output contains for example the following information:

```
{
  'algorithm': "IncrementalDistanceAlgorithm (cache_statistics=SplittedStatistics, distance=StartDistance, supported=['ProcessStartEvent'])",
  'signature': 'PQGramSignature (p=1, q=0)',
  'event_streamer': 'GNMCSVEventStreamer(None)',
  'date': '2019-07-24 17:42:40.263174',
  'source': 'development/assess_workflows/assess_workflows/../workflow.py (process_as_matrix)',
  'version': '/lib/python/assess'
}
```
