function sendMessage() {
    let input = document.getElementById("user-input");
    let question = input.value.trim();

    if (question === "") return;

    let chatBox = document.getElementById("chat-box");

    chatBox.innerHTML += `<div class="user-message">${question}</div>`;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ question: question })
    })
    .then(response => response.json())
    .then(data => {
        chatBox.innerHTML += `<div class="bot-message">${data.answer}</div>`;
        chatBox.scrollTop = chatBox.scrollHeight;
    });

    input.value = "";
}