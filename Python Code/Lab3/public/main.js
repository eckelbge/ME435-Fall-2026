async function sendCommand(command) {
    var response = await fetch("/api/" + command) //fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log(replyText);

    document.querySelector("#replyText").innerHTML = replyText;

    return replyText;
}

function main(){
    console.log("Hello JavaScript!!!");
    // document.querySelector("#reset").innerHTML = "Hello";

    document.querySelector("#reset").onclick = () => {
        sendCommand("RESET");
    };

    document.querySelector("#x1").onclick = () => {
        sendCommand("X-AXIS 1");
    };
    document.querySelector("#x2").onclick = () => {
        sendCommand("X-AXIS 2");
    };
    document.querySelector("#x3").onclick = () => {
        sendCommand("X-AXIS 3");
    };
    document.querySelector("#x4").onclick = () => {
        sendCommand("X-AXIS 4");
    };
    document.querySelector("#x5").onclick = () => {
        sendCommand("X-AXIS 5");
    };

    document.querySelector("#gripop").onclick = () => {
        sendCommand("GRIPPER OPEN");
    };
    document.querySelector("#gripcl").onclick = () => {
        sendCommand("GRIPPER CLOSE");
    };

    document.querySelector("#ze").onclick = () => {
        sendCommand("Z-AXIS EXTEND");
    };
    document.querySelector("#zr").onclick = () => {
        sendCommand("Z-AXIS RETRACT");
    };

    document.querySelector("#move").onclick = () => {
        let startPos = document.querySelector("#movefrom").value
        let endPos = document.querySelector("#moveto").value
        sendCommand(`MOVE ${startPos} ${endPos}`)
    };

    document.querySelector("#status").onclick = () => {
        sendCommand("LOADER_STATUS");
    };
}


main();
