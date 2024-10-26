# Installazione di conda e creazione dell'ambiente di lavoro

(miniconda3)

## Installazione

Durante la fase di installazione accettare la modifica del file bashrc

Se durante l'installazione non è stata fatta fare la modifica al bashrc, eseguire il seguente
```bash 
conda init
```

Se 'conda' non è disponibile aggiungere al bashrc
```bash
alias conda='miniconda3/bin/conda'
```


#### - Disattivare l'attivazione automatica del base environment
```bash
conda config --set auto_activate_base false
```
in questo modo all'apertura del terminale non si è in nessun ambiente

## Eliminazione

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

## Creazione e gestione dell'ambiente

#### - Creazione dell ambiente
```bash
conda create --prefix /home/.../folder python
```
viene installata l'ultima versione disponibile di python

per creare un ambiente nella directory di default --name env_name

#### - Rinominazione dell'ambiente
Dopo aver attivato l'ambiente
```bash
conda config --set env_prompt '({name})'
```
in questo modo al posto del path per intero compare solo il nome della cartella finale

#### - Creazione di una variabile per l'attivazione dell'ambiente

Nel caso di un prefix evita di dover inserire ogni volta il path per intero

In bashrc file
```bash  
export condaenv='/home/.../folder'
```    
dove '....' è il path dove si trova l'ambiente

Comando di attivazione dell'ambiente
```bash
conda activate $condaenv
```

## Pacchetti utilizzati in questo corso

#### - Installazione dei pacchetti
```bash
conda install -c conda-forge matplotlib
conda install -c conda-forge scipy
conda install -c conda-forge numpy
```

Nel caso matplotlib presenti problemi ad aprire una finestra grafica <>
```
conda install -c conda-forge pyqt
conda install -c conda-forge qt
```
