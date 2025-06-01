from spellchecker import SpellChecker

def get_spellchecker(language):
    try:
        spell = SpellChecker(language=language)
        return spell
    except Exception as e:
        print(f"Error: {e}")
        return None

def correct_word(word, language='en'):
    spell = get_spellchecker(language)
    if not spell:
        return None, []
    
    corrected = spell.correction(word)
    suggestions = spell.candidates(word)
    return corrected, list(suggestions)

# Program starts here
if __name__ == "__main__":
    print("Supported languages: en (English), es (Spanish), de (German), fr (French), pt (Portuguese)")
    lang = input("Enter the language code (e.g., en): ").strip().lower()
    word = input("Enter a word to autocorrect: ").strip()

    corrected, suggestions = correct_word(word, language=lang)

    if corrected:
        print(f"\nOriginal: {word}")
        print(f"Corrected: {corrected}")
        print(f"Suggestions: {suggestions}")
    else:
        print("Language not supported or error occurred.")
