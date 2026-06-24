const http = require("http");
const fs = require("fs");

const html = `
<!DOCTYPE html>
<html>
<head>
    <title>DevOps App</title>
</head>
<body>
    <h1>DevOps Project</h1>
    <button onclick="loadTodos()">Load Todos</button>
    <ul id="list"></ul>

    <script>
        async function loadTodos() {
            const res = await fetch("/api/todos");
            const data = await res.json();

            const list = document.getElementById("list");
            list.innerHTML = "";

            data.forEach(todo => {
                const li = document.createElement("li");
                li.innerText = todo.text;
                list.appendChild(li);
            });
        }
    </script>
</body>
</html>
`;

http.createServer((req, res) => {
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
}).listen(3000);