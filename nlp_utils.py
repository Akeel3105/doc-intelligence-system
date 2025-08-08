# nlp_utils.py
import re

def extract_entities(text: str) -> dict:
    results = {"Name": None, "Date of Birth": None, "PAN Number": None}

    lines = text.splitlines()
    for line in lines:
        line = line.strip()

        # PAN detection
        if not results["PAN Number"]:
            pan_match = re.search(r"[A-Z]{5}[0-9]{4}[A-Z]", line)
            if pan_match:
                results["PAN Number"] = pan_match.group(0)

        # DOB detection (even if no "DOB:" prefix)
        if not results["Date of Birth"]:
            dob_match = re.search(r"\d{2}[\/\-]\d{2}[\/\-]\d{4}", line)
            if dob_match:
                results["Date of Birth"] = dob_match.group(0)

    # Heuristic for Name – assume it's the **first valid line** that is not PAN or DOB
    for line in lines:
        line = line.strip()
        if (results["Date of Birth"] and results["Date of Birth"] in line) or \
           (results["PAN Number"] and results["PAN Number"] in line):
            continue
        if len(line.split()) >= 2 and line.isalpha():
            results["Name"] = line
            break

    return results


