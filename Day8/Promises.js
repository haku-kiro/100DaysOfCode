//Ge the loan stuff


var amtApproved = "";
var minDraw = "";
var freq = "";
var currentAmt = "";
var oppoId = "";

function checkThings() {

    var promise1 = new Promise(function(resolve, reject) 
    {
        crm.sdata(
            {
                "entity": "loan",
                "id" : crm.fields("ltrn_loanid").val(),
                "success" : function(crmRecord) 
                {
                    resolve(crmRecord.loan_opportunityid);
                }
            }
        );
    })
    .then(function(value) 
    {
        console.log(value);
        var promise2 = new Promise(function(resolve, reject){
            //Gets the limits
            $.ajax({
                type: "GET",
                url: "<private endpoint>"+value,
                success: function(data) {
                    resolve(data); 
                    }
            });
        }).then(function(value){
            //Use the limits (TODO set limits here)
            oppoId = value.data.oppoid;
            amtApproved = value.data.amtApproved;
            minDraw = value.data.minDraw;
            freq = value.data.freq;

            var promise3 = new Promise(function(resolve, reject){
                $.ajax({
                    type: "GET",
                    url: "<private endpoint>"+ oppoId,
                    success: function(data) {
                        resolve(data); 
                        }
                });
            }).then(function(value){
                //Do all the things
                currentAmt = value.data.facilityLimitTotal;
                console.log(currentAmt);
                console.log(oppoId);
                console.log(amtApproved);
                console.log(minDraw);
                console.log(freq);

                //Do init checks
                if (currentAmt > amtApproved)
                {
                    crm.infoMessage("Work related content");
                }

                //Work related content
                tranAmount = crm.fields("ltrn_amttransaction").val();
                if (tranAmount != null)
                {
                    //Process
                    if (tranAmount < minDraw)
                    {
                        //Need to check if there is a message already - if so, add to it, don't write new (would overwrite)
                        crm.infoMessage("Work related content");
                    }
                    
                    if (tranAmount+ currentAmt >= amtApproved)
                    {
                        crm.infoMessage("Work related content");
                    }
                }
                else 
                {
                    console.log("The transaction amount is currently null");
                }
            });
        });

    }).catch(function(error){
        console.log("There was an error");
    });
}


///////////////// Random tests
var outer = "";
//Get the oppo stuff
crm.sdata(
    {
        "entity":"opportunity",
        "id": crm.fields("loan_opportunityid").val(),
        "success": function(crmRecord) {alert(crmRecord.oppo_mindrawamt);}
    }
);

var promise1 = new Promise(function(resolve, reject) 
{
    crm.sdata(
        {
            "entity": "opportunity",
            "id" : 70198,
            "success" : function(crmRecord) 
            {
                resolve(crmRecord);
            }
        }
    );
})
.then(function(value) 
{
    outer = value;
    console.log("Done");
}).catch(function(error){
    console.log("There was an error");
})


crm.sdata({
	"entity":"opportunity",
	"where": ' oppo_description = "I\'m A Test Facility"',
	"success": function(crmRecord) {
		console.log(crmRecord.oppo_opportunityid);
	}
})

//Adding method to inputs (Work related content)
$("input").change(checkThings);