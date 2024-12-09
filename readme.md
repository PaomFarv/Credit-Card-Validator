
# Credit Card Validator

A Python-based credit card number validation tool that utilizes the **Luhn algorithm** to verify the validity of credit card numbers. The program ensures input is clean and correctly formatted before performing the validation process.

---

## Features

- Supports credit card number inputs with spaces or dashes.
- Implements the Luhn algorithm to check the validity of the credit card.
- Provides real-time feedback for invalid inputs.
- Offers a simple and efficient solution for credit card verification.

---

## Requirements

- **Python 3.x**
- No additional libraries are required.

---

## How It Works

1. The user inputs a credit card number (with or without spaces or dashes).
2. The program cleans the input to remove unnecessary characters.
3. The credit card number is reversed and processed using the Luhn algorithm:
   - Every second digit from the right is doubled.
   - If doubling results in a number greater than 9, 9 is subtracted.
   - All digits are summed up.
4. The program checks if the total is divisible by 10:
   - If divisible, the card number is valid.
   - Otherwise, it is invalid.

---

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/paomfarv/credit-card-validator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd credit-card-validator
   ```
3. Run the script:
   ```bash
   python credit_card_validator.py
   ```

4. Follow the prompts to enter a credit card number.

---

## Example

```plaintext
-----------Credit-Card-Number-Validator------------
Insert the Credit Card Number: 4539-1488-0343-6467
Checking---
It's a valid credit card number.
---------------------------------------------------
```

---

## Contribution

Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements or additional features.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
