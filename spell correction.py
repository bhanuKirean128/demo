from textblob import TextBlob

# Function to correct spelling
def correct_spelling(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return str(corrected_text)

# Input text with spelling errors
text_with_errors = "isht is ym naem."
print("Original Text:", text_with_errors)

# Correcting the spelling
corrected_text = correct_spelling(text_with_errors)
print("Corrected Text:", corrected_text)
