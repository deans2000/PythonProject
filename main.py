from judete import romania
from flask import Flask,request
app=Flask(__name__)

def replace_romanian_letters(text):
    replacements = {
        "ă": "a", "â": "a", "î": "i", "ș": "s", "ț": "t",
        "Ă": "A", "Â": "A", "Î": "I", "Ș": "S", "Ț": "T"
    }
    for romanian, english in replacements.items():
        text = text.replace(romanian, english)
    return text.replace(" ", "")

# Apply the function to each city in the dictionary
new_romania = {}
for county, cities in romania.items():
    new_county = replace_romanian_letters(county)
    new_cities = []
    for city in cities:
        new_city = replace_romanian_letters(city)
        new_cities.append(new_city)
    new_romania[new_county] = new_cities

@app.route('/judete')
def getJudete():
    return new_romania

@app.route('/judete/<oras>')
def getJudet(oras):
    for judet in new_romania:
        if oras in new_romania[judet]:
            return judet

if __name__=='__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)