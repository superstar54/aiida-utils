
## Install cp2k
conda create -yn cp2k-9.1

conda activate cp2k-9.1

conda install -c conda-forge cp2k



## create code from yaml
```
verdi code create core.code.installed --config pw-7.0-eiger.yaml
```