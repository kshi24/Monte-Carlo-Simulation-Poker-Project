# Monte Carlo Poker Advisor

## Overview

This project is a command-line helper for no-limit Texas Hold'em players. It runs thousands of Monte Carlo simulations to estimate your equity in real time, then combines those results with bankroll-aware betting advice so you can decide whether to bet, raise, call, or fold during every street of a hand.

The program guides you through each betting round (pre-flop, flop, turn, river), asking for the cards you see and the current pot size. After each update it simulates the remaining cards against your chosen number of opponents, prints your estimated win probability, and offers betting guidance based on the Kelly Criterion and pot-odds analysis.

## Features

- 🎲 **Monte Carlo equity simulation** using a full 52-card deck with collision checks for known cards.
- 🧠 **Advisory engine** that sizes bets with a street-aware Kelly discount and evaluates maximum profitable calls.
- 🂡 **Complete hand evaluator** capable of ranking all poker hands, including edge cases like ace-low straights and multi-way full houses.
- 🛠️ **Modular architecture** so components such as the simulator, advisor, and hand evaluator can be reused in other projects or tested independently.
- 📈 **Progress feedback** every 1,000 simulations plus a final win-rate summary.

## Project Structure

```
Monte-Carlo-Simulation-Poker-Project-5/
├── advisor.py         # Betting recommendations (Kelly Criterion, pot odds)
├── card.py            # Card data model and string parsing helpers
├── hand.py            # Poker hand ranking and comparison logic
├── hand_helper.py     # Utility functions used by the hand evaluator
├── probability.py     # Deck generation and Monte Carlo engine
├── poker_game.py      # Interactive CLI flow for each betting round
├── main.py            # Entry point that starts the game loop
├── test.py            # Lightweight regression and sanity tests
└── README.md          # Project documentation
```

## Requirements

- Python 3.9 or newer (developed and tested with Python 3.10)
- No third-party dependencies

Creating a virtual environment is optional but recommended for isolating tooling:

```bash
python3 -m venv .venv
source .venv/bin/activate  # macOS / Linux
```

## Running the Interactive Advisor

Launch the CLI helper from the project root:

```bash
python main.py
```

You'll be prompted for:

1. Your initial bankroll.
2. Number of opponents (1–22 supported).
3. Pot size and visible cards at each street.

After every input stage the program reports:

- Estimated win probability (based on 10,000 simulations by default).
- Recommended bet size (if you have the betting lead).
- Maximum call size and guidance when facing a bet.

### Example Session

```
Welcome to the poker computer program...
How much money did you bring to the table?
500
How many opponents do you have
2

___________NEW ROUND____________
What's the current pot size? (antes/blinds)
15
First hole card?
Ace of Spades
Second hole card?
Ace of Hearts

✅ ADVICE: Bet/Raise $13.45
	(Win probability: 82.4%)
If facing a bet:
	- Call $7.50 ✓ (half-pot sized bet)
```

## Adjusting Simulation Settings

The simulator runs 10,000 iterations per street. For faster experimentation (for example during testing or on lower-powered hardware) you can pass a custom `sim_runs` value when calling `Probability.monte_carlo` directly, or modify the default in `probability.py`.

```python
from card import Card
from probability import Probability

hand = [Card(14, "Spades"), Card(14, "Hearts")]
win_rate = Probability.monte_carlo(hand, opps=3, sim_runs=5000)
print(win_rate)
```

## Running the Test Suite

The `test.py` module exercises key components including the advisor logic, hand evaluator, and probability engine. Run it with:

```bash
python test.py
```

Monte Carlo tests in `test.py` default to 1,000 iterations to keep runtime short while still validating typical win-rate ranges.

## How It Works

1. **Input collection:** `poker_game.py` gathers your hole cards, community cards, pot size, and opponent count as the hand progresses.
2. **Deck construction:** `probability.py` builds a fresh deck, removing any known cards before each simulation.
3. **Monte Carlo loop:** For every iteration it deals the remaining board cards plus random opponent hands, ranks each showdown, and increments a win counter if you hold the best hand.
4. **Hand ranking:** `hand.py` evaluates seven-card combinations, detecting all standard poker hands and breaking ties lexicographically.
5. **Advisory output:** `advisor.py` turns the resulting equity into betting and calling recommendations, adjusting aggressiveness based on the street and number of opponents.

## Contributing & Next Steps

Ideas for future improvements:

- Add command-line flags to control simulation count and verbosity without editing source files.
- Track bankroll changes across rounds and surface risk warnings when Kelly-sized bets exceed remaining chips.
- Support weighted opponent ranges instead of purely random cards to model tighter or looser tables.
- Bundle a lightweight GUI or web interface for faster card entry during live play.

Contributions are welcome—open an issue describing the enhancement or bug fix you'd like to tackle, then submit a pull request with your changes and accompanying tests.

Enjoy sharper poker decisions powered by data-driven simulations!