#!/usr/bin/env bash
set -euo pipefail

# Saccharomyces cerevisiae (S288C / RefSeq GCF_000146045.2)
URL="https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/GCF_000146045.2_R64_genomic.fna.gz"

GREEN="\033[1;32m"
CYAN="\033[1;36m"
RESET="\033[0m"

mkdir -p data/raw
TARGET="data/raw/sample.fasta"
echo -e "${CYAN} Downloading sample genome dataset...${RESET}"
curl -L --fail --progress-bar "$URL" | gunzip -c > "$TARGET"
echo ""
echo -e "${GREEN} Download completed:${RESET} $TARGET"
