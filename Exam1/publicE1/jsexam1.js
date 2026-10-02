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
   
    document.querySelector("#flash").onclick = () => {
        let numflash = document.querySelector("#flashnum").value
        let perflash = document.querySelector("#flashper").value
        sendCommand(`FLASH ${numflash} ${perflash}`)
    };
}


main();