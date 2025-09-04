function add_game()
{
    const card = document.querySelector(".card");

    card.innerHTML += `<div class="capa-cover"><img id="cover"></div>
    <div class="janela">
        <div class="capa">
            <input type="file" id="file-capa" accept="image/*">
            <label for="file-capa" class="upload"><img id="capa"></label>
        </div>
        <form id="formulario">
            <label for="nome">Nome:</label>
            <input type="text" id="nome">
            <label for="desc">Descrição:</label>
            <textarea id="desc"></textarea>
            <label for="plataformas">Adicione plataformas:</label>
            <select id="plataforma1">
                <option value="vazio">Vazio...</option>
                <option value="steam">Steam</option>
                <option value="xbox">Xbox</option>
                <option value="epic">Epic Games</option>
                <option value="gog">GOG</option>
                <option value="play">Playstation</option>
            </select>
            <select id="plataforma2">
                <option value="vazio">Vazio...</option>
                <option value="steam">Steam</option>
                <option value="xbox">Xbox</option>
                <option value="epic">Epic Games</option>
                <option value="gog">GOG</option>
                <option value="play">Playstation</option>
            </select>
            <select id="plataforma3">
                <option value="vazio">Vazio...</option>
                <option value="steam">Steam</option>
                <option value="xbox">Xbox</option>
                <option value="epic">Epic Games</option>
                <option value="gog">GOG</option>
                <option value="play">Playstation</option>
            </select>
            <button type="submit"><img src="/static/icons/Save.png"></button>
        </form>
    </div><button id="voltar" onclick="voltar()">X</button>`;

    const file_capa = document.querySelector("#file-capa");
    const capa_preview = document.querySelector("#capa")
    const capa_cover = document.querySelector("#cover");
    const formulario = document.querySelector("#formulario");


    file_capa.addEventListener("change", function(e){

        if(e.target.files && e.target.files[0])
        {
            const reader = new FileReader();

            reader.onload = (event) =>{
                capa_preview.src = event.target.result;
                capa_cover.src = event.target.result;
            }
            reader.readAsDataURL(e.target.files[0]);
        }
    });

    formulario.addEventListener("submit", function(event){
        event.preventDefault();

        const formData = new FormData();

        const nome = document.querySelector("#nome").value;
        const desc = document.querySelector("#desc").value;
        const plataforma1 = document.querySelector("#plataforma1").value;
        const plataforma2 = document.querySelector("#plataforma2").value;
        const plataforma3 = document.querySelector("#plataforma3").value;

        formData.append("nome", nome);
        formData.append("desc", desc);
        formData.append("plataforma1", plataforma1);
        formData.append("plataforma2", plataforma2);
        formData.append("plataforma3", plataforma3);

        if(file_capa.files && file_capa.files[0])
        {
            formData.append("imagem", file_capa.files[0]);
        }

        fetch("/games/add", {
            method: 'POST',
            body: formData
        })
        .then(response =>{
            return response.json().then(data =>{
                if(!response.ok)
                {
                    alert("Algo deu errado, tente novamente!")
                }
                return data
            })
        })
        .then(data =>{
            alert(data.mensagem);
            location = "/home";
        })

    })
}



