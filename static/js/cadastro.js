addEventListener("submit", function(event){
    event.preventDefault();

    nome = this.document.querySelector("#nome").value;
    usuario = this.document.querySelector("#usuario").value;
    email = this.document.querySelector("#email").value;
    senha = this.document.querySelector("#senha").value;
    senha2 = this.document.querySelector("#senha2").value;

    if(senha != senha2)
    {
        alert("As senhas precisam ser idênticas!")
    }
    else
    {
        dados = {
            nome: nome,
            usuario: usuario,
            email: email,
            senha: senha
        }

        alert("Cadastro realizado com sucesso!");

        location = "login.html";
    }
})