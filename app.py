import streamlit as st
import pickle
import string
from nltk.corpus import  stopwords
import nltk
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

def transform_text(Email):
    Email = Email.lower()
    Email = nltk.word_tokenize(Email)

    y = []
    for i in Email:
        if i.isalnum():
            y.append(i)
    Email = y[:]
    y.clear()
    for i in Email:
        if i not in stopwords.words("english") and i not in string.punctuation:
            y.append(i)
    Email = y[:]
    y.clear()
    for i in Email:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter the message")

if st.button('Predict'):
    # 1. Preprocess
    transformed_sms = transform_text((input_sms))
    # 2. Vectorize
    vector_input = tfidf.transform([transformed_sms])
# 3. predict
    result = model.predict(vector_input)[0]
# 4. Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")



