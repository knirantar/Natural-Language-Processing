from nltk.corpus import stopwords
def lexical_diversity(text):
    return round(len(set(text))/len(text)*100,2)

def stopword_fraction(text):
    stop = stopwords.words('english')
    stop_text = [w for w in text if w in stop]
    return round(len((stop_text))/len(text)*100,2)

def remove_stop(text):
    stop = stopwords.words('english')
    res = []
    for i in text:
        if i not in stop:
            res.append(i)      
    return res

def remove_duplicate_words(text):
    return list(set(text))

def remove_case_sensitivity(text):
    text = [w.lower() for w in text]
    return list(set(text))

def remove_numbers(text):
    res = []
    for i in text:
        if not i.isdigit():
            res.append(i)
    return res

def remove_names(text):
    names = nltk.corpus.names
    male_names = names.words('male.txt')
    female_names = names.words('female.txt')
    males = [w for w in male_names]
    females = [w for w in female_names]
    #TODO REMOVAL OF NAMES FROM THE TEXT