from abc import ABC, abstractmethod

class Academic(ABC):
    def __init__(self, subjects, scores):
        self.subjects = subjects
        self.scores = scores

    @abstractmethod
    def average_score(self):
        pass

class DesiredAcademic(Academic):
    def __init__(self, subjects, desired_scores):
        super().__init__(subjects, desired_scores)

    def average_score(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)
