const socket = io();

let currentAlias = '';

function joinChat() {
    const aliasInput = document.getElementById('alias');

    currentAlias = aliasInput.value.trim();

    if (!currentAlias) {
        alert('Enter alias');
        return;
    }

    socket.emit('join', {
        alias: currentAlias
    });
}

function sendMessage() {
    const messageInput = document.getElementById('message');

    const message = messageInput.value.trim();

    if (!message) return;

    socket.emit('send_message', {
        alias: currentAlias,
        message: message
    });

    messageInput.value = '';
}

const shownMessages = new Set();

socket.on('message', (data) => {

    if (shownMessages.has(data.message)) {
        return;
    }

    shownMessages.add(data.message);

    addMessage(data.message);

    setTimeout(() => {
        shownMessages.delete(data.message);
    }, 2000);

});

socket.on('system', (data) => {
    addSystemMessage(data.message);
});

function addMessage(message) {

    const chatBox = document.getElementById('chat-box');

    const div = document.createElement('div');

    const isOwnMessage = message.includes(`[${currentAlias}]`);

    if (isOwnMessage) {
        div.className = 'message own-message';
    } else {
        div.className = 'message other-message';
    }

    div.innerText = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}

function addSystemMessage(message) {
    const chatBox = document.getElementById('chat-box');

    const div = document.createElement('div');

    div.className = 'message system';
    div.innerText = message;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;
}
