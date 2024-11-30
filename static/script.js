document.addEventListener("DOMContentLoaded", async () => {
    const runButton = document.getElementById("run-button");
    const clearButton = document.getElementById("clear-button");
    const terminal = document.getElementById("terminal");
    const modeSelector = document.getElementById("mode");
    const scriptSelector = document.getElementById("script-selector");
    const projectDropdown = document.getElementById("projects");
    const scriptsDropdown = document.getElementById("scripts");

    let pyodide = null;

    // Carrega Pyodide
    async function loadPyodideInstance() {
        terminal.textContent = "Loading Pyodide...\n";
        pyodide = await loadPyodide();
        terminal.textContent += "Pyodide loaded. Ready to execute Python scripts.\n";
    }

    await loadPyodideInstance();

    // Modo Write/Choose
    modeSelector.addEventListener("change", async (event) => {
        const mode = event.target.value;

        if (mode === "write") {
            document.getElementById("python-code").style.display = "block";
            scriptSelector.style.display = "none";
        } else if (mode === "choose") {
            document.getElementById("python-code").style.display = "none";
            scriptSelector.style.display = "block";
            await loadProjects();
        }
    });

    // Carrega os projetos e scripts
    async function loadProjects() {
        const response = await fetch("/list-scripts");
        const projects = await response.json();

        projectDropdown.innerHTML = ""; // Limpa projetos antigos
        scriptsDropdown.innerHTML = ""; // Limpa scripts antigos

        Object.keys(projects).forEach((project) => {
            const option = document.createElement("option");
            option.value = project;
            option.textContent = project;
            projectDropdown.appendChild(option);
        });

        // Carrega os scripts do primeiro projeto por padrão
        loadScripts(projectDropdown.value, projects);
    }

    // Carrega os scripts do projeto selecionado
    projectDropdown.addEventListener("change", async (event) => {
        const selectedProject = event.target.value;
        const response = await fetch("/list-scripts");
        const projects = await response.json();

        loadScripts(selectedProject, projects);
    });

    function loadScripts(project, projects) {
        scriptsDropdown.innerHTML = ""; // Limpa scripts antigos
        const scripts = projects[project] || [];

        scripts.forEach((script) => {
            const option = document.createElement("option");
            option.value = script;
            option.textContent = script;
            scriptsDropdown.appendChild(option);
        });
    }

    // Limpa o terminal
    clearButton.addEventListener("click", () => {
        terminal.textContent = "";
    });

    // Executa o script selecionado
    runButton.addEventListener("click", async () => {
        const mode = modeSelector.value;
        let code;

        if (mode === "write") {
            code = document.getElementById("python-code").value;
        } else if (mode === "choose") {
            const project = projectDropdown.value;
            const script = scriptsDropdown.value;

            const response = await fetch(`/get-script/${project}/${script}`);
            const data = await response.json();

            if (data.error) {
                terminal.textContent += `Error: ${data.error}\n`;
                return;
            }

            code = data.content;
        }

        if (!code) {
            terminal.textContent += "No code to run.\n";
            return;
        }

        try {
            terminal.textContent += "Running...\n";
            const result = await pyodide.runPythonAsync(code);
            terminal.textContent += `Output:\n${result}\n`;
        } catch (error) {
            terminal.textContent += `Error:\n${error}\n`;
        }
    });
});
