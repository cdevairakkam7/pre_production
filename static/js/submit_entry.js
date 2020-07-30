
/* Submit entry or show alert */
function submit_entry() {
    var long_url = document.getElementById('lname').value;
    var usr_input = document.getElementById('usr_input').value;
    var brand_domain = document.getElementById('branded_link').value;
    var obj = {
            long_url: long_url,
            usr_input: usr_input,
            brand_domain: brand_domain
        };
        long_url=long_url.trim();
        brand_domain=brand_domain.trim();
     console.log("under brand domain ")
        if (long_url.substring(0, 6) == 'https:')
         {
            fetch(`${window.origin}/`, {
                method: "POST",
                credentials: "include",
                cache: "no-cache",
                headers: new Headers({

                    'Content-Type': 'application/json'
                }),
                body: JSON.stringify(obj)
            }).then(function(response) {
                response.json().then(function(data) {

                    console.log(data.short_url)
                    if (data.short_url.match(/not/)) {

                        var output = document.getElementById("demo")
                        output.innerHTML = data.short_url;

                        document.getElementById('usr_input').value = ""
                    } else {
                        var output = document.getElementById("demo")
                        output.innerHTML = data.short_url;

                        document.getElementById('usr_input').value = "";
                        document.getElementById('lname').value = "";
                        document.getElementById("copy_id").style.display = "initial";

                    }


                })

            })

        }
    else {
        window.alert("Please enter a secure link. ")

    }
}
