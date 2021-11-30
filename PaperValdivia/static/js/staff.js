const editIcon = "http://localhost:8000/static/images/edit.png";

function deleteCategoria(categoria) {
    $.ajax({
        url: 'http://' + ipCatalogo + "/categorias/destroy/" + categoria,
        crossDomain: true,
        type: 'DELETE',
        success: function(response) {
            window.location.href = "/staff/panel";
        }
    });
}

function fillPanel(){
    $.ajax({
        url: 'http://' + ipCatalogo + "/listProducts",
        crossDomain: true,
        type: 'GET',
        success: function(response) {
            console.log(response);
            $.each(response.results, function(i, item) {
                $("#table").append(
                    "<tr onclick='trclick(event)' id="+i+"><td><input type='checkbox' /></td><td>"+i+"</td><td>"+ item.nombre + "</td><td>"+ item.categoria + "</td><td>"+ item.subcategoria + "</td><td>"+ item.precio +"</td><td>" + item.vendidos + "</td><td>" + item.stock + " </td><td><a href='edit/"+item.slug+"'><img src="+editIcon+" width='20px' height='auto'/></a></td></tr>"
                );
            });
        },
        error: function(data) {
            console.log(data);
        }
    });
}

function getProductInfo(producto) {
    $.ajax({
        url: 'http://' + ipCatalogo + "/listProducts" + "?producto=" + producto,
        crossDomain: true,
        type: 'GET',
        success: function(response) {
            item = response.results[0];
            // fill input values
            $("#nombre").val(item.nombre);
            $("#precio").val(item.precio);
            $("#descripcion").val(item.descripcion);
            $("#categoria").val(item.categoria);
            // add actual option to categoria
            $('#categoria').append($('<option>', {
                value: item.categoria,
                text: item.categoria
            }));
            $("#subcategoria").val(item.subcategoria);
            // add actual option to subcategoria
            $('#subcategoria').append($('<option>', {
                value: item.subcategoria,
                text: item.subcategoria
            }));
            $("#stock").val(item.stock);

        },
        error: function(data) {
            console.log(data);
        }
    });
}

function postProduct(formData) {
    console.log(formData);
    $.ajax({
        data: formData,
        url: 'http://' + ipCatalogo + "/productos",
        crossDomain: true,
        type: 'POST',
        processData: false,
        contentType: false,
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
