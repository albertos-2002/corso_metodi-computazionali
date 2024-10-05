# corso_metodi-computazionali

### In bashrc file:

- To add conda as an easier command
```bash
alias conda='miniconda3/bin/conda'
```
(dopo il conda init non so quanto rimanga utile)

- Per la modifica del file bashrc (se non fatto durante l'installazione?)
```bash 
conda init
```

- Disattivare l'attivazione automatica del base environment
```bash
conda config --set auto_activate_base false
```

- Creazione di una variabile per l'attivazione dell'ambiente

In bashrc file
```bash  
export mcenv='/home/alberto/UniPd_github/corso_metodi-computazionali/pyenv'
```    
Comando di attivazione dell'ambiente
```bash
conda activate $mcenv
```

