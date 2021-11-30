const ipCatalogo = "localhost:8001";

function getProducts(page, categoria) {
    $.ajax({
        url: 'http://' + ipCatalogo + "/productos?page=" + page + "&categoria=" + categoria,
        crossDomain: true,
        type: 'GET',
        success: function(response) {
            $.each(response.results, function(i, item) {
                $("#productos").append(
                    "<a href='/catalogo/" + item.categoria + "/" + item.slug + "' style='text-decoration:none;color:rgb(0, 0, 0)'><div class='col'><div class='card shadow-sm'><img src='" + item.imagenes[0] + "' width='100%' height='225'><div class='card-body'><p style='font-family: Berlin-Sans-Fb-Regular; font-size:20px; margin-bottom: 0px;'>" + item.nombre + "</p><p style='font-family: Berlin-Sans-Fb-Regular; font-size:20px; color:rgb(94, 128, 119); margin-bottom: -5px;'>$" + item.precio + "</p></div></div></div></a>"
                );
            });
        },
        error: function(data) {
            console.log(data);
        }
    });
}

function getCategorias() {
    $.ajax({
        url: 'http://' + ipCatalogo + "/categorias",
        crossDomain: true,
        type: 'GET',
        success: function(response) {
            $.each(response, function(i, categoria) {
                $('#categoria').append($('<option>', {
                    value: categoria.slug,
                    text: categoria.nombre
                }));
            });
        },
        error: function(data) {
            console.log(data);
        }
    });
}

function getSubcategorias(categoriaSel) {
    var categoria = categoriaSel.value;
    $.ajax({
        url: 'http://' + ipCatalogo + "/subcategorias?categoria=" + categoria,
        crossDomain: true,
        type: 'GET',
        success: function(response) {
            $("#subcategoria").empty();
            $('#subcategoria').append($('<option>', {
                value: null,
                text: null
            }));
            $.each(response, function(i, subcategoria) {
                $('#subcategoria').append($('<option>', {
                    value: subcategoria.slug,
                    text: subcategoria.nombre
                }));
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
            $("#image").attr("src", response.imagenes[0]);
            $("#nombre").text(response.nombre);
            $("#precio").text("$" + response.precio);
            $("#descripcion").text(response.descripcion);
            // for each other image excluding first in the array add a new image div
            $("#innerwrapper").css("width", 150*(response.imagenes.length-1)+"px");
            $.each(response.imagenes, function(i, imagen) {
                if (i > 0) {
                    $("#innerwrapper").append(
                        "<img class='img-flex' src='" + imagen + "' width='150px' height='100px'>"
                    );
                }
            });
        },
        error: function(data) {
            console.log(data);
        }
    });
}