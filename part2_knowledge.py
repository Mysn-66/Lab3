from logic import Symbol, Not, And, Or, Implication, KB, check_all

# ============================================================
# STEP 1: Define Symbols
# ============================================================

sara_key = Symbol("SaraHasKey")
lina_key = Symbol("LinaHasKey")
lina_seen = Symbol("LinaSeenNearRoom")
lina_guilty = Symbol("LinaIsGuilty")

# 🆕 Nora
nora_key = Symbol("NoraHasKey")
nora_guilty = Symbol("NoraIsGuilty")

# All symbols
all_symbols = [
    "SaraHasKey",
    "LinaHasKey",
    "LinaSeenNearRoom",
    "LinaIsGuilty",
    "NoraHasKey",
    "NoraIsGuilty"
]

# ============================================================
# STEP 2: Build Knowledge Base
# ============================================================

kb = KB()

# Clue 1: If Lina has a key → Lina is guilty
kb.tell(Implication(lina_key, lina_guilty))

# Clue 2: Sara does NOT have a key
kb.tell(Not(sara_key))

# Clue 3: Lina was seen near the room
#kb.tell(lina_seen)

# Clue 4: If Lina was seen → Lina has a key
kb.tell(Implication(lina_seen, lina_key))

# 🆕 Nora has a key
kb.tell(nora_key)

# ============================================================
# STEP 3: Ask Questions
# ============================================================

print("=" * 50)
print("CS3081 Lab 3 -- Knowledge Base Detective")
print("=" * 50)

# Lina guilty?
answer = check_all(kb, lina_guilty, all_symbols)
print("\nQuery: Is Lina guilty?")
if answer:
    print("YES -- The KB ENTAILS that Lina is guilty.")
else:
    print("NO -- The KB does NOT entail that Lina is guilty.")

# Sara has key?
answer2 = check_all(kb, sara_key, all_symbols)
print("\nQuery: Does Sara have a key?")
if answer2:
    print("YES -- The KB entails Sara has a key.")
else:
    print("NO -- The KB does NOT entail Sara has a key.")

# 🆕 Nora guilty?
answer3 = check_all(kb, nora_guilty, all_symbols)
print("\nQuery: Is Nora guilty?")
print(answer3)