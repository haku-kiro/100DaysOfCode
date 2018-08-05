//Will contain all of my jquery
$(document).ready(function() {
    //All of the codes :P
    
    //This would hide all the paragraph tags
    //$("p").hide();

    //This would make the button hide something
    $("#toggleButton").on("click", function() {
        $("p").toggle(); // This toggles the show and hide method
    });

    //Special selectors:

    $("#Hidemyself").on("click", function(){
        //'This', selects the current element
        $("#someItems").empty();
        $(this).hide(); 
    });


    //Selects all the p elements with the class 'thing'
    $("p.thing").css("color", "red");

    //Selects the first element
    $("p:first").css("color", "blue");

    //A lot more special selectors available at:  https://www.w3schools.com/Jquery/jquery_selectors.asp

    //Events
    $("p").dblclick(function() {
        alert("You double clicked a p tag!");
    });

    // //Works, just stops the rest of the buttons purpose from happening
    // $("button:first").mouseenter(function() {
    //     alert("Your mouse entered the first button");
    // });

    //Focus on an element (Does this only apply to the first element? Only when you use an id, 
    //a class doesn't have that problem - can be applied to many things
    $(".textField").focus(function(){
        $(this).css("background-color", "blue");
    });

    //Leave that element:
    $(".textField").blur(function() {
        $(this).css("background-color", "white");
    });

    //Attaching multiple event handlers to something using the on keyword
    // Quite nice
    $("#thing5").on(
        {
            mouseenter: function(){
                $(this).css("background-color", "lightgray");
            },
            mouseleave: function(){
                $(this).css("background-color", "lightblue");
            },
            click: function(){
                $(this).css("background-color", "yellow");
            }
        }
    );

    //Showing things:
    $("#showAll").click(function(){
        //Special selector to select everything
        //interestingly enough, shows the title on the webpage as well. Therefore, use with caution
        $("*").show();
    });

    $("#thing3").click(function() {
        //The value is in milliseconds, can also use `fast`, or `slow`
        $(this).hide(1000);
    });

    //You can fade things in and out:
    $("#thing4").click(function(){
        $(this).fadeOut("slow");
        //This value is in milliseconds as well (fast, slow as well)
        $(this).fadeIn(1000);
    });

    $("#fadeToggle").click(function(){
        $("*").fadeToggle("slow"); // everything goes away
    });

    //You can fade to a certain opacity
    $("#thing6").click(function() {
        $(this).fadeTo("slow", 0.7); // level between 0 and 1
    });

    //There are a lot of other effects: Just check the w3schools webpage

    //jQuery dom manipulation methods:
    //These are set or return methods (no params, gets, params - sets).
    //.html (content, including html markup)
    //.text (sets content)
    //.val (sets form fields)

    $("#thing6").html("Changed with jQuery <br>"); // would include the html markup
    $("#thing6").text("Changed, you didn't see anything <br>");


    //Getting the values:
    $("#thing2").click(function() {
        alert("The html value of the thing you clicked: " + $("#thing2").html()); //returns the html
        alert("The text value of the thing you clicked: " + $("#thing2").text()); //returns the text
    });

    $("#thing8").on("click", function() {
        alert("href value: " + $("#thing8").attr('src'));
    });

    // you can use the get fields with values in them (text, html, val) to set a value
    // you can use the attr with a second param as the value if you want to set something

    //TODO: go over the use of the callback functions in the setters

    //jQuery, adding elements to the dom
    // these methods:
    //append() - inserts element at the end of the selected elements
    //prepend() - insertes content at the beginning of the selected elements
    //after() - inserts content after the selected elements
    //before() - inserts content before the selected elements

    //Append
    $("p:first").append("- Some appeneded text");

    //Prepend
    $("p:first").prepend("Some prepended text -");

    appendText();

    //after
    $("p:first").after("Some text after");

    //Before
    $("p:first").before("Some text before");

    //Methods for removing
    //remove() - Removes the selected element (and it's child elements)
    //empty() - removes the child elements from the selected element

    //remove
    $("#thing9").remove();

    //empty
    //Rather try this with a div at some point
    $("#someItems").click(function() {
        $("#someItems").empty();
    });

});

//Function to create elements 
function appendText() {
    var txt1 = "<p>Text.</p>";               // Create element with HTML 
    var txt2 = $("<p></p>").text("Text.");   // Create with jQuery
    var txt3 = document.createElement("p");  // Create with DOM
    txt3.innerHTML = "Text.";
    $("body").append(txt1, txt2, txt3);      // Append the new elements
}