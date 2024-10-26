# Funzioni util

## Aggiunta del path

```python
import sys
sys.path.append("path/to/util")
```

Sono così disponibili per l'import gli script inseriti nella cartella util

```python
import make_range as mr
import set_graph as sg
```

## make_range.py (deprecated)

Creazione di un range quasi-simmetrico rispetto allo 0

Per la struttura del codice i punti creati appartengono all'intervallo $[-xMax, xMax-step]$ per un totale di punti pari a $NUmeroPunti$ e un numero di intervalli pari a $NumeroPunti-1$

Variabile $step$ è disponibile per la lettura, contiene appunto lo stepping size tra un punto e il successivo

#### range_man()
range creato manualmente

#### range_np()
range creato con $numpy.arange()$

#### ask_range(npFlag)

se $npFlag =$ "$np$" il range viene creato con $range_np$

chiede di inserire $xMax$ e $NumeroPunti$ e procede a create il corrispettivo range

## set_graph.py

#### make_fine(axObj)

la funzione prende come argomento un oggetto di tipo $axes$ di matplotlib, disegna gli assi per $x=0$ e $y=0$, setta la griglia e la legenda

#### set_style(fontSize=10, markerSize=6)

la funzione accetta come argomento gli interi per definire le dimenzione dei marker e del font, i valori predefiniti inseriti sono quelli di default di matplotlib, il nome font per il nome degli assi e quello della legenta è rispettivamente aumentato e diminuti rispetto a quello di default

la funzione setta anche il $tight_layout()$ e mette a $False$ l'uso di Tex in modo da usare quello intergrato di matplotlib 