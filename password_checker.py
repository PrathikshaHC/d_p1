# ============================================================
#   [*] Password Strength Checker
#   DecodeLabs | Cyber Security Project 1
#   Industrial Training Kit | Batch: 2026
# ============================================================

import re
import sys

# Fix Windows terminal encoding
sys.stdout.reconfigure(encoding='utf-8')

# ── Common/leaked passwords list ──────────────────────────────
COMMON_PASSWORDS = [
    "password", "123456", "123456789", "qwerty", "abc123",
    "password1", "iloveyou", "admin", "letmein", "welcome",
    "monkey", "dragon", "master", "sunshine", "princess",
    "shadow", "superman", "michael", "football", "pass123"
]

# ── Banner ────────────────────────────────────────────────────
def show_banner():
    print("=" * 50)
    print("   🔐 PASSWORD STRENGTH CHECKER")
    print("   DecodeLabs | Cyber Security Project 1")
    print("=" * 50)

# ── Check functions ───────────────────────────────────────────
def check_length(password):
    """Returns a score based on password length."""
    length = len(password)
    if length >= 12:
        return 2   # Strong length
    elif length >= 8:
        return 1   # Medium length
    else:
        return 0   # Too short

def has_uppercase(password):
    """Returns True if password contains at least one uppercase letter."""
    return bool(re.search(r'[A-Z]', password))

def has_lowercase(password):
    """Returns True if password contains at least one lowercase letter."""
    return bool(re.search(r'[a-z]', password))

def has_numbers(password):
    """Returns True if password contains at least one digit."""
    return bool(re.search(r'[0-9]', password))

def has_symbols(password):
    """Returns True if password contains at least one special symbol."""
    return bool(re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?/`~\\"\']', password))

def is_common(password):
    """Returns True if password is in the common/leaked passwords list."""
    return password.lower() in COMMON_PASSWORDS

# ── Core strength evaluator ───────────────────────────────────
def evaluate_strength(password):
    """
    Evaluates password strength and returns:
    - strength level  : 'Weak', 'Medium', or 'Strong'
    - score           : numeric score out of 6
    - feedback list   : tips to improve the password
    """
    score = 0
    feedback = []

    # 1. Check if it's a common/leaked password
    if is_common(password):
        return "Weak", 0, ["❌ This is a very common/leaked password. Never use it!"]

    # 2. Length check
    length_score = check_length(password)
    score += length_score
    if length_score == 0:
        feedback.append("❌ Password is too short. Use at least 8 characters.")
    elif length_score == 1:
        feedback.append("⚠️  Password length is okay, but 12+ characters is stronger.")

    # 3. Uppercase check
    if has_uppercase(password):
        score += 1
    else:
        feedback.append("❌ Add at least one UPPERCASE letter (A-Z).")

    # 4. Lowercase check
    if has_lowercase(password):
        score += 1
    else:
        feedback.append("❌ Add at least one lowercase letter (a-z).")

    # 5. Number check
    if has_numbers(password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # 6. Symbol check
    if has_symbols(password):
        score += 1
    else:
        feedback.append("❌ Add at least one special symbol (!@#$%^&* etc.).")

    # ── Determine strength level based on score ──
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    if not feedback:
        feedback.append("✅ Great password! Keep it safe and never share it.")

    return strength, score, feedback

# ── Display result ────────────────────────────────────────────
def display_result(password, strength, score, feedback):
    print("\n" + "-" * 50)
    print(f"  Password  : {'*' * len(password)}")
    print(f"  Length    : {len(password)} characters")
    print(f"  Score     : {score} / 6")

    # Strength badge with color-coded label
    if strength == "Weak":
        badge = "🔴 WEAK"
    elif strength == "Medium":
        badge = "🟡 MEDIUM"
    else:
        badge = "🟢 STRONG"

    print(f"  Strength  : {badge}")
    print("-" * 50)
    print("  📋 Feedback:")
    for tip in feedback:
        print(f"     {tip}")
    print("-" * 50)

# ── Strength meter ────────────────────────────────────────────
def strength_meter(score):
    """Displays a visual strength meter."""
    filled = "█" * score
    empty  = "░" * (6 - score)
    print(f"\n  Strength Meter: [{filled}{empty}] {score}/6\n")

# ── Main loop ─────────────────────────────────────────────────
def main():
    show_banner()
    print("\nType 'quit' to exit the program.\n")

    while True:
        password = input("  Enter a password to check: ")

        if password.lower() == "quit":
            print("\n  👋 Exiting Password Checker. Stay secure!\n")
            break

        if not password.strip():
            print("  ⚠️  Please enter a valid password.\n")
            continue

        strength, score, feedback = evaluate_strength(password)
        display_result(password, strength, score, feedback)
        strength_meter(score)

        again = input("  Check another password? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("\n  👋 Exiting Password Checker. Stay secure!\n")
            break
        print()

# ── Entry point ───────────────────────────────────────────────
if __name__ == "__main__":
    main()
