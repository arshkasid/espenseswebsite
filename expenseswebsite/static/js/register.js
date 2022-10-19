const usernameField = document.querySelector("#usernameField");
console.log(usernameField);
usernameField.addEventListener('keyup', (e) => {
    const usernameVal = e.target.value;

    if(usernameVal.length > 0){
        fetch('/authentication/validate-username', {
            body: JSON.stringify({ username: usernameVal }),
            method: 'POST',
        }).then(res => res.json())
        .then(data => {
            console.log(data);
        })
    }
});
