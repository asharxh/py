# Data Normalizer Setup & Usage Guide

## Quick Start (5 minutes)

### Step 1: Install Python (if not already installed)
- **Windows**: Download from [python.org](https://python.org) (version 3.8 or higher)
- **Mac**: Python usually pre-installed, or use `brew install python3`

### Step 2: Install Required Libraries
Open Terminal (Mac) or Command Prompt (Windows) and run:
```bash
pip install pandas openpyxl numpy
```

### Step 3: Setup Folder Structure
1. Create a new folder for this project (e.g., `DataProcessor`)
2. Save the Python script as `data_normalizer.py` in this folder
3. The script will automatically create:
   - `input/` folder (place your raw files here)
   - `output/` folder (cleaned files appear here)
   - `config.json` file (customize settings)

### Step 4: Run the Process
1. Place your CSV/Excel files in the `input` folder
2. Double-click `data_normalizer.py` OR run from terminal:
   ```bash
   python data_normalizer.py
   ```
3. Check the `output` folder for cleaned files

## Features

### ✅ What It Does
- **Normalizes headers** (e.g., "ID", "Record Number" → `record_id`)
- **Classifies records** as Residential, Commercial, or Unknown
- **Removes duplicates** based on ID columns
- **Combines multiple files** into one master sheet
- **Exports both** individual cleaned files AND combined dataset
- **Handles large datasets** efficiently
- **Works with** CSV, XLS, and XLSX files

### 📁 File Structure After Setup
```
DataProcessor/
├── data_normalizer.py     # Main script
├── config.json            # Settings file (auto-created)
├── input/                 # Put raw files here
│   ├── permits_jan.csv
│   ├── records_feb.xlsx
│   └── data_march.xls
└── output/               # Clean files appear here
    ├── cleaned_permits_jan.csv
    ├── cleaned_records_feb.csv
    ├── cleaned_data_march.csv
    └── combined_data_20240115_143022.csv
```

## Customization Guide

### Modify Classification Keywords
Edit `config.json` to add/remove keywords:

```json
"classification_rules": {
    "residential": [
        "residential", "house", "home", "dwelling",
        "YOUR_NEW_KEYWORD_HERE"
    ],
    "commercial": [
        "commercial", "business", "office", 
        "YOUR_NEW_KEYWORD_HERE"
    ]
}
```

### Add New Header Mappings
To recognize new column variations, add to `header_mappings`:

```json
"header_mappings": {
    "your_weird_column_name": "standard_name",
    "another_variation": "standard_name"
}
```

### Control Which Columns to Keep
Modify `columns_to_keep` in config.json:

```json
"columns_to_keep": [
    "record_id", "date", "description", "address",
    "ADD_YOUR_COLUMN_HERE"
]
```

### Toggle Features On/Off
```json
"deduplicate": true,           # Set to false to keep duplicates
"combine_files": true,         # Set to false for individual files only
"export_individual_files": true # Set to false for combined file only
```

## Troubleshooting

### Common Issues & Solutions

**"No module named pandas"**
- Run: `pip install pandas openpyxl numpy`

**"No files found in input folder"**
- Make sure files are in the `input` folder (not subfolders)
- Check file extensions are .csv, .xls, or .xlsx

**Memory errors with large files**
- Process files individually by setting `"combine_files": false`
- Increase available memory or process in batches

**Dates not parsing correctly**
- The script handles most date formats automatically
- For unusual formats, files may need preprocessing

**Classification showing mostly "Unknown"**
- Add more keywords specific to your data in config.json
- Check that description/address columns exist in your data

## Advanced Usage

### Running from Command Line
```bash
# Basic run
python data_normalizer.py

# With specific config file
python data_normalizer.py --config my_config.json
```

### Batch Processing Multiple Folders
Create multiple config files with different input/output folders:
```json
// config_permits.json
"input_folder": "permits_raw",
"output_folder": "permits_clean"

// config_licenses.json
"input_folder": "licenses_raw",
"output_folder": "licenses_clean"
```

### Creating a Batch File (Windows)
Save as `run_processor.bat`:
```batch
@echo off
echo Processing data files...
python data_normalizer.py
echo Done! Check output folder.
pause
```

### Creating a Shell Script (Mac/Linux)
Save as `run_processor.sh`:
```bash
#!/bin/bash
echo "Processing data files..."
python3 data_normalizer.py
echo "Done! Check output folder."
read -p "Press enter to continue"
```

## Data Quality Tips

1. **Consistent Input**: The cleaner your input data, the better the results
2. **Review Classifications**: Check the "Unknown" category for patterns to add to keywords
3. **ID Columns**: Ensure your files have some form of unique identifier
4. **Regular Updates**: Periodically update config.json based on new data patterns

## Output Files

### Individual Cleaned Files
- Named: `cleaned_[original_name].csv`
- Contains all processed records from single source
- Classification column added

### Combined Master File
- Named: `combined_data_[timestamp].csv` and `.xlsx`
- Includes all records from all input files
- Additional `source_file` column shows origin
- Duplicates removed across all files

## Performance Notes

- **Small datasets** (< 10,000 rows): Instant processing
- **Medium datasets** (10,000 - 100,000 rows): 5-30 seconds
- **Large datasets** (100,000+ rows): 1-5 minutes
- **Memory usage**: Approximately 5-10x the file size

## Support & Maintenance

### Updating the Script
Simply replace the .py file with any newer version

### Backing Up Configuration
Keep a copy of your customized `config.json` file

### Version Control
Consider using Git to track changes to your configuration

---

**Note**: This tool processes data locally on your machine. No data is sent to external servers.