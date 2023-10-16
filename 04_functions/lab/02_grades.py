def grade_in_words(grade_score: float) -> str:
    if 2.00 <= grade_score <= 2.99:
        return "Fail"
    elif 3.00 <= grade_score <= 3.49:
        return "Poor"
    elif 3.50 <= grade_score <= 4.49:
        return "Good"
    elif 4.50 <= grade_score <= 5.49:
        return "Very Good"
    elif 5.50 <= grade_score <= 6.00:
        return "Excellent"
    else:
        return "Invalid input"


grade_score_input = float(input())
print(grade_in_words(grade_score=grade_score_input))
