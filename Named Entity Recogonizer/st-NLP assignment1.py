import streamlit as st
import streamlit as st
import spacy
from spacy import displacy
#from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
from pprint import pprint
from newspaper import Article




st.title("Named Entity Recognizer")
st.info("This app will take an input from the user and then prints the named entities")


#-----------------------------------------------

import streamlit as st

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Type: ", ('Paragraph', 'URL'))
 
# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Paragraph'):

    
    text = st.text_area("Enter a paragraph")

    if(st.button("Submit")):
        doc = nlp(text)
        ent_html = displacy.render(doc, style="ent", jupyter=False)
        # Display the entity visualization in the browser:
        st.markdown(ent_html, unsafe_allow_html=True)



else:
    url = st.text_input("Enter URL")
    from newspaper import Article

    if st.button("Submit"):
        article=Article(url)
        article.download()
        article.parse()
        doc=nlp(article.text)
        displacy.render(doc, jupyter=False, style='ent')
        st.markdown(displacy.render(doc,style='ent',jupyter=False),unsafe_allow_html=True)
 


