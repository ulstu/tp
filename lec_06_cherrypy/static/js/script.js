
show_image_editor = function(file_name) {
    var url = "/get_image?file_name=" + file_name + "&q=" + Math.random();
    var canvas = document.getElementById('image_canvas');
    ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    img = new Image;
    img.onload = function(){
        scale = Math.min(canvas.width / img.width, canvas.height / img.height);
        ctx.drawImage(img, 0, 0, img.width * scale, img.height * scale);
    };
    img.src = url;
    $("#edit_dialog").dialog({
        draggable: false, 
        resizable: false,
        modal: true,
        width: 680,
        height: 570,
            buttons: {
                'OK': function() {
                    $( this ).dialog( "close" );
                }
            }

    });
}

fill_image_list = function() {
    $.getJSON('/get_all_images', function(data) {
        console.log("data received: " + JSON.stringify(data));
        $("#imageList").html("");
        $.each(data.images, function(i, item) {
            console.log(i, item);
            var idpart = data.images[i].file_name.replace(".", "_");
            $('<div class="col-md-3">').html(
                "<div class='card mb-1 shadow-sm center'>" +
                    "<a id='a" + idpart + "' href='javascript:show_image_editor(\"" + data.images[i].file_name + "\")'>"+
                    "<img id='img" + idpart + "' class='bd-placeholder-img card-img-top' src='/get_image?file_name=" + data.images[i].file_name + "&thumbnail=1' alt='image'/>" +
                    "</a>" +
                    "<div class='card-body'><p class='cart-text'>" + data.images[i].file_name + "<br /></p></div>"+
                "</div>"
            ).appendTo('#imageList');
        });
    });
}

$(document).ready(function(){
    fill_image_list();
});
