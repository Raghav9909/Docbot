#!/usr/bin/env python
# coding: utf-8

# In[1]:


#IMPORT THE MODULES
import nltk
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings('ignore')


# In[2]:


#DATA 

data = '''
COVID-19 is the disease caused by a new coronavirus called Severe Acute Respiratory Syndrome Coronavirus-2 (SARS-CoV-2).


Sypmtoms
The symptoms are Fever,Dry cough,Fatigue,Loss of taste or smell,Nasal congestion,Conjunctivitis (also known as red eyes),Sore throat,Headache,Muscle or joint pain,Different types of skin rash,Nausea or vomiting,Diarrhea,Chills or dizziness.Shortness of breath,Loss of appetite,Confusion,Persistent pain or pressure in the chest,High temperature (above 38 °C) 


Among those who develop them , most (about 80%) recover from the disease without needing hospital treatment. About 15% become seriously ill and require oxygen and 5% become critically ill and need intensive care.Complications leading to death may include respiratory failure, acute respiratory distress syndrome (ARDS), sepsis and septic shock, thromboembolism, and/or multiorgan failure, including injury of the heart, liver or kidneys

The long-term effects
The effects are Some people who have had it, whether they have needed hospitalization or not, continue to experience signs, including fatigue, respiratory and neurological signs

When should I get a test
Anyone with indicators should be tested, wherever possible. People who do not have indicators but have had close contact with someone who is, or may be, infected may also consider testing – contact your local health guidelines and follow their guidance.
While a person is waiting for test results, they should remain isolated from others

what should I do if I have any indicators
If you have any signs of it , call your health care provider or the hotline for instructions and find out when and where to get a test, stay at home for 14 days away from others and monitor your health.

The treatment for people who are hospitalised with severe of this disease is largely supportive (e.g.oxygen therapy, management of fluids), mostly using a symptomatic approach, targeting them rather than the virus.Several pharmaceuticals have been studied or are currently being studied in clinical trials to assess their safety and efficacy as potential treatments for the disease. There is evidence that dexamethasone, a corticosteroid, is beneficial for severe disease (i.e. patients who require oxygen).Several drugs and antibody preparations are under assessment.


can I contract coronavirus more than once
yes


how is it transmitted
SARS-CoV2 is mainly transmitted via respiratory droplets and aerosols from an infected person when they sneeze, cough, speak or breathe and are in close proximity to other people. The virus has also been isolated from the faeces of infected cases, indicating that faecal-oral transmission might also be a route of infection. Droplets can be inhaled or can land on surfaces that others come into contact with and are then infected when they touch their nose, mouth or eyes. The virus can survive on surfaces from anything between a few hours (copper, cardboard) to a number of days (plastic and stainless steel). However, the amount of viable virus declines over time and it may not always be present in sufficient quantities to cause infection.

cases in each country
for total cases refer to this link:- https://covid19.who.int/

Precaution
stay safe by taking some simple precautions, such as physical distancing, wearing a mask, keeping rooms well ventilated, avoiding crowds, cleaning your hands, and coughing into a bent elbow or tissue. Check local advice where you live and work. Do it all!

Variants
When a virus has one or more new mutations it’s called a variant of the original virus.Currently, several variants of the virus that causes coronavirus disease are creating concern in the U.S. ,These variants include:- Alpha,Beta,Gamma,and Delta


The delta variant is now the most common COVID-19 variant in the U.S. It’s nearly twice as contagious as earlier variants and might cause more severe illness. The greatest risk of transmission is among unvaccinated people.


Vaccines
There are now several vaccines that are in use.The Pfizer/BioNtech Comirnaty vaccine was listed for WHO Emergency Use Listing (EUL) on 31 December 2020.The SII/Covishield and AstraZeneca/AZD1222 vaccines (developed by AstraZeneca/Oxford and manufactured by the State Institute of India and SK Bio respectively) were given EUL on 16 February.
'''

#TOKENIZATION

sentence_list = nltk.sent_tokenize(data)


#A function to return a random greeting response to a users greeting

def greeting_response(text):
    text = text.lower()

    bot_greetings = ["Hi", "Hey", "*nods*", "Hi There", "Hello", "I am glad! You are talking to me"]

    user_greetings = ["hello", "hi", "greetings", "sup", "what's up","hey","yo",]

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)

#Sort Function
def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                list_index[i],list_index[j]= list_index[j],list_index[i]

    return list_index

#Create the bots response
def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    index = index[1:]
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response+' '+sentence_list[index[i]]
            response_flag = 1
            j = j + 1
        if j > 2:
            break

        if response_flag == 0:
            bot_response = bot_response+' '+"I apologize, I don't understand"

        sentence_list.remove(user_input)

        return bot_response

#START THE CHAT

print("Doc Bot: I am Doctor Bot or Doc Bot for short. I will answer all your queries about COVID-19 Disease.If you want to exit ,type bye")

exit_list = ['exit','see you later','bye','quit','break']

while(True):
    user_input = input()
    if user_input.lower() in exit_list:
        print("Doc Bot: Chat with you later !")
        break
    else:
        if greeting_response(user_input) != None:
            print("Doc Bot:" +greeting_response(user_input))
        else:
            print("Doc Bot:" +bot_response(user_input))



# In[3]:


#


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:








