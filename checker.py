
# TCR-Epitope Binding Checker

def check_binding(tcr_cdr3, epitope):
    print(f"Analyzing TCR: {tcr_cdr3} with Epitope: {epitope}")

    # Improved rule: Check if first 3 amino acids of epitope match inside CDR3
    motif = epitope[:3]
    if motif in tcr_cdr3:
        return f"Strong Binding (Motif '{motif}' matched)"
    return "Low/No Binding"

tcr_seq = "CASSYEQYF"
epitope_seq = "CASPMVATV"

result = check_binding(tcr_seq, epitope_seq)
print(f"Result: {result}")