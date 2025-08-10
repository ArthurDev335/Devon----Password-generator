
document.getElementById("buttonValider").addEventListener("click", () => {
    const nombreCaracteres = document.getElementById("nombreCaracteres").value;
    const chiffre = document.getElementById("nombre");
    const speciaux = document.getElementById("caracteresSpeciaux");

    console.log(nombreCaracteres)
    console.log(chiffre.checked)
    console.log(speciaux.checked)

    fetch("/creation_mdp", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ 
            nombreCaracteres: parseInt(nombreCaracteres),
            chiffre: chiffre.checked,
            speciaux: speciaux.checked}),
    })
    .then(response => response.json())
    then( data => {
        document.getElementById("reponse").textContent = data.result;
    })
    .catch(() => {
        document.getElementById("reponse").textContent = "Erreur serveur.";
    })
});