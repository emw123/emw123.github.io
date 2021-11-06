import random

grammatical_number = random.randint(1,10)


def get_determiner(grammatical_number):
    #grammatical_number = random.randint(1,10)
    global words
    if grammatical_number == 1:
        words = ['the', 'one']
    
    else:
        words = ['some', 'many']
    
    global word
    word = random.choice(words)
    return word
        
def get_noun(grammatical_number):
    global nouns
    if grammatical_number == 1:
        nouns = ['adult', 'bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'women']

    else: 
        nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    global noun
    noun = random.choice(nouns)
    return noun

    

def get_verb(grammatical_number,tense):
    global verb
    global verbs
    if tense == 'past':
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        

    elif tense == 'present' and grammatical_number == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        

    elif tense == 'present' and grammatical_number != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
        

    elif tense == 'future':
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"] 
    
    
    verb = random.choice(verbs)
    return verb

def get_preposition():
    global preposistions
    preposistions = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    global preposistion
    preposistion = random.choice(preposistions)
    return preposistion

def get_prepositional_phrase():
    
    if grammatical_number == 1:
        quantity = 'single'
    if grammatical_number != 1:
        quantity = 'plural'
    get_preposition()
    preposistion = random.choice(preposistions)
    get_determiner(grammatical_number)
    word = random.choice(words)
    get_noun(grammatical_number)
    noun = random.choice(nouns)
    global prepositional_phrase
    prepositional_phrase = (preposistion + ' '  + word + ' ' + noun)

def main(grammatical_number,tense):
    for _ in range(0,6):
        grammatical_number = random.randint(1,10)
        tenses = ['past', 'present', 'future']
        tense = random.choice(tenses)
        get_determiner(grammatical_number)
        get_noun(grammatical_number)
        get_verb(grammatical_number,tense)
        get_preposition()
        get_prepositional_phrase()
        print(f'{word} {noun} {verb}')
    for _ in range(0,6):
        grammatical_number = random.randint(1,10)
        tenses = ['past', 'present', 'future']
        tense = random.choice(tenses)
        get_determiner(grammatical_number)
        get_noun(grammatical_number)
        get_verb(grammatical_number,tense)
        get_preposition()
        get_prepositional_phrase()
        print(f'{word} {noun} {verb} {prepositional_phrase}.')

    
main("grammatical_number","tense")










