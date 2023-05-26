class DNAMistake:
    def __init__(self, mistake_type, date, description, evidence_id):
        self.mistake_type = mistake_type
        self.date = date
        self.description = description
        self.evidence_id = evidence_id

    def __str__(self):
        return f"{self.date.strftime('%Y-%m-%d %H:%M:%S')} - Mistake Type: {self.mistake_type}, Evidence ID: {self.evidence_id}, Description: {self.description}"

class DNAMistakeLog:
    def __init__(self):
        self.mistakes = []

    def log_mistake(self, mistake_type, description, evidence_id):
        mistake = DNAMistake(mistake_type, datetime.datetime.now(), description, evidence_id)
        self.mistakes.append(mistake)
        print(f"Mistake logged for Evidence ID {evidence_id}.")

    def get_mistakes_by_type(self, mistake_type):
        return [str(mistake) for mistake in self.mistakes if mistake.mistake_type == mistake_type]

# Sample usage
if __name__ == "__main__":
    dna_mistake_log = DNAMistakeLog()

    dna_mistake_log.log_mistake("Falsely read", "DNA sample was misread due to lab error.", "EVID12345")
    dna_mistake_log.log_mistake("Switched", "DNA samples were switched during transport.", "EVID67890")
    dna_mistake_log.log_mistake("Sealed in higher directory", "DNA sample was sealed in incorrect directory.", "EVID11223")

    falsely_read_mistakes = dna_mistake_log.get_mistakes_by_type("Falsely read")

    print("Falsely read mistakes:")
    for mistake in falsely_read_mistakes:
        print(mistake)
