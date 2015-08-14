var table = $("#form_table");
var row = $("#table_row");
var filelist;
// ADD ROW TO TABLE AFTER LAST ELEMENT
function addToList(){
      var limit = 1;
    for(var i=0; i<limit;i++){
        row.show();
        row.clone().appendTo(table);
    }
    row.hide();
}

$("#add_more").click(function () {
    addToList();
});

// CREATE TABLE BASED ON DATA ON JSON FILE. 
// DEPENDS HOW MANY FILES THERE ARE IN THE JSON
function makeTable(){
    $.get('/comictable','hello server',function(data){
        alert(data);
        var len = data.comics.length;
        console.log(len);
        console.log("Full JSON Data");
        console.log(data);
        if (data.comic =="root"){ console.log("EQUALS ROOT");}
        for(var i=0; i< len;i++){
            var comic = data.comics[i];
            console.log(comic);
            console.log(i);
            $("#id").text(i+1);
            $("#name").text(comic.name);
            $("#year").text(comic.year);
            $("#issue").text(comic.issue_number);
            $("#lang").text("English_");
            $("#publisher").text("DC");
            var n_row = row.clone().appendTo(table); //FIX ME:later: to add row with data from json
            n_row.attr("id","#table_row_"+i);

            // console.log(data.comics[i].name);
        }
        row.hide();
    });

}

$("#make_table").click(function(){
    makeTable();
});


$(function() {
    $('#upload_button').click(function() {
        var form_data = new FormData($('#upload_comic')[0]);
        $.ajax({
            type: 'POST',
            url: '/upload',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            async: true,
            success: function(data) {
                console.log('Success!');
                console.log(form_data);
            },
        });
    });
});

//DO MORE
//https://developer.mozilla.org/en-US/docs/Using_files_from_web_applications#Getting_information_about_selected_file(s)
//HANDLES OPENING A FILE OR MULTIPLE FILES TO GET FILE OBJECT

// $('#comicdrop').filedrop({
//     paramname: 'file',
//     maxfiles: 50,
//     maxfilesize: 50,
//     url: '/upload',
//     uploadFinished:function(i,file,response){
//         $.data(file).addClass('done');
//         console.log(file);
//     }


// });

