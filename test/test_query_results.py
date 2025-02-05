import pytest
import sys
import os
from langchain_ollama import OllamaLLM
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.query import query
from langchain_ollama import OllamaLLM


EVAL_PROMPT = """
Expected Response: {expected_response}
Actual Response: {actual_response}
---
(Answer with 'true' or 'false') Does the actual response match the expected response? 
"""

@pytest.fixture
def model():
    return OllamaLLM(model="mistral")

def test_monopoly_rules(model):
    assert query_and_validate(
        model = model,
        question="How much total money does a player start with in Monopoly? (Answer with the number only)",
        expected_response="$1500",
    )

def test_ticket_to_ride_rules(model):
    assert query_and_validate(
        model = model,
        question="How many points does the longest continuous train get in Ticket to Ride? (Answer with the number only)",
        expected_response="10 points",
    )

def test_uno_rules(model):
    assert query_and_validate(
        model = model,
        question="What happens when a player has only one card left in Uno?",
        expected_response="If a player has only one card left in Uno, they must say 'UNO' before playing their next to last card. If they fail to do so and another player catches them with just one card before the next player begins their turn, the player who forgot to say 'UNO' must pick four more cards from the DRAW pile",
    )

def test_exploding_kittens_rules(model):
    assert query_and_validate(
        model = model,
        question="How many cards are dealt to each player at the start of the game in exploding kittens? (Answer with the number only)",
        expected_response="7 cards",
    )

def test_werewolves_rules(model):
    assert query_and_validate(
        model = model,
        question="In Werewolves, What is the objective of the Werewolves in the game?",
        expected_response="They secretly eliminate all the Villagers or reduce their numbers enough so that the Werewolves can outvote the remaining players during the Day phase. The Werewolves aim to blend in and avoid being identified while secretly working together to eliminate Villagers one by one.",
    )

def test_bang_rules(model):
    assert query_and_validate(
        model = model,
        question="Can players reveal their identity at any time in Bang!? (Just need to answer 'Yes' or 'No')",
        expected_response="No",
    )

def query_and_validate(model: OllamaLLM, question: str, expected_response: str) -> bool:
    response_text = query(question)
    prompt = EVAL_PROMPT.format(
        expected_response=expected_response, actual_response=response_text
    )

    evaluation_results_str = model.invoke(prompt)
    evaluation_results_str_cleaned = evaluation_results_str.strip().lower()

    if "true" in evaluation_results_str_cleaned:
        return True
    elif "false" in evaluation_results_str_cleaned:
        return False
    else:
        raise ValueError(
            f"Invalid evaluation result. Cannot determine if 'true' or 'false'."
        )