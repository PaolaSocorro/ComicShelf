var table = $("#form_table");
var row = $("#table_row");


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


function makeTable(){
    $.get('/comictable','hello server',function(data){
        alert(data);
        var len = data.comics.length;
        console.log(len);
        console.log(data);
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