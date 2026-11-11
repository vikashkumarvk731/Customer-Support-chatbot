const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");
const chatBox = document.getElementById("chat-box");
const sendButton = document.getElementById("send-button");

function addMessage(text, sender) {
  const row = document.createElement("div");
  row.className = `message-row ${sender === "user" ? "user-row" : "bot-row"}`;

  if (sender === "bot") {
    const avatar = document.createElement("div");
    avatar.className = "avatar";
    avatar.textContent = "AI";
    row.appendChild(avatar);
  }

  const bubble = document.createElement("div");
  bubble.className = `message ${sender === "user" ? "user-message" : "bot-message"}`;
  bubble.textContent = text; // textContent prevents user input from being interpreted as HTML
  row.appendChild(bubble);
  chatBox.appendChild(row);
  chatBox.scrollTop = chatBox.scrollHeight;
  return row;
}

async function sendMessage(message) {
  const text = (message ?? userInput.value).trim();
  if (!text) return;

  addMessage(text, "user");
  userInput.value = "";
  sendButton.disabled = true;
  const typingRow = addMessage("Typing...", "bot");
  typingRow.querySelector(".message").classList.add("typing");

  try {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: text })
    });
    const data = await response.json();
    typingRow.remove();
    if (!response.ok) throw new Error(data.reply || "Request failed");
    addMessage(data.reply || "I couldn't generate a response.", "bot");
  } catch (error) {
    typingRow.remove();
    addMessage("Sorry, I couldn't connect to the server. Check that Flask is running and try again.", "bot");
    console.error("Chat request failed:", error);
  } finally {
    sendButton.disabled = false;
    userInput.focus();
  }
}

chatForm.addEventListener("submit", (event) => {
  event.preventDefault();
  sendMessage();
});

document.querySelectorAll(".suggestion").forEach((button) => {
  button.addEventListener("click", () => sendMessage(button.dataset.message));
});
