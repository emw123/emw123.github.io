from sentances import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    single_determiners = ['the', 'one']
    global word
    for _ in range(4):
        word = get_determiner(1)

        assert word in single_determiners

    plural_determiners = ['some', 'many']

    for _ in range(4):
        word = get_determiner(2)

        assert word in plural_determiners

def test_get_noun():
    single_nouns = ['adult', 'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'women']

    global noun
    for _ in range(4):
        noun = get_noun(1)

        assert noun in single_nouns

    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    
    for _ in range(4):
        noun = get_noun(2)

        assert noun in plural_nouns

def test_get_verb():

    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    for _ in range(4):
 
        verb = get_verb('tense',1)

        assert verb in past_verbs
        return verb

    present_plural_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        
        verb = get_verb('tense',2)

        assert verb in present_plural_verbs
        return verb
    present_single_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    for _ in range(4):
        verb = get_verb('tense',3)

        assert verb in present_single_verbs
        return verb
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"] 

    for _ in range(4):
        verb = get_verb('tense',4)

        assert verb in future_verbs
        return verb

def test_get_preposition():

    preposistions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    global preposistion
    for _ in range(4):
        preposistion = get_preposition()
        assert preposistion in preposistions

def test_get_prepositional_phrase():

    prepositional_phrases = (preposistion + ' '  + word + ' ' + noun)
    for _ in range(4):
        assert prepositional_phrases in prepositional_phrases

pytest.main(["-v", "--tb=line", "-rN", "test_words.py"])

