
sum=0
function count(){
    
    sum+=1;
    document.getElementById('counter').textContent=sum
}
function zero(){
    document.getElementById('counter').textContent=0
}




function background(a) {
    document.getElementById('colChanger').style.backgroundColor=a
}