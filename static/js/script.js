
const inputTarefa = document.getElementById("tarefa")

const formularioSuperior = document.querySelector(".formSuperior")

const formulario = document.querySelector(".formulario")

inputTarefa.addEventListener("click", () => {

    if (formularioSuperior.querySelector("textarea")) return;


    const descricao = document.createElement("textarea")
    descricao.name = "descricao"
    descricao.rows=5
    descricao.placeholder="Adicione uma descrição (opcional)"

    formularioSuperior.append(descricao)
    
    const formularioInferior = document.createElement("div")
    formularioInferior.classList.add("formInferior")

    const btnAdicionar = document.createElement("button")

    
    const imgMais = document.createElement("img")
    imgMais.src = "/static/img/add-svgrepo-com.svg"
    imgMais.classList.add("iconMais")

    const pAdicionar = document.createElement("p")
    pAdicionar.classList.add("adicionar")

    pAdicionar.textContent = "Adicionar"

    btnAdicionar.append(imgMais, pAdicionar)

    formularioInferior.append(btnAdicionar)

    formulario.append(formularioInferior)
})

// salva posição antes de sair
window.addEventListener("beforeunload", () => {
  localStorage.setItem("scrollY", window.scrollY);
});

// restaura ao carregar
window.addEventListener("load", () => {
  const scrollY = localStorage.getItem("scrollY");
  if (scrollY !== null) {
    window.scrollTo(0, parseInt(scrollY));
    localStorage.removeItem("scrollY");
  }
});