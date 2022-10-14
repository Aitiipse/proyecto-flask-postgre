function obtenerdatos(id){
    document.getElementById('formulario').action='/editar_persona/'+id
    document.getElementById('boton_form').innerHTML='Actualizar'
    nombreactual=document.getElementById('table_nombre'+id).innerHTML
    apellidoactual=document.getElementById('table_apellido'+id).innerHTML
    edadactual=document.getElementById('table_edad'+id).innerHTML
    document.getElementById('nombre').value =nombreactual
    document.getElementById('apellido').value =apellidoactual
    document.getElementById('edad').value =edadactual
}