
var catalog = [];

function loadData() {
    $.ajax({
        url: '/api/movies',
        type: 'GET',
        success: (res) => {
            console.log('From server', res);
        },
        error: (errorDetials) => {
            console.log(errorDetails);
        }
    });
}

function init(){
    console.log("Catalog page");
    loadData();
}

window.onload = init;