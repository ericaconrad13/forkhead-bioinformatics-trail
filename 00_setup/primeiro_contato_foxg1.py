"""Primeiro contato com FOXG1: baixa a sequência do Uniprot e mostra informações básicas."""

from io import StringIO

import requests
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

UNIPROT_ID = "P55316"  # FOXG1 humano
url = f"http://rest.uniprot.org/uniprotkb/{UNIPROT_ID}.fasta"

resposta = requests.get(url, timeout=30)
resposta.raise_for_status()

registro = SeqIO.read(StringIO(resposta.text), "fasta")

print("ID:", registro.id)
print("Descrição:", registro.description)
print("Comprimento:", len(registro.seq), "aminoácidos")
print("Primeiros 60 resíduos:", registro.seq[:60])

analise = ProteinAnalysis(str(registro.seq))

print("Massa molecular (Da):", round(analise.molecular_weight(), 1))
print("pI:", round(analise.isoelectric_point(), 2))