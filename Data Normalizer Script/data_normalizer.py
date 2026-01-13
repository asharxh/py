#!/usr/bin/env python3
"""
Data Normalizer and Classifier
A user-friendly ETL tool for processing CSV/Excel files with automatic classification
"""

import pandas as pd
import numpy as np
import os
import sys
import json
import glob
from datetime import datetime
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configuration file path
CONFIG_FILE = 'config.json'

def load_config():
    """Load configuration from JSON file or create default"""
    default_config = {
        "input_folder": "input",
        "output_folder": "output",
        
        "header_mappings": {
            # ID mappings
            "id": "record_id",
            "record number": "record_id",
            "record_number": "record_id",
            "ref_num": "record_id",
            "reference": "record_id",
            "permit_number": "record_id",
            "permit number": "record_id",
            "case_number": "record_id",
            "case number": "record_id",
            
            # Date mappings
            "date": "date",
            "issue_date": "issue_date",
            "issued": "issue_date",
            "application_date": "application_date",
            "applied": "application_date",
            "completion_date": "completion_date",
            "completed": "completion_date",
            
            # Description mappings
            "description": "description",
            "desc": "description",
            "details": "description",
            "work_description": "description",
            "project_description": "description",
            "scope": "description",
            
            # Address mappings
            "address": "address",
            "location": "address",
            "site_address": "address",
            "property_address": "address",
            "street": "address",
            
            # Owner/Contractor mappings
            "owner": "owner",
            "property_owner": "owner",
            "applicant": "owner",
            "contractor": "contractor",
            "builder": "contractor",
            
            # Value/Fee mappings
            "valuation": "valuation",
            "value": "valuation",
            "estimated_cost": "valuation",
            "project_value": "valuation",
            "fee": "fee",
            "fees": "fee",
            "permit_fee": "fee",
            "total_fee": "fee"
        },
        
        "columns_to_keep": [
            "record_id", "issue_date", "application_date", "completion_date",
            "description", "address", "owner", "contractor", 
            "valuation", "fee", "type", "status", "category"
        ],
        
        "classification_rules": {
            "residential": [
                "residential", "house", "home", "dwelling", "residence",
                "single family", "single-family", "duplex", "triplex",
                "apartment", "condo", "townhouse", "townhome",
                "bedroom", "kitchen", "bathroom", "garage",
                "deck", "patio", "fence", "pool", "spa"
            ],
            "commercial": [
                "commercial", "business", "office", "retail", "store",
                "shop", "restaurant", "warehouse", "industrial",
                "manufacturing", "factory", "hotel", "motel",
                "mall", "plaza", "center", "suite", "tenant",
                "storefront", "showroom", "clinic", "hospital"
            ]
        },
        
        "deduplicate": True,
        "deduplicate_columns": ["record_id"],
        "combine_files": True,
        "export_individual_files": True
    }
    
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                loaded_config = json.load(f)
                # Merge with defaults to ensure all keys exist
                for key, value in default_config.items():
                    if key not in loaded_config:
                        loaded_config[key] = value
                return loaded_config
        except Exception as e:
            print(f"Error loading config file: {e}")
            print("Using default configuration...")
    else:
        # Save default config for user reference
        with open(CONFIG_FILE, 'w') as f:
            json.dump(default_config, f, indent=4)
        print(f"Created default configuration file: {CONFIG_FILE}")
    
    return default_config

def ensure_folders(config):
    """Create input and output folders if they don't exist"""
    for folder in [config['input_folder'], config['output_folder']]:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Created folder: {folder}")

def normalize_headers(df, config):
    """Normalize column headers based on mapping configuration"""
    # Convert all headers to lowercase for matching
    df.columns = df.columns.str.lower().str.strip()
    
    # Apply mappings
    rename_dict = {}
    for col in df.columns:
        normalized_col = col.replace('_', ' ').replace('-', ' ').strip()
        if normalized_col in config['header_mappings']:
            rename_dict[col] = config['header_mappings'][normalized_col]
        elif col in config['header_mappings']:
            rename_dict[col] = config['header_mappings'][col]
    
    df = df.rename(columns=rename_dict)
    return df

def classify_record(row, config):
    """Classify a record as Residential, Commercial, or Unknown"""
    # Combine relevant text fields for analysis
    text_fields = []
    for field in ['description', 'address', 'type', 'category']:
        if field in row.index and pd.notna(row[field]):
            text_fields.append(str(row[field]).lower())
    
    combined_text = ' '.join(text_fields)
    
    # Check for residential keywords
    residential_score = sum(1 for keyword in config['classification_rules']['residential'] 
                           if keyword in combined_text)
    
    # Check for commercial keywords
    commercial_score = sum(1 for keyword in config['classification_rules']['commercial'] 
                          if keyword in combined_text)
    
    # Classify based on scores
    if residential_score > commercial_score:
        return 'Residential'
    elif commercial_score > residential_score:
        return 'Commercial'
    else:
        return 'Unknown'

def clean_dataframe(df, config):
    """Clean and process a dataframe"""
    print(f"  Processing {len(df)} records...")
    
    # Normalize headers
    df = normalize_headers(df, config)
    
    # Add classification column
    df['classification'] = df.apply(lambda row: classify_record(row, config), axis=1)
    
    # Keep only specified columns (that exist in the dataframe)
    columns_to_keep = ['classification'] + [col for col in config['columns_to_keep'] 
                                           if col in df.columns]
    df = df[columns_to_keep]
    
    # Remove duplicates if configured
    if config['deduplicate']:
        initial_count = len(df)
        dedupe_cols = [col for col in config['deduplicate_columns'] if col in df.columns]
        if dedupe_cols:
            df = df.drop_duplicates(subset=dedupe_cols, keep='first')
            removed = initial_count - len(df)
            if removed > 0:
                print(f"  Removed {removed} duplicate records")
    
    # Clean numeric columns
    if 'valuation' in df.columns:
        df['valuation'] = pd.to_numeric(df['valuation'].astype(str).str.replace('$', '').str.replace(',', ''), errors='coerce')
    if 'fee' in df.columns:
        df['fee'] = pd.to_numeric(df['fee'].astype(str).str.replace('$', '').str.replace(',', ''), errors='coerce')
    
    # Parse dates
    date_columns = [col for col in df.columns if 'date' in col.lower()]
    for col in date_columns:
        df[col] = pd.to_datetime(df[col], errors='coerce')
    
    return df

def process_file(filepath, config):
    """Process a single file"""
    filename = os.path.basename(filepath)
    print(f"\nProcessing: {filename}")
    
    try:
        # Read file based on extension
        if filepath.endswith('.csv'):
            df = pd.read_csv(filepath, low_memory=False)
        elif filepath.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(filepath)
        else:
            print(f"  Skipping unsupported file type: {filename}")
            return None
        
        # Clean the dataframe
        df = clean_dataframe(df, config)
        
        # Add source file column
        df['source_file'] = filename
        
        print(f"  Successfully processed {len(df)} records")
        print(f"  Classification breakdown:")
        print(f"    Residential: {len(df[df['classification'] == 'Residential'])}")
        print(f"    Commercial: {len(df[df['classification'] == 'Commercial'])}")
        print(f"    Unknown: {len(df[df['classification'] == 'Unknown'])}")
        
        return df
        
    except Exception as e:
        print(f"  Error processing {filename}: {str(e)}")
        return None

def main():
    """Main processing function"""
    print("=" * 60)
    print("DATA NORMALIZER AND CLASSIFIER")
    print("=" * 60)
    
    # Load configuration
    config = load_config()
    print(f"\nConfiguration loaded from: {CONFIG_FILE}")
    
    # Ensure folders exist
    ensure_folders(config)
    
    # Get list of files to process
    input_patterns = [
        os.path.join(config['input_folder'], '*.csv'),
        os.path.join(config['input_folder'], '*.xlsx'),
        os.path.join(config['input_folder'], '*.xls')
    ]
    
    files = []
    for pattern in input_patterns:
        files.extend(glob.glob(pattern))
    
    if not files:
        print(f"\nNo CSV or Excel files found in '{config['input_folder']}' folder.")
        print(f"Please place your data files in the '{config['input_folder']}' folder and run again.")
        input("\nPress Enter to exit...")
        return
    
    print(f"\nFound {len(files)} file(s) to process")
    
    # Process each file
    all_dataframes = []
    for filepath in files:
        df = process_file(filepath, config)
        if df is not None:
            all_dataframes.append(df)
            
            # Export individual file if configured
            if config['export_individual_files']:
                base_name = Path(filepath).stem
                output_path = os.path.join(config['output_folder'], f"cleaned_{base_name}.csv")
                df.drop('source_file', axis=1, errors='ignore').to_csv(output_path, index=False)
                print(f"  Exported to: {output_path}")
    
    # Combine all files if configured
    if config['combine_files'] and len(all_dataframes) > 0:
        print("\nCombining all files...")
        combined_df = pd.concat(all_dataframes, ignore_index=True)
        
        # Remove duplicates from combined dataset
        if config['deduplicate']:
            initial_count = len(combined_df)
            dedupe_cols = [col for col in config['deduplicate_columns'] if col in combined_df.columns]
            if dedupe_cols:
                combined_df = combined_df.drop_duplicates(subset=dedupe_cols, keep='first')
                removed = initial_count - len(combined_df)
                if removed > 0:
                    print(f"Removed {removed} duplicates from combined dataset")
        
        # Export combined file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        combined_csv = os.path.join(config['output_folder'], f"combined_data_{timestamp}.csv")
        combined_excel = os.path.join(config['output_folder'], f"combined_data_{timestamp}.xlsx")
        
        combined_df.to_csv(combined_csv, index=False)
        combined_df.to_excel(combined_excel, index=False, engine='openpyxl')
        
        print(f"\nCombined dataset statistics:")
        print(f"  Total records: {len(combined_df)}")
        print(f"  Classification breakdown:")
        print(f"    Residential: {len(combined_df[combined_df['classification'] == 'Residential'])}")
        print(f"    Commercial: {len(combined_df[combined_df['classification'] == 'Commercial'])}")
        print(f"    Unknown: {len(combined_df[combined_df['classification'] == 'Unknown'])}")
        print(f"\nExported combined data to:")
        print(f"  CSV: {combined_csv}")
        print(f"  Excel: {combined_excel}")
    
    print("\n" + "=" * 60)
    print("PROCESSING COMPLETE!")
    print("=" * 60)
    
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        input("\nPress Enter to exit...")
        sys.exit(1)