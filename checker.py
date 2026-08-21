# TCR-Epitope Binding Checker

def check_binding(tcr_cdr3, epitope):
    print(f"Analyzing TCR: {tcr_cdr3} with Epitope: {epitope}")

    # Simple rule: If both sequences exist, classify as Potential Match
    if len(tcr_cdr3) > 0 and len(epitope) > 0:
        return "Potential Binding Detected"
    else:
        return "Invalid Input"

# Test sequences
tcr_seq = "CASSYEQYF"
epitope_seq = "NLVPMVATV"

result = check_binding(tcr_seq, epitope_seq)
print(f"Result: {result}")