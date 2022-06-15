# 

You can use IPython.display to generate the audio controls in the frontend. It requires Jupyter notebooks but it is also compatible with Azure Machine Learning notebooks - no need to install anything.

```
import IPython
IPython.display.Audio("test.wav")
```


Fileshare: 
```
IPython.display.Audio("./[directoryOfTheFileInFileShare]/test.wav")
```

Datastore: mount the datastore and then read the file:
```
from azureml.core import Workspace, Datastore, Dataset
ws = Workspace.from_config()
datastore = Datastore.get(ws, datastore_name=[dataStoreName])
dataset = Dataset.File.from_files((datastore, ‘[PathToTheAudioFiles]/test.wav'))

mount_context = dataset.mount()
mount_context.start() 
IPython.display.Audio(mount_context.mount_point + '/test.wav')
```

