import re
from collections import Counter
from typing import Dict, List

def count_word_frequency(text: str, stop_words: List[str], word_bank: List[str]) -> Dict[str, int]:
    """Counts the frequency of each word and two consecutive words in the given text, ignoring non-alphabet characters and stop words."""

    # Use regular expression to find all words consisting of at least two alphabet characters
    words = re.findall(r"\b[a-zA-Z]{2,}\b", text)

    # Adding custom stop words
    custom_stop_words = set(stop_words + word_bank)

    words = [word for word in words if word.lower() not in custom_stop_words]
    word_count = Counter(words)

    # Counting two consecutive words (bigrams)
    bigrams = [
        " ".join(words[i : i + 2])
        for i in range(len(words) - 1)
        if words[i].lower() not in custom_stop_words
        and words[i + 1].lower() not in custom_stop_words
    ]
    word_count.update(bigrams)


    return word_count