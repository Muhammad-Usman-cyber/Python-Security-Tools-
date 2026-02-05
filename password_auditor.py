import re

def password_audit():
    print("--- Corporate Password Policy Auditor ---")
    password = input("Enter password to test: ")
    
    score = 0
    remarks = ""
    
    # 1. Length Check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    
    # 2. Complexity Checks
    if re.search(r"\d", password): score += 1 # Numbers
    if re.search(r"[A-Z]", password): score += 1 # Uppercase
    if re.search(r"[!@#$%^&*]", password): score += 1 # Symbols

    # Output Results
    print(f"\nAudit Score: {score}/5")
    
    if score >= 4:
        print("Result: ✅ STRONG (Compliant with NIST Standards)")
    elif score == 3:
        print("Result: ⚠️ MEDIUM (Needs more complexity)")
    else:
        print("Result: 🚨 WEAK (Immediate change required)")

if __name__ == "__main__":
    password_audit()
