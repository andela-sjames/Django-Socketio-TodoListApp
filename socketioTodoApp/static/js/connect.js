// function addTodoForm() {
//     $('#addtodo').on('submit', function(event) {
//         event.preventDefault();

//         var $form = $(this);
//         var fd = new FormData();
//         var form_data = $form.serializeArray();

//         $.each(form_data, function(key, input) {
//             fd.append(input.name, input.value);
//         });

//         $.ajax({
//             type: "POST",
//             url: $form.attr('action'),
//             data: fd,
//             contentType:false,
//             processData: false,

//             success: function(data) {

//                 if (data == "success") {
//                     console.log('success');
//                 }
//             },

//             error: function(error) {
//                 console.log(error.responseText);
//             },

//             headers: {
//                 "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val()
//             },

//         })

//     }
// }

// console.log("socket msg recieved  = " + msg);

// $('#messages').append($('<li>').text(msg));
// etc


$(document).ready(function(){

    // addTodoForm();


    $('#addtodoio').submit(function() {
        var value = $('#textarea1').val();

        if (value) {

            console.log(value);

            data = {action: 'add', message: value};

            socket.send(data);
        }
        $('#textarea1').val('').focus();
        return false;
    });

    var socket;
    var connected = function() {
        socket.subscribe('added');
    };

    var disconnected = function() {
        setTimeout(start, 1000);
    };

    var messaged = function(data) {
        console.log( data +' success');
         switch (data.action) {
            case 'done':
                console.log("socket msg recieved  = " + data);
                $('#messages').append($('<li>').text(data.name));
                break;

            case 'no':
                console.log(data.name);
         }
    }

    var start = function() {
        socket = new io.Socket();
        socket.connect();
        socket.on('connect', connected);
        socket.on('disconnect', disconnected);
        socket.on('message', messaged);
    };

    start();

})
