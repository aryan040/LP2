def triage_system():
    print("=== Hospital Expert System: Patient Triage Assistant ===")

    name = input("Enter Patient Name: ").strip()
    
    # Robust Age Input
    try:
        age = int(input("Enter Age: "))
    except ValueError:
        print("Invalid age entered. Defaulting to 0.")
        age = 0

    print("\nSelect Symptoms (Y/N):")
    
    # Helper function to reduce repetitive .lower() == 'y'
    def get_yes_no(prompt):
        return input(prompt).lower().strip().startswith('y')

    chest_pain = get_yes_no("Chest Pain? ")
    short_breath = get_yes_no("Shortness of Breath? ")
    bleeding = get_yes_no("Heavy Bleeding? ")
    high_fever = get_yes_no("High Fever? ")
    injury = get_yes_no("Recent Injury? ")
    dizziness = get_yes_no("Dizziness or Fainting? ")
    stomach_pain = get_yes_no("Severe Stomach Pain? ")

    print("\nAnalyzing symptoms...")

    # Logic Prioritization: Life-threatening first
    if chest_pain or short_breath:
        department = "Emergency / Cardiology"
        advice = "CRITICAL: Potential cardiac or respiratory distress. Immediate ER attention."
    elif bleeding:
        department = "Emergency Room (ER)"
        advice = "CRITICAL: Heavy bleeding. Proceed to ER immediately."
    elif injury:
        department = "Emergency Room (ER) / Trauma"
        advice = "Urgent: Physical injury. Proceed to ER."
    elif high_fever and age < 12:
        department = "Pediatrics"
        advice = "Urgent: High fever in a minor. Visit Pediatrics immediately."
    elif high_fever:
        department = "General Medicine"
        advice = "Fever detected. Consult a general physician."
    elif dizziness:
        department = "Neurology"
        advice = "Neurological symptoms present. Visit Neurology for evaluation."
    elif stomach_pain:
        department = "Gastroenterology"
        advice = "Visit a gastroenterologist for abdominal diagnosis."
    else:
        department = "Outpatient (OPD)"
        advice = "No critical symptoms detected. Please proceed to regular OPD."

    print(f"\n" + "="*25)
    print(f"PATIENT REPORT: {name.upper()}")
    print(f"Age: {age}")
    print(f"Recommended Department: {department}")
    print(f"Action Plan: {advice}")
    print("="*25)


if __name__ == "__main__":
    triage_system()