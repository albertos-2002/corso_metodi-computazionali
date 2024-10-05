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

- Disattivare l'attivazione automatica del base environment
```bash
conda config --set auto_activate_base false
```
in questo modo all'apertura del terminale non si è in nessun ambiente


- Creazione di una variabile per l'attivazione dell'ambiente

In bashrc file
```bash  
export mcenv='/home/alberto/UniPd_github/corso_metodi-computazionali/pyenv'
```    
dove '....' è il path dove si trova l'ambiente

Comando di attivazione dell'ambiente
```bash
conda activate $mcenv
```

