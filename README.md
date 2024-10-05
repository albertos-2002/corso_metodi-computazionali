# corso_metodi-computazionali

Durante la fase di installazione accettare la modifica del file bashrc

---
Se 'conda' non è disponibile aggiungere al bashrc
```bash
alias conda='miniconda3/bin/conda'
```

Se durante l'installazione non è stata fatta fare la modifica al bashrc, eseguire il seguente
```bash 
conda init
```
---

### - Disattivare l'attivazione automatica del base environment
```bash
conda config --set auto_activate_base false
```
in questo modo all'apertura del terminale non si è in nessun ambiente


### - Creazione di una variabile per l'attivazione dell'ambiente

In bashrc file
```bash  
export mcenv='/home/alberto/UniPd_github/corso_metodi-computazionali/pyenv'
```    
dove '....' è il path dove si trova l'ambiente

Comando di attivazione dell'ambiente
```bash
conda activate $mcenv
```

### - Rinominazione dell'ambiente
Dopo aver attivato l'ambiente
```bash
conda config --set env_prompt '({name})'
```
in questo modo al posto del path per intero compare solo il nome della cartella finale

---

### - Creazione dell ambiente
```bash
conda create --prefix /home/alberto/UniPd_github/corso_metodi-computazionali/pyenv python
```
viene installata l'ultima versione disponibile di python

il path puo essere cambiato 

per creare un ambiente nella directory di default --name env_name

### - Installazione dei pacchetti
```bash
conda install -c conda-forge matplotlib
conda install -c conda-forge scipy
conda install -c conda-forge numpy
```

### - Eliminazione

eliminare i seguenti file e/o cartelle

``` 
/conda o /anaconda3 o /miniconda3
.condarc
.conda
.continuum
.anaconda o .miniconda
```

per la rimozione delle modifiche dal bashrc
```bash
conda init --reverse --all
```
oppure rimuoverlo a mano
