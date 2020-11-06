from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # Background
    Or(AKnight, AKnave),
    # Sentence - A says "I am both a knight and a knave."

    # If A is both Knight and knave (A is telling the truth), then A is night.
    Implication(And(AKnight, AKnave), AKnight),
    # If A is not Knight and knave (A is lying), then A is nave.
    Implication(Not(And(AKnight, AKnave)), AKnave)
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # Background
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # Sentence - A says "We are both knaves."
    # If A and B are not both knaves (A is lying), then A is nave.
    Implication(Not(And(AKnave, BKnave)), AKnave),
    # If A is nave and they are not of the same type, then B is night.
    Implication(AKnave, BKnight)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Background
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),

    # Sentence - A says "We are the same kind."
    # If A and B are not same kind, in this case night (A is lying), then A is nave.
    Implication(Not(And(AKnight, BKnight)), AKnave),
    # If A and B are not same kind, in this case nave (A is lying), then A is nave.
    Implication(Not(And(AKnave, BKnave)), AKnave),

    # Sentence - B says "We are of different kinds."
    # If A is nave and they are not same kind, B is night.
    # B is telling the truth on sentence "We are of different kinds."
    Implication(AKnave, BKnight)
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # Background
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    # Sentence - A says either "I am a knight." or "I am a knave.", but you don't know which.
    # If A is knight or nave (it is telling the truth), then A is knight
    Implication(Or(AKnight, AKnave), AKnight),

    # Sentence - C says "A is a knight."
    # If A is night, then C is telling the truth, means that C is night.
    Implication(AKnight, CKnight),

    # Sentence - B says "C is a knave."
    # If C is night, then B is lying, means that B is nave.
    Implication(CKnight, BKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
