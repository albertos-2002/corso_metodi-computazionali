# Informazioni neccessarie per l'utilizzo della GUI

Parte necessaria (per non digitarlo manualmente ogni volta)
per far si che si apra la gui di matplotlib

```python
import os
# Set the QT_QPA_PLATFORM environment variable
os.environ['QT_QPA_PLATFORM'] = 'xcb'
```

Per ottenere informazioni o settare il backend
```python
#import matplotlib
#matplotlib.use('QtAgg')
#check the backend
#print("Current backend:", matplotlib.get_backend())
```

Per aprire la gui è necessario includere
```py
plt.show()
```
