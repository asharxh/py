def fibonacci_fixed():
    a = 0
    b = 1
    term1 = a
    term2 = b
    term3 = a + b
    term4 = b + term3
    term5 = term3 + term4
    term6 = term4 + term5
    term7 = term5 + term6
    term8 = term6 + term7
    term9 = term7 + term8
    term10 = term8 + term9
    print("Fibonacci sequence:")
    print(term1, term2, term3, term4, term5, term6, term7, term8, term9, term10)

fibonacci_fixed()