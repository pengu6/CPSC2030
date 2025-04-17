from abc import ABC, abstractmethod

# from random import randint, choice
import random
import unittest
from unittest.mock import patch, MagicMock
from typing import List, Type


class Operand:
    """Immutable numeric value container"""

    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return str(self.value)


class ValueGenerator(ABC):
    """Abstract base class for operand value generation"""

    @abstractmethod
    def generate(self) -> int:
        """Generates an integer"""


class RandomValueGenerator(ValueGenerator):
    """ValueGenerator providing random numbers"""

    def generate(self) -> int:
        return random.randint(1, 9)


class FixedValueGenerator(ValueGenerator):
    """ValueGenerator providing specified numbers"""

    def __init__(self, value: int):
        self.value = value

    def generate(self) -> int:
        return self.value


class MathProblem(ABC):
    """Abstract base class representing a math problems

    Problems must implement `display` so they can be shown to a
    user as well as `solution` so user input can be checked.
    """

    @property
    @abstractmethod
    def solution(self) -> int:
        """Returns the solution to this problem"""

    @abstractmethod
    def display(self) -> str:
        """Displays the problem to the user"""


class AdditionProblem(MathProblem):
    """A MathProblem using basic addition"""

    def __init__(self, lhs_gen: ValueGenerator, rhs_gen: ValueGenerator):
        self.lhs = Operand(lhs_gen.generate())
        self.rhs = Operand(rhs_gen.generate())

    @property
    def solution(self) -> int:
        return self.lhs.value + self.rhs.value

    def display(self) -> str:
        return f"{self.rhs} + {self.lhs} ="


class SubtractionProblem(MathProblem):
    """MathProblem using basic subtraction"""

    def __init__(self, lhs_gen: ValueGenerator, rhs_gen: ValueGenerator):
        self.lhs = Operand(lhs_gen.generate())
        self.rhs = Operand(rhs_gen.generate())

    @property
    def solution(self) -> int:
        return self.rhs.value - self.lhs.value

    def display(self) -> str:
        return f"{self.rhs} - {self.lhs} ="


class AnswerChecker(ABC):
    """An abstract base class for checking answers against user input"""

    @abstractmethod
    def check(self, problem: MathProblem) -> bool:
        """Checks a problem using user input

        :return: Boolean that will be True if answered correctly
        """


class CLIAnswerChecker(AnswerChecker):
    """AnswerChecking using the command line interface for input"""

    def check(self, problem: MathProblem) -> bool:
        """Checks for a correct answer by asking on the CLI"""
        answer = input(f"{problem.display()} ")
        return int(answer) == problem.solution


class MathQuiz:
    """Aggregate of MathProblems that produces a score over all problems"""

    def __init__(
        self,
        problem_factories: List[Type[MathProblem]],
        checker: AnswerChecker,
        value_gen: ValueGenerator,
        num_problems: int = 3,
    ):
        self.problems = [
            random.choice(problem_factories)(value_gen, value_gen)
            for _ in range(num_problems)
        ]
        self.checker = checker
        self.results = []

    def run_quiz(self) -> str:
        for problem in self.problems:
            self.results.append(self.checker.check(problem))

        score = sum(self.results)
        return f"Score: {score}/{len(self.problems)}"


class TestRandomValueGenerator(unittest.TestCase):
    def setUp(self):
        self.gen = RandomValueGenerator()

    def test_random_values(self):
        for _ in range(100):
            self.assertTrue(1 <= self.gen.generate() <= 9)

    def test_patched_random(self):
        with patch("random.randint", return_value=7):
            self.assertEqual(7, self.gen.generate())


if __name__ == "__main__":
    # Run tests
    unittest.main(exit=False)

    # Run quiz
    quiz = MathQuiz(
        problem_factories=[AdditionProblem, SubtractionProblem],
        checker=CLIAnswerChecker(),
        value_gen=RandomValueGenerator(),
    )

    # Uncomment to use the quiz
    # print(quiz.run_quiz())