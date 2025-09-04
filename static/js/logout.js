function logout() {
  // Pergunta ao usuário se tem certeza
  const confirmar = confirm("Tem certeza que deseja sair?");
  if (confirmar) {
    // Limpa dados de login
    localStorage.clear();
    sessionStorage.clear();

    // Redireciona para a página de login
    window.location.href = "/Game-Hub/templates/login.html"; // ajuste o caminho real
  } 
  // Se o usuário clicar "Não", nada acontece
}
