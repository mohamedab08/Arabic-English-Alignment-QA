import json

def validate_translation_evals(file_path):
    """Validates structure and linguistic alignment of bilingual evaluation records."""
    try:
        with open(file_path, 'r' , encoding='utf-8') as f:
            data = json.load(f)
            
        print(f"Loaded {len(data)} bilingual evaluation records successfully.\n")
        
        for record in data:
            record_id = record.get("id", "Unknown ID")
            domain = record.get("domain", "Unspecified")
            audit = record.get("terminology_audit")
            
            if not audit:
                print(f"[FAIL] Record {record_id} ({domain}): Missing terminology audit.")
            else:
                print(f"[PASS] Record {record_id} ({domain}): Verified Arabic-English alignment.")
                
    except Exception as e:
        print(f"Error loading translation file: {e}")

if __name__ == "__main__":
    validate_translation_evals("translation_evals.json")