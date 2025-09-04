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

        fetch("/cadastro", {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(dados)
        })
        .then(response => {
            return response.json().then(data => {
                if(!response.ok){
                    alert("Algo deu errado, tente novamente!")
                }
                return data
            })
        })
        .then(data => {
            alert(data.mensagem)

            location = "/login";
        })

    }
})