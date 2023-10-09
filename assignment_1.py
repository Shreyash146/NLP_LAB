'''
Name : Shreyash Jeughale
Roll No: 30
Assignment No :01
Title: Text Processing using Spacy Library ,Tokenization, Stop Words, Lemmitization, POS tagging        
'''

# importing libs
import spacy

# loading model for english language
nlp = spacy.load("en_core_web_sm")

# input
inp=(
 "The Indian Navy is a multi-dimensional force that has been organized to safeguard India's maritime territorial integrity and other maritime interests. It is headed by the Chief of the Naval Staff or the CNS. He is of the rank of Admiral and has his headquarters at New Delhi."
)

print("Input: ",inp,"\n\nApplying NLP Operations")
# passing inp to english model
passedtxt=nlp(inp)

# Operation 1 : Tokenization 
print("\n\nOperation 1: Tokenization\n")
for token in passedtxt:
    print(token,token.idx)



#Operation 2: Stop Words
print("\n\nOperation 2: Stop Words\n")

# loading stopwords using spacy library
spacy_stopwords = spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)

# for stop_word in list(spacy_stopwords)[:10]:
#     print(stop_word)

print("\nPrinting stop words:\n",[token for token in passedtxt if not token.is_stop]) #actual stop words



#Operation 3: Lemmitization
print("\n\nOperation 3: Lemmitization\n")
for token in passedtxt:
    # using lemma_ to identify the lemma of particular word that have actual dicitionary meaning
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")


#Operation 3: Part of Speech Tagging
print("\n\nOperation 4: Part of Speech Tagging\n")
# using tag_ from spacy to tag Part of Speech and pos_ for identifying type of Part of Speech
for token in passedtxt:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}   
EXPLANATION: {spacy.explain(token.tag_)}"""    
    )        



'''
Applying NLP Operations


Operation 1: Tokenization

The 0
Indian 4
Navy 11
is 16
a 19
multi 21
- 26
dimensional 27
force 39
that 45
has 50
been 54
organized 59
to 69
safeguard 72
India 82
's 87
maritime 90
territorial 99
integrity 111
and 121
other 125
maritime 131
interests 140
. 149
It 151
is 154
headed 157
by 164
the 167
Chief 171
of 177
the 180
Naval 184
Staff 190
or 196
the 199
CNS 203
. 206
He 208
is 211
of 214
the 217
rank 221
of 226
Admiral 229
and 237
has 241
his 245
headquarters 249
at 262
New 265
Delhi 269
. 274


Operation 2: Stop Words


Printing stop words:
 [Indian, Navy, multi, -, dimensional, force, organized, safeguard, India, maritime, territorial, integrity, maritime, interests, ., headed, Chief, Naval, Staff, CNS, ., rank, Admiral, headquarters, New, Delhi, .]


Operation 3: Lemmitization

                 The : the
                  is : be
                 has : have
                been : be
           organized : organize
           interests : interest
                  It : it
                  is : be
              headed : head
                  He : he
                  is : be
                 has : have


Operation 4: Part of Speech Tagging


TOKEN: The
=====
TAG: DT         POS: DET   
EXPLANATION: determiner

TOKEN: Indian
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: Navy
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: is
=====
TAG: VBZ        POS: AUX   
EXPLANATION: verb, 3rd person singular present

TOKEN: a
=====
TAG: DT         POS: DET   
EXPLANATION: determiner

TOKEN: multi
=====
TAG: JJ         POS: ADJ   
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: -
=====
TAG: JJ         POS: ADJ   
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: dimensional
=====
TAG: JJ         POS: ADJ   
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: force
=====
TAG: NN         POS: NOUN   
EXPLANATION: noun, singular or mass

TOKEN: that
=====
TAG: WDT        POS: PRON   
EXPLANATION: wh-determiner

TOKEN: has
=====
TAG: VBZ        POS: AUX   
EXPLANATION: verb, 3rd person singular present

TOKEN: been
=====
TAG: VBN        POS: AUX   
EXPLANATION: verb, past participle

TOKEN: organized
=====
TAG: VBN        POS: VERB   
EXPLANATION: verb, past participle

TOKEN: to
=====
TAG: TO         POS: PART   
EXPLANATION: infinitival "to"

TOKEN: safeguard
=====
TAG: VB         POS: VERB   
EXPLANATION: verb, base form

TOKEN: India
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: 's
=====
TAG: POS        POS: PART   
EXPLANATION: possessive ending

TOKEN: maritime
=====
TAG: JJ         POS: ADJ   
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: territorial
=====
TAG: JJ         POS: ADJ   
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: integrity
=====
TAG: NN         POS: NOUN   
EXPLANATION: noun, singular or mass

TOKEN: and
=====
TAG: CC         POS: CCONJ   
EXPLANATION: conjunction, coordinating

TOKEN: other
=====
TAG: JJ         POS: ADJ   
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: maritime
=====
TAG: JJ         POS: ADJ   
EXPLANATION: adjective (English), other noun-modifier (Chinese)

TOKEN: interests
=====
TAG: NNS        POS: NOUN   
EXPLANATION: noun, plural

TOKEN: .
=====
TAG: .          POS: PUNCT   
EXPLANATION: punctuation mark, sentence closer

TOKEN: It
=====
TAG: PRP        POS: PRON   
EXPLANATION: pronoun, personal

TOKEN: is
=====
TAG: VBZ        POS: AUX   
EXPLANATION: verb, 3rd person singular present

TOKEN: headed
=====
TAG: VBN        POS: VERB   
EXPLANATION: verb, past participle

TOKEN: by
=====
TAG: IN         POS: ADP   
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET   
EXPLANATION: determiner

TOKEN: Chief
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: of
=====
TAG: IN         POS: ADP   
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET   
EXPLANATION: determiner

TOKEN: Naval
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: Staff
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: or
=====
TAG: CC         POS: CCONJ   
EXPLANATION: conjunction, coordinating

TOKEN: the
=====
TAG: DT         POS: DET   
EXPLANATION: determiner

TOKEN: CNS
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: .
=====
TAG: .          POS: PUNCT   
EXPLANATION: punctuation mark, sentence closer

TOKEN: He
=====
TAG: PRP        POS: PRON   
EXPLANATION: pronoun, personal

TOKEN: is
=====
TAG: VBZ        POS: AUX   
EXPLANATION: verb, 3rd person singular present

TOKEN: of
=====
TAG: IN         POS: ADP   
EXPLANATION: conjunction, subordinating or preposition

TOKEN: the
=====
TAG: DT         POS: DET   
EXPLANATION: determiner

TOKEN: rank
=====
TAG: NN         POS: NOUN   
EXPLANATION: noun, singular or mass

TOKEN: of
=====
TAG: IN         POS: ADP   
EXPLANATION: conjunction, subordinating or preposition

TOKEN: Admiral
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: and
=====
TAG: CC         POS: CCONJ   
EXPLANATION: conjunction, coordinating

TOKEN: has
=====
TAG: VBZ        POS: VERB   
EXPLANATION: verb, 3rd person singular present

TOKEN: his
=====
TAG: PRP$       POS: PRON   
EXPLANATION: pronoun, possessive

TOKEN: headquarters
=====
TAG: NN         POS: NOUN   
EXPLANATION: noun, singular or mass

TOKEN: at
=====
TAG: IN         POS: ADP   
EXPLANATION: conjunction, subordinating or preposition

TOKEN: New
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: Delhi
=====
TAG: NNP        POS: PROPN   
EXPLANATION: noun, proper singular

TOKEN: .
=====
TAG: .          POS: PUNCT   
EXPLANATION: punctuation mark, sentence closer
'''
