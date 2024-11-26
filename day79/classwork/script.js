// const num1=prompt("enter number")
// const num2=prompt("enter number")


// document.getElementById('par').textContent=Number(num1)+Number(num2)


const form = document.getElementById('for')


function check(){
    const emailvalue=form.elements.gmail.value
    const colorvalue=form.elements.collor.value
    if (emailvalue == null || colorvalue == null)
    {
        alert('fill out');
        return
    }
}