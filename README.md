# 🎯 Guess the Number

A classic number guessing game built in Python. The computer picks a random number and you try to guess it — with hints to guide you closer on each attempt.

## Demo

```
Welcome to Guess the Number!
I'm thinking of a number between 1 and 100.

Enter your guess: 50
Too low! Try again.

Enter your guess: 75
Too high! Try again.

Enter your guess: 63
🎉 Correct! You guessed it in 3 attempts.
```

## Features

- Random number generation within a configurable range
- Higher / lower hints after each guess
- Attempt counter to track your performance
- Input validation — handles non-numeric input gracefully
- Play again option after each round

## Getting Started

### Prerequisites

- Python 3.x

### Installation

```bash
git clone https://github.com/your-username/guess-the-number.git
cd guess-the-number
```

### Run

```bash
python guess_the_number.py
```

No external dependencies — uses Python's built-in `random` module only.

## How to Play

1. Run the script
2. The program picks a secret number between 1 and 100
3. Enter your guess
4. Follow the **Too high** / **Too low** hints
5. Keep guessing until you land on the correct number
6. Your attempt count is shown at the end

## Project Structure

```
guess-the-number/
├── guess_the_number.py   # Main game logic
└── README.md
```

## Configuration

You can change the number range by editing these constants at the top of `guess_the_number.py`:

```python
LOWER_BOUND = 1
UPPER_BOUND = 100
```

## Optimal Strategy

Binary search gets you to any answer in at most **7 guesses** for a 1–100 range. Always guess the midpoint of your remaining range.

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

## License

[MIT](LICENSE)
