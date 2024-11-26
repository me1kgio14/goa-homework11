let form = document.getElementById('myForm');

const base=[]

function valui(){
    const lastvalue=form.lastname.value;
    const namevalue=form.name.value;
    const emailvalue=form.gmail.value

    const values = {
        last : lastvalue,
        name : namevalue,
        email: emailvalue,
    }

    base.push(values)
    console.log(base)
}
   
