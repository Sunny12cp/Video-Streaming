const chat = document.getElementById("chat");
const chatBtn = document.getElementById("chat-button");
const chatInput = document.getElementById("chat-input");
const chatText = document.getElementById("chat-text");

function openChat() {
  chat.style.width = "50%";
  chatBtn.setAttribute("onclick", "closeChat()");
  chatInput.focus();
}

function closeChat() {
  chat.style.width = "0%";
  chatBtn.setAttribute("onclick", "openChat()");
}

function sendMessage(e) {
  if (e.key == "Enter") {
    let msg = chatInput.value;
    if (msg != "") {
      socket.emit("addMsg", msg);
    }
  } else if (e.key == "Escape") {
    closeChat();
  }
}

socket.on("displayMsg", (msg) => {
  let p = document.createElement("p");
  let text = document.createTextNode(msg);
  p.appendChild(text);
  chatText.appendChild(p);
  chatInput.value = "";
});
