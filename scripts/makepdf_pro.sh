#!/bin/bash

# ==============================================================================
# Professional DevOps Lab PDF Generator
# Purpose: Converts GitHub Pages HTML to a unified PDF Lab Report
# Requirements: pandoc, xelatex (texlive-xetex)
# ==============================================================================

# --- Configuration & Logging ---
LOG_FILE="pdf_generator.log"
OUTPUT_PDF="DevOps_Lab_Report.pdf"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

exec > >(tee -a "$LOG_FILE") 2>&1

echo "----------------------------------------------------------------"
echo "Starting PDF Generation at $TIMESTAMP"
echo "----------------------------------------------------------------"

# --- Function: Error Handler ---
error_exit() {
    echo "[ERROR] $1" >&2
    exit 1
}

# --- 1. Dependency Check ---
echo "[1/4] Verifying Dependencies..."
command -v pandoc >/dev/null 2>&1 || error_exit "Pandoc is not installed. Run 'sudo apt install pandoc'."
command -v xelatex >/dev/null 2>&1 || error_exit "XeLaTeX (texlive-xetex) is not installed."

# --- 2. Interactive Inputs ---
echo "[2/4] Collecting Student Metadata..."
read -p "Enter Full Name: " AUTHOR
read -p "Enter SAP ID: " SAPID
read -p "Enter Index URL: " INDEX_URL

if [[ -z "$AUTHOR" || -z "$SAPID" || -z "$INDEX_URL" ]]; then
    error_exit "Metadata fields and Index URL cannot be empty."
fi

# --- 3. URL Collection ---
URLS=("$INDEX_URL")
echo "Enter experiment URLs (one per line). Press ENTER on an empty line to finish:"

while true; do
    read -p "Add URL: " URL
    [[ -z "$URL" ] ] && break
    
    # Simple URL Validation
    if [[ ! "$URL" =~ ^https?:// ]]; then
        echo "[WARN] Invalid URL format: $URL. Skipping..."
        continue
    fi
    URLS+=("$URL")
done

if [ ${#URLS[@]} -eq 1 ]; then
    echo "[WARN] No experiment URLs added. Only the index will be converted."
fi

# --- 4. PDF Generation ---
echo "[3/4] Generating PDF using Pandoc (XeLaTeX engine)..."
echo "This may take a moment depending on the number of pages..."

pandoc "${URLS[@]}" \
    -o "$OUTPUT_PDF" \
    --pdf-engine=xelatex \
    --toc \
    --number-sections \
    -V geometry:margin=1in \
    -V mainfont="DejaVu Sans" \
    -M title="DevOps Infrastructure Laboratory Report" \
    -M author="$AUTHOR | SAP ID: $SAPID" \
    -M date="$(date "+%B %d, %Y")"

# --- 5. Verification ---
if [ -f "$OUTPUT_PDF" ]; then
    echo "[4/4] SUCCESS: PDF generated successfully as '$OUTPUT_PDF'."
    echo "Check '$LOG_FILE' for details."
else
    error_exit "PDF generation failed. Check the log file for LaTeX errors."
fi

echo "----------------------------------------------------------------"
