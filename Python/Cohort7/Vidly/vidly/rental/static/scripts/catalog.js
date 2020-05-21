
var catalog = [];

function loadData() {
    $.ajax({
        url: '/api/movies',
        type: 'GET',
        success: (res) => {
            console.log('From server', res);

            for(let i=0; i< res.objects.length; i++){
                var movie = res.objects[i];
            }
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