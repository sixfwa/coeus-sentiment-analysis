from textblob import TextBlob

def analyse(text):
    testimonial = TextBlob(text)
    return testimonial.sentiment

def polarity(text):
    pol = analyse(text)[0]
    return pol

def subjectivity(text):
    sub = analyse(text)[1]
    return sub 


# 0.9 < subjectivity <= 1 -> very subjective
# 0.65 < subjectivity <= 0.9 -> subjective
# 0.55 < subjectivity <= 0.65 -> somewhat subjective
# 0.45 < subjectivity <= 0.55 -> neutral
# 0.35 < subjectivity <= 0.45 -> somewhat objective
# 0.1 < subjectivity <= 0.35 -> objective
# 0 <= subjectivity <= 0.1 -> very objective

def subjectivity_statement(text):
    sub = subjectivity(text)
    statement = "The text submitted is "
    if (sub > 0.9 and sub <= 1):
        statement += "very subjective."
    elif (sub > 0.65 and sub <= 0.9):
        statement += "subjective."
    elif (sub > 0.55 and sub <= 0.65):
        statement += "somewhat subjective."
    elif (sub > 0.45 and sub <= 0.55):
        statement += "neutral. It is neither subjective nor objective."
    elif (sub > 0.35 and sub <= 0.45):
        statement += "somewhat objective."
    elif (sub > 0.1 and sub <= 0.35):
        statement += "objective."
    else:
        statement += "very objective."

    return statement

# 0.75 < polarity <= 1 -> very positive
# 0.5 < polarity <= 0.75 -> positive
# 0.25 < polarity <= 0.5 -> somewhat positive
# -0.25 < polarity <= 0.25 -> neutral
# -0.5 < polarity <= -0.25 -> somewhat negative
# -0.75 < polarity <= -0.5 -> negative
# -1 <= polarity <= -0.75 -> very negative

def polarity_statement(text):
    pol = polarity(text)
    statement = "The text submitted is "
    if (pol > 0.75 and pol <= 1):
        statement += "very positive."
    elif (pol > 0.5 and pol <= 0.75):
        statement += "positive."
    elif (pol > 0.25 and pol <= 0.5):
        statement += "somewhat positive."
    elif (pol > -0.25 and pol <= 0.25):
        statement += "neutral."
    elif (pol > -0.5 and pol <= -0.25):
        statment += "somewhat negative."
    elif (pol > -0.75 and pol <= -0.5):
        statement += "negative."
    elif (pol >= -1 and pol <= -0.75):
        statement += "very negative."
    
    return statement