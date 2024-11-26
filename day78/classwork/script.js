let info = {
    lastname:'melkadze',
    adres:'tbilisi',
    academy:'goal oriented academy'
}
console.log(info);



document.getElementById('forPar').textContent='change'
document.getElementById('forPar1').textContent='change1'



function changer() {
    forP=document.getElementById('secTask')
    forP.textContent='changed'
}

forColor=document.getElementById('color')

function green() {
    forColor.style.color='green'
}

function red() {
    forColor.style.color='red'
}

function blue() {
    forColor.style.color='blue'
}