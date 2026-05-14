async function sendMessage(){

    let input = document.getElementById("user-input");

    let chatBox = document.getElementById("chat-box");

    let message = input.value;

    if(message === ""){
        return;
    }

    // Show user message
    chatBox.innerHTML += `
        <p><b>You:</b> ${message}</p>
    `;

    // Send to backend
    const response = await fetch("http://127.0.0.1:5000/chat", {

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({
            message:message
        })

    });

    const data = await response.json();

    // Show AI reply
    chatBox.innerHTML += `
        <p><b>AI:</b> ${data.reply}</p>
    `;

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;
}