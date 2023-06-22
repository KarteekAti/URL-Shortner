var checkbox = document.getElementById('checkbox');
checkbox.addEventListener('change',function(){
    var custom = document.getElementById('custom-url');
    if(this.checked){
        custom.style.display = 'block';
    }
    else{
        custom.style.display = 'none';
    }
})

console.log(window.location.hostname)
