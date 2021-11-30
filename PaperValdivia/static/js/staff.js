const ipCatalogo = "localhost:8001";

function fillPanel(){
    $.ajax({
        url: 'http://' + ipCatalogo + "/productos",
        crossDomain: true,
        type: 'GET',
        success: function(response) {
            $.each(response.results, function(i, item) {
                $("#table").append(
                    "<tr><th scope='row'><input type='checkbox' /></th><td>"+ item.nombre + "</td><td>"+ item.categoria + "</td><td>$"+ item.precio +"</td><td>" + item.vendidos + "</td><td>" + item.stock + " </td><td><a href='#' class='tm-product-delete-link'><i class='far fa-trash-alt tm-product-delete-icon'></i></a></td></tr>"
                );
            });
        },
        error: function(data) {
            console.log(data);
        }
    });
}

function postProduct(form) {
    var parametros = {
        "nombre": form.nombre.value,
        "precio": form.precio.value,
        "descripcion": form.descripcion.value,
        "categoria": form.categoria.value,
        "subcategoria": form.subcategoria.value,
        "imagenes": form.imagenes.value
    }
    $.ajax({
        data: parametros,
        url: 'http://' + ipCatalogo + "/productos",
        crossDomain: true,
        type: 'POST',
        datatype: 'multipart/form-data',
        enctype: 'multipart/form-data',
        success: function(response) {
            console.log(response);
            window.location.href = "/staff/panel";
        },
        error: function(data) {
            console.log(data);
        }
    });
}

function postCategoria(form) {
    $.ajax({
        data: {
            "nombre": form.nombre.value,
        },
        url: 'http://' + ipCatalogo + "/categorias",
        crossDomain: true,
        type: 'POST',
        success: function(response) {
            window.location.href = "/staff/panel";
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
