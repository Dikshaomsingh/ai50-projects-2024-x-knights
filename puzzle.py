from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
ASays0=  Symbol("I am both a knight and a knave.")
knowledge0 = And(
    # TODO
    Or(AKnight,AKnave),
    Not(And(AKnight,AKnave)),
    Biconditional(ASays0,And(AKnight,AKnave)),
    Biconditional(AKnight,ASays0),
    Biconditional(AKnave,(Not(ASays0)))
)

# Puzzle 1
ASays1 = Symbol("We are both knaves.")
# B says nothing.
knowledge1 = And(
    # TODO
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Biconditional(ASays1,And(AKnave,BKnave)),
    Biconditional(And(AKnave,BKnight),(Not(ASays1))),
    Biconditional(And(AKnight,BKnave),ASays1)
)

# Puzzle 2
ASays2 = Symbol("We are the same kind.")
BSays2 = Symbol("We are of different kinds.")
knowledge2 = And(
    # TODO
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Biconditional(ASays2,Or(And(AKnave,BKnave),And(AKnight,BKnight))),
    Biconditional(BSays2,Or(And(AKnave,BKnight),And(AKnight,BKnave))),
    Biconditional(And(AKnight,BKnight),ASays2),
    Biconditional(And(BKnight,AKnave),BSays2),
    Biconditional(And(AKnave,BKnight),Not(ASays2)),
    Biconditional(And(AKnave,BKnave),Not(BSays2))
)

# Puzzle 3
ASays3 = Symbol("either I am a knight. or I am a knave. but you don't know which.")
BSays3 = Symbol("A said 'I am a knave'. and C is a knave.")
# B says "C is a knave."
CSays3 = Symbol("A is a knight.")
knowledge3 = And(
    # TODO
    Or(AKnight,AKnave),
    Or(BKnight,BKnave),
    Or(CKnight,CKnave),
    Not(And(AKnight,AKnave)),
    Not(And(BKnight,BKnave)),
    Not(And(CKnight,CKnave)),
    Biconditional(ASays3,Or(AKnave,AKnight)),
    Biconditional(BSays3,And(AKnave,CKnave)),
    Biconditional(CSays3,AKnight),
    Biconditional(And(AKnight,CKnight,BKnave),ASays3),
    Biconditional(And(AKnave,BKnight,CKnave),BSays3),
    Biconditional(And(AKnight,CKnight,BKnave),CSays3),
    Biconditional(And(BKnight,CKnave,AKnave),Not(ASays3)),
    Biconditional(And(AKnight,BKnave,CKnight),Not(BSays3)),
    Biconditional(And(AKnave,BKnight,CKnave),Not(CSays3))
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
