$('.selectpicker').selectpicker();
$('.selectpicker').selectpicker({
      style: 'btn-info',
      // size: 4
  });


$(function(){
$('.comicopen').on('click', function (){

    // $('.comicImg').attr('src',$(this).find('img').attr('src'));
    // $('.para').html($(this).find('img').attr('data-source'));
    $('#modal_input').attr('value',($(this).find('img').attr('data-source')));
    $('#myModalLabel').html($(this).find('img').attr('alt'));
    var folder_path = $(this).find('img').attr('data-source');
    $('.carousel-inner').empty();
    $('#myModal').modal('show');
    console.log(folder_path);
    // console.log("TO COMPARE: " + $('form').serialize());
    // console.log("TO COMPARE: " + folder_path);
    $.ajax({
            url: '/open_book',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
                printy(response,folder_path);


            },
            error: function(error) {
                console.log(error);
            }
        });


    });
});
// #########################



// $('#myModal').on('shown.bs.modal', function() {
//     $('#magnify').click(function(){

//         if($(this).hasClass('zoomed')){
//             $(this).removeClass('zoomed');
//             $(this).elevateZoom({
//                 zoomEnabled: false
//             });
//             // $('.zoomContainer').remove();

//         }else{
//             zoom();
//             $(this).addClass('zoomed');
//         }

       
//     });
// });


function zoom (){
    $("#zoom_07").elevateZoom({
    zoomType: 'lens',
    // zoomType: "inner",
    lensShape: "square",
    lensSize: 200,
    cursor: 'crosshair',
    responsive: true
    });
}



// ###################
var response;
var path;

function printy(response,path){
    console.log(response[1]);
    var len = Object.keys(response).length;
    console.log(len);
    for(var i=0; i < len; i++){
        var img_path = path + "/"+ response[i];
        // console.log(img_path);
        // console.log(jQuery.type(img_path));
        $('<div class="item "><img id="zoom_07" src="'+img_path+'" data-zoom-image="'+img_path+'" ><div class="carousel-caption" ></div>   </div>').appendTo('.carousel-inner');
        $('<li data-target="#carousel-example-generic" data-slide-to="'+i+'"></li>').appendTo('.carousel-indicators');

    }
    $('.item').first().addClass('active');
    $('.carousel-indicators > li').first().addClass('active');
    $('#carousel').carousel();
    
}


//Open Menu Trigger Function
$('a.sideTrigger').click(function() {
        $('body').toggleClass('sideOpen');
        return false;
    });

// Close Menu Trigger Function
$('span.a.closeTrigger').click(function() {
    $('body').toggleClass('sideOpen');
    return false;
});



//Footer stick to bottom with dynamic pages

$(function(){
    posFooter();
    function posFooter(){

        var padding_top = $('.footer').css("padding-top").replace("px","");
        var document_height = $(document.body).height() - padding_top;
        var window_height = $(window).height();
        var diff = window_height - document_height;

        if (diff <0){diff = 0;}

        $('.footer').css({
            padding: diff + "px 0 0 0"
        });
    }

    $(window).resize(posFooter);
});


$(function(){
    positionFooter(); 
    function positionFooter(){
        var padding_top = $(".footer").css("padding-top").replace("px", "");
        var page_height = $(document.body).height() - padding_top;
        var window_height = $(window).height();
        var difference = window_height - page_height;
        if (difference < 0)
            difference = 0;

        $(".footer").css({
            padding: difference + "px 0 0 0"
        });
    }

    $(window).resize(positionFooter);
});

// $('#carousel').carousel({
//     interval: 99999,
//     pause: false
// });
// $('.item').zoom({on:'mouseover'});
