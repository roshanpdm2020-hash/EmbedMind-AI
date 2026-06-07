async function analyzeCode() {

    const code = document.getElementById("codeArea").value;

    const response = await fetch(
        "http://127.0.0.1:8000/analyze",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                code: code
            })
        }
    );

    const data = await response.json();

    document.getElementById("result").textContent =
        data.analysis;
}