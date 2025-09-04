addEventListener("submit", function(event){
    event.preventDefault();

    usuario = document.querySelector("#usuario").value;
    senha = document.querySelector("#senha").value;

    dados = {
        usuario: usuario,
        senha: senha
    }
    
    fetch("/login", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(dados)
    })
    .then(response => {
        return response.json().then(data => {
            if(!response.ok)
            {
                throw new Error(data.erro)
            }
            return data
        })
    })
    .then(data => {
        alert(data.mensagem)

        location = "/home";
    })
    
})