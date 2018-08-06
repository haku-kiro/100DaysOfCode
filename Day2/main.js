$(document).ready(function() {

    //Just to load the text from the file to the div element onscreen
    $("#button1").on({
        "click": function() {
            $("#div1").load("data.txt");
        },
    });


    //Not too sure how this works
    $("#button2").click(function() {
        $("#div2").load("data.txt #p1");
    });

    //You can pass a callback to the load function to have a success message/event handler on success as well as 
    //fail

    $("#button3").click(function() {
        $("#div3").load("data.txt", function(resp, status, xhr) {
            if (status == "success")
            {
                alert("Success! xhr status: " + xhr.status + " status text:"+ xhr.statusText);
            }
            else if (status == "error")
            {
                alert("Fail! xhr status: " + xhr.status + " status text:"+ xhr.statusText);
            }
            else 
            {
                alert("xhr status: " + xhr.status + " status text:"+ xhr.statusText + " status: " + status);
            }
        })
    });

    //There are http request covered by jquery as well:
    //get - requests data from a resource (NOTE, may return cached data)
    //post - submits data to be processed

    //Get
    // Testing with - https://resttesttest.com/
    $("#button4").click(function() {
        $.get("https://resttesttest.com/", function(data, status) {
            alert("Data: " + data + "\nStatus: " + status);
        });
    });


    //Post
    //Testing with - http://127.0.0.1:5002/check
    //A rest api endpoint i have created with python

    //Even though I got a cors error, this worked and handled my post request
    $("#button5").click(function() {
        $.post("http://127.0.0.1:5002/check", 
        {
           id: "Values", 
        },
        //This call back didn't occur, I think cors stopped it from working 
            function(data, status) {
                alert("Data: " + data + "\nStatus: " + status);
            }
        );
    });

    //Misc - other jQuery things to do:
    //jQuery has a no conflict mode incase another framework uses the $ 
    
    //Still works, just messes with the rest of the file ($ is no longer a function)
    // var jq = $.noConflict();
    // jq("#div1").css("background-color", "red");
});

//Jquery filter
//Expample taken from: https://www.w3schools.com/Jquery/tryit.asp?filename=tryjquery_filters_list

$(document).ready(function(){

    //We select the input, adding the keyup event listener
    $("#myInput").on("keyup", function() {
        //we set the value of the input (this) to lower case
        var value = $(this).val().toLowerCase();
        // we select the list items under the list and toggle their visability based on the 
        // index of that element being in the list. Rem, toggle goes from hide() to show() and back
        $("#myList li").filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1); //Quite cool that the param can be bool 
        });                                                                   // and is dynamic
    });
  });