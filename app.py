from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

def creation_mdp(length, chiffres, speciaux):
    lettres = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    caractere = ['&', '@', '§', '#', '$', '€', '£', '%', '(', ')', '!']

    n = length
    chiffre = chiffres
    caracteres = speciaux
    mdp = []
    password = []

    if chiffre == True:
        iteration = random.randint(1, n//2)
        for x in range(iteration):
            y = random.randint(0,9)
            y = str(y)
           
            if y in mdp:
                y = random.randint(0,9)
                y = str(y)
                mdp.append(y)

            else:
                mdp.append(y)
        
    if caracteres == True:
        iterationC = random.randint(1, n//2)
        for z in range(iterationC):
            z = random.randint(0,10)
            ajoutC = caractere[z]

            if ajoutC in mdp:
                z = random.randint(0,10)
                ajoutC = caractere[z]

            else:
                mdp.append(ajoutC)

    while len(mdp) <= n-1:
        hasard = random.randint(0, 25)
        lettre = lettres[hasard]
        if lettre in mdp:
            hasard = random.randint(0, 25)
            lettre = lettres[hasard]
            mdp.append(lettre)

        else:
            mdp.append(lettre)
    
    random.shuffle(mdp)
    password.append(''.join(mdp)) 
    return (password[0])

#serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint
@app.route("/creation_mdp", methods = ["POST"])
def api_generate():
    data = request.get_json()
    length = data.get("nombreCaracteres")
    chiffre = data.get("chiffre", True)
    speciaux = data.get("speciaux", True)

    try:
        length = int(length)
        chiffres = bool(chiffre)
        speciaux = bool(speciaux)

    except: 
        return(jsonify({"error": "Invalid parameters"})), 400

    motDePasse = creation_mdp(length, chiffres, speciaux)
    return jsonify({"password": motDePasse})

if __name__ == "__main__":
    app.run(debug = True)