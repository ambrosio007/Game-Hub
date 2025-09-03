addEventListener("submit", function(event){
    event.preventDefault();

    usuario = this.document.querySelector("#usuario").value;
    senha = this.document.querySelector("#senha").value;

    dados = {
        usuario: usuario,
        senha: senha
    }

    alert("Login realizado com sucesso!");

    location = "home.html";
 
    
    
})