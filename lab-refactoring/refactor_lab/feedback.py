def feedback_codemaker(pattern_maker, pattern_breaker):
    feedback = []

    for i in range(4):

        if pattern_breaker[i] == pattern_maker[i]:
            feedback.append('black')

        elif pattern_breaker[i] in pattern_maker:
            feedback.append('white')

        else:
            feedback.append(' - ')

    return sorted(feedback)