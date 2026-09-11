#!/usr/bin/env bash
set -euo pipefail

URL="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/GCF_000005845.2_ASM584v2_genomic.fna.gz"
mkdir -p data/raw
TARGET="data/raw/sample.fasta"
curl -sSL --fail "$URL" | gunzip -c > "$TARGET"
