if (document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
} else {
    ready()
}

function ready() {
    // PHONE MASK
    $('#id_phone_number').mask('+48-999-999-999');
    //
}
