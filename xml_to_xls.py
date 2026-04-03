import pandas as pd
import logging
import os

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='--- [LOG] %(message)s ---')

def convert_xml_to_excel(xml_file='D406DOM.xml', xlsx_file='output.xlsx'):
    """Converts an XML file to an Excel file."""
    
    if not os.path.exists(xml_file):
        logging.error(f"Input file {xml_file} not found!")
        return

    try:
        logging.info(f"Parsing {xml_file}...")
        df = pd.read_xml(xml_file)  # Read XML file into a DataFrame
        
        logging.info(f"Writing to {xlsx_file}...")
        df.to_excel(xlsx_file, index=False, engine='openpyxl')  # Write DataFrame to Excel
        logging.info("--- [SUCCESS] Conversion complete! ---")
    except Exception as e:
        logging.error(f"Conversion failed: {e}")

if __name__ == "__main__":
    convert_xml_to_excel()
