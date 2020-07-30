/*Populates Branded url based on input*/
function brand_namespace_atuo_fill() {
   var long_url = document.getElementById("lname").value;
   if(long_url.length < 1 )
      {
         
      }
      else{

  
   document.getElementById('branded_link').style.display="grid"
    

    /*Get the Document*/
    
    console.log(long_url);

    /*Change to lower caset*/
    long_url = long_url.toLowerCase();

    /*Parse as URL*/
    const url = new URL(long_url)
    console.log(url)

    /*Checks for https and populates data accordingly*/
    if (url.protocol == 'https:') {
        console.log('https check');

        const url_hostname= url.hostname;
        const all_of_url=url.href;
        

        /* Adding conditions for claim.run */
        var claim_run_conditions = ["sale", "hurry", "discount","claim","cheap","low","price","cost","end","soon"];


        if (url_hostname.includes('amazon')==true){
            /*Fills in Amazon*/
            document.getElementById("branded_link").value='amzn.how';
            
        } else if (url_hostname.includes('youtube')==true) {

            document.getElementById("branded_link").value='ytube.page';
            
        } else if (url_hostname.includes('twitter')==true) {

            document.getElementById("branded_link").value='twttr.site';
           
        } else if (url_hostname.includes('ebay')==true) {


           document.getElementById("branded_link").value='ebay.party';
        } else if (url_hostname.includes('yelp')==true) {


           document.getElementById("branded_link").value='yelp.pw';
        } else if (url_hostname.includes('linkedin')==true) {


           document.getElementById("branded_link").value='lnkd.dev';
        } else if (url_hostname.includes('instagram')==true) {


           document.getElementById("branded_link").value='insta.blue';
        } else if (url_hostname.includes('etsy')==true) {


           document.getElementById("branded_link").value='etsy.one';

        } else if (url_hostname.includes('pinterest')==true) {

           document.getElementById("branded_link").value='pinterest.blue';

        } else if (url_hostname.includes('walmart')==true) {

           document.getElementById("branded_link").value='wlmart.in';

        } else if (url_hostname.includes('reddit')==true) {

           document.getElementById("branded_link").value='reddit.fyi';

        } else if (url_hostname.includes('wiki')==true) {

           document.getElementById("branded_link").value='wiki.army';

        } else if ((claim_run_conditions.some(el => all_of_url.includes(el))==true)) {

           document.getElementById("branded_link").value='claim.run';
        } 
        else {
            document.getElementById("branded_link").value='omelet.xyz';
        }
    }
    else{
        console.log("fell inside mega else")
    }

   }
}

