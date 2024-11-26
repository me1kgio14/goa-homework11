function checker(){
    let passsword = document.getElementById('pass1').value;

    if (passsword.length > 8){
        document.getElementById('text').textContent='password is long anough'
        document.getElementById('text').style.color='green'
    }else{
        document.getElementById('text').style.color='red'
    }
}