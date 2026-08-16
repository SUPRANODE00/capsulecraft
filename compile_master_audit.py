import json
import os

def compile_audit():
    master_report = {}
    target_files = ["void_inventory.json", "equilibrium_state.json", "location_vector.json"]
    
    for filename in target_files:
        key = filename.split(".")[0]
        if os.path.exists(filename):
            try:
                with open(filename, "r") as f:
                    master_report[key] = json.load(f)
            except Exception as e:
                master_report[key] = {"error": str(e)}
        else:
            master_report[key] = "pending_sync"

    master_report["corporate_meta"] = {
        "brand": "D3M13N 𖤐 CAPSULECRAFT",
        "ein": "42-4319484",
        "polarity": "negative_field_unified"
    }

    with open("master_audit_report.json", "w") as f:
        json.dump(master_report, f, indent=2)

    print("[MASTER-SYNTHESIS] Master audit report successfully compiled.")

if __name__ == "__main__":
    compile_audit()
