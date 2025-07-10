class QAAgent:
    def __init__(self, plagiarism_checker, readability_checker, seo_checker):
        self.plagiarism = plagiarism_checker
        self.readability = readability_checker
        self.seo = seo_checker

    def run_checks(self, content):
        return {
            "plagiarism": self.plagiarism.check(content),
            "readability": self.readability.check(content),
            "seo": self.seo.audit(content)
        }
