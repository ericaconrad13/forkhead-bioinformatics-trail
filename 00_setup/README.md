# Módulo 00: ambiente e primeiro contato com FOXG1

## Objetivo
 Configurar o ambiente e fazer uma primeira caracterização da sequência de FOXG1.

## Métodos 
Foi criado o ambiente forkhead, com o Python 3.12.16, Biopython 1.88. A sequência foi buscada no UniProt com código P55316 e o script montado busca essa sequência a lê com a SeqIO e a análise com o ProtParam

## Resultados 
A FOXG1 humana tem 489 resíduos, massa molecular 52351,8 Da, pI 8,99 e tem como resíduos mais frequentes P 63, S 54, G 48, L 38, A 36.


## Limitações 
O pI é da proteína inteira, mas o começo com bastante histidina fica no começo, assim não significa que o domínio FOXHEAD seja básico. Estou apenas no começo da análise estrutural, mas já sei quais são as proporções de resíduos existentes e que a histidina aparece no começo, mas não está no top 5 (Prolina, Serina, Glicina, Leucina e Alanina) de resíduos e que prolina, serina e glicina juntas são cerca de um terço da proteína. E esse trio é típico de regiões intrinsecamente desordenadas (prolina quebra hélices, glicina é flexível demais, a serina é pequena e polar). 

## O que aprendi 
 - git, commit e .gitignore; um commit por ideia completa e funcionando
 - cabeçalho FASTA do UniProt (sp, OS, OX, GN, PE, SV)
 - Biopython é dividido em módulos, SeqIO lê arquivos e devolve SeqRecord
 - indexação a partir de zero (seq[:60])
 - ler traceback de baixo para cima
 - sorted com key=lambda e reverse=True
 - pI: K e R puxam para cima; His (pKa ~6) pesa pouco