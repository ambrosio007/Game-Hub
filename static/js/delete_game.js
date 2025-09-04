function deletar(jogo_id)
{
    fetch(`/games/${jogo_id}`, {
        method: 'DELETE'
    })

    .then(response =>{
        return response.json().then(data =>{
            if(!response.ok)
            {
                throw new Error(data.erro)
            }
            return data
        })
    })

    .then(data =>{
        alert(data.mensagem);
        location = "/home";
    })
}