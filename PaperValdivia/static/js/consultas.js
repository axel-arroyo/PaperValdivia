var ipUsers = "localhost:8001";
var ipCatalogo = "localhost:8002";


function login() {
    var parametros = {
        "username": $("#username").val(),
        "password": $("#password").val()
    }
    $.ajax({
        data: parametros,
        url: 'http://' + ipUsers + "/login",
        crossDomain: true,
        type: 'POST',
        success: function(response) {
            $.each(response, function(i, item) {
                localStorage.setItem(i, item);
            });
        },
        error: function(data) {
            console.log(data);
        }
    });
};


function getProducts() {
    $.ajax({
        url: 'http://' + ipCatalogo + "/productos",
        crossDomain: true,
        type: 'GET',
        success: function(response) {
            console.log(response);
            $.each(response, function(i, item) {
                $("#productos").append(
                    "<a href='/catalogo/" + item.categoria + "/" + item.slug + "' style='text-decoration:none;color:rgb(0, 0, 0)'><div class='col'><div class='card shadow-sm'><img src='" + item.imagen_url + "' width='100%' height='225'><div class='card-body'><p style='font-family: Berlin-Sans-Fb-Regular; font-size:20px; margin-bottom: 0px;'>" + item.nombre + "</p><p style='font-family: Berlin-Sans-Fb-Regular; font-size:20px; color:rgb(94, 128, 119); margin-bottom: -5px;'>$" + item.precio + "</p></div></div></div></a>"
                );
            });
        },
        error: function(data) {
            console.log(data);
        }
    });
}

function getProductInfo(producto, categoria) {
    $.ajax({
        url: 'http://' + ipCatalogo + "/productos" + "?producto=" + producto,
        crossDomain: true,
        type: 'GET',
        success: function(response) {
            console.log(response);
            $("#image").attr("src", response.imagen_url);
            $("#nombre").text(response.nombre);
            $("#precio").text("$" + response.precio);
            $("#descripcion").text(response.descripcion);
        },
        error: function(data) {
            console.log(data);
        }
    });
}