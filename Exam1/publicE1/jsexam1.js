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

    document.querySelector("#on").onclick = () => {
        sendCommand("LED ON");
    };
    document.querySelector("#off").onclick = () => {
        sendCommand("LED OFF");
    };
   
    document.querySelector("#move").onclick = () => {
        let numflsh = document.querySelector("#numflash").value
        let perflsh = document.querySelector("#perflash").value
        sendCommand(`FLASH ${numflsh} ${perflsh}`)
    };
}


main();