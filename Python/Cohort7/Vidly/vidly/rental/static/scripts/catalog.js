var catalog = [];

function loadData() {
    $.ajax({
        url: '/api/movies',
        type: 'GET',
        success: (res) => {
            console.log('From server', res);

            catalog = res.objects;
            for(let i=0; i< res.objects.length; i++){
                var movie = res.objects[i];
                displayMovie(movie);
            }
        },
        error: (errorDetials) => {
            console.log(errorDetails);
        }
    });
}

function displayMovie(movie){
    var tr = 
    `<tr>
        <td align='center'><img src='/static/images/${movie.image}' width='120' </td>
        <td><a href="/movie/${movie.id}">${movie.title}</a></td>
        <td align='right'>${movie.release_year}</td>
        <td align='right'>${movie.price}</td>
        <td align='right'>${movie.in_stock}</td>
    </tr>`

    $(".catalog table tbody").append(tr);
}

function init(){
    console.log("Catalog page");
    loadData();
}

window.onload = init;