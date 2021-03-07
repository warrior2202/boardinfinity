from flask import Flask,url_for,render_template,request
import spacy
from spacy import displacy
from mediawiki import MediaWiki
nlp = spacy.load('en_core_web_md')
import json
import wikipedia
import streamlit as st 
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('en')

wikipedia1 = MediaWiki()




HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""



# def analyze_text(text):
# 	return nlp(text)

def index():
    st.title("Intern Project")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Intern Project ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Wiki = st.text_input("wiki","Type Here")
    if st.button("Only summarry to NER"):
        extract(Wiki)
    elif st.button("Entire Text to NER"):
        extract2(Wiki)
        
	



def extract(wiki):
    raw_test2 = wiki_wiki.page(wiki)
    if(raw_test2.exists):
        docx = nlp(raw_test2.summary)
        html = displacy.render(docx, style="ent")
        html = html.replace("\n", " ")
        st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
    #    visualize_ner(docx, labels=nlp.get_pipe("ner").labels)
    else:
        index()

# Newlines seem to mess with the rendering
        
        


def extract2(wiki):
    raw_test2 = wiki_wiki.page(wiki)
    if(raw_test2.exists):
            docx = nlp(raw_test2.text)
            html = displacy.render(docx, style="ent")
            html = html.replace("\n", " ")
            st.write(HTML_WRAPPER.format(html), unsafe_allow_html=True)
    else:
            index()
if __name__ == '__main__':
	index()




       
           
