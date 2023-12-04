'''
Name- Shreyash Jeughale 
Roll no- 30
Batch- B2
Practical no.6 -Implement Dependency Parsing of textual input using spacy library.
'''
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

multiline_text = """
Rain tapped gently on the window pane.
Lost keys, frantic search, relieved smile.
Cat curled up, purring softly.
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")


'''
******************    OUTPUT      *************************
TOKEN: 

=====
token.tag_ = '_SP'
token.head.text = 'Rain'
token.dep_ = 'dep'

TOKEN: Rain
=====
token.tag_ = 'NNP'
token.head.text = 'tapped'
token.dep_ = 'nsubj'

TOKEN: tapped
=====
token.tag_ = 'VBD'
token.head.text = 'tapped'
token.dep_ = 'ROOT'

TOKEN: gently
=====
token.tag_ = 'RB'
token.head.text = 'tapped'
token.dep_ = 'advmod'

TOKEN: on
=====
token.tag_ = 'IN'
token.head.text = 'tapped'
token.dep_ = 'prep'

TOKEN: the
=====
token.tag_ = 'DT'
token.head.text = 'pane'
token.dep_ = 'det'

TOKEN: window
=====
token.tag_ = 'NN'
token.head.text = 'pane'
token.dep_ = 'compound'

TOKEN: pane
=====
token.tag_ = 'NN'
token.head.text = 'on'
token.dep_ = 'pobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'tapped'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

TOKEN: Lost
=====
token.tag_ = 'VBN'
token.head.text = 'keys'
token.dep_ = 'amod'

TOKEN: keys
=====
token.tag_ = 'NNS'
token.head.text = 'keys'
token.dep_ = 'ROOT'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'keys'
token.dep_ = 'punct'

TOKEN: frantic
=====
token.tag_ = 'JJ'
token.head.text = 'search'
token.dep_ = 'amod'

TOKEN: search
=====
token.tag_ = 'NN'
token.head.text = 'smile'
token.dep_ = 'nmod'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'search'
token.dep_ = 'punct'

TOKEN: relieved
=====
token.tag_ = 'JJ'
token.head.text = 'smile'
token.dep_ = 'amod'

TOKEN: smile
=====
token.tag_ = 'NN'
token.head.text = 'keys'
token.dep_ = 'conj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'smile'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

TOKEN: Cat
=====
token.tag_ = 'NNP'
token.head.text = 'curled'
token.dep_ = 'nsubj'

TOKEN: curled
=====
token.tag_ = 'VBD'
token.head.text = 'curled'
token.dep_ = 'ROOT'

TOKEN: up
=====
token.tag_ = 'RP'
token.head.text = 'curled'
token.dep_ = 'prt'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'curled'
token.dep_ = 'punct'

TOKEN: purring
=====
token.tag_ = 'VBG'
token.head.text = 'curled'
token.dep_ = 'advcl'

TOKEN: softly
=====
token.tag_ = 'RB'
token.head.text = 'purring'
token.dep_ = 'advmod'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'curled'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

'''