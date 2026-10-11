const chatForm = document.getElementById('chatForm');
const chatWindow = document.getElementById('chatWindow');
const messageInput = document.getElementById('messageInput');

function appendMessage(text, isUser = false) {
  const div = document.createElement('div');
  div.className = `message ${isUser ? 'user' : 'bot'}`;
  div.textContent = text;
  chatWindow.appendChild(div);
  chatWindow.scrollTop = chatWindow.scrollHeight;
}

chatForm.addEventListener('submit', async (event) => {
  event.preventDefault();
  const message = messageInput.value.trim();
  if (!message) return;

  appendMessage(message, true);
  messageInput.value = '';

  const response = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message }),
  });

  const data = await response.json();
  appendMessage(data.reply, false);
});
