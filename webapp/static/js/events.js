function addMessageFromUser()
{
    let message = document.getElementById("question");
    let appendLocation = document.getElementById("messaging");
    let newMessageDiv = document.createElement("div");
    newMessageDiv.className = "item right";
    let newSubDiv = document.createElement("div");
    newSubDiv.className = "msg";
    let messageContent = document.createElement("p");
    messageContent.innerText = message.value;
    newSubDiv.appendChild(messageContent);
    newMessageDiv.appendChild(newSubDiv);
    let alignment = document.createElement("br");
    alignment.clear = "both";
    appendLocation.appendChild(alignment);
    appendLocation.appendChild(newMessageDiv);
    addMessageFromBot();
}

function addMessageFromBot()
{
    let responseFromBot = "{{ response }}";
    let appendLocation = document.getElementById("messaging");
    let newResponseDiv = document.createElement("div");
    newResponseDiv.className = "item";
    let iconDiv = document.createElement("div");
    iconDiv.className = "icon";
    let italic = document.createElement("div");
    italic.className = "fa fa-user";
    iconDiv.appendChild(italic);
    newResponseDiv.appendChild(iconDiv);
    let newSubDiv = document.createElement("div");
    newSubDiv.className = "msg";
    let responseContent = document.createElement("p");
    responseContent.innerText = responseFromBot;
    newSubDiv.appendChild(responseContent);
    newResponseDiv.appendChild(newSubDiv);
    let alignment = document.createElement("br");
    alignment.clear = "both";
    appendLocation.appendChild(alignment);
    appendLocation.appendChild(newResponseDiv);
}