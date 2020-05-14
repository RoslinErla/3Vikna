$(document).ready(function(){
    $('#search-btn').on('click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        console.log(searchText)
        $.ajax({
            url: '?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="one product"> 
                                <a href="/${d.id}">
                                    <img class="product-image" src="${d.firstImage}"/>
                                    <h4>${d.name}</h4>
                                    <p>${d.price} isk</p>                                 
                                </a>
                            </div>`
                });
                $('h4').empty()
                $('h1').empty()
                $('h2').empty()
                $('.product-details').remove()
                $('.show').empty()
                $('.total-cart').empty()
                $('.back-button').remove()
                $('#purchase').remove()
                $('.profile').remove()
                $('.btn-block').remove()
                $('.products').empty()
                $('.products').html(newHtml.join(''));
                $('#search-box').val();
            },
            error: function (xhr, status, error) {
                console.log(error);

            }
        })
    })
})

jQuery(function($) {
 let path = window.location.href; // because the 'href' property of the DOM element is the absolute path
  $('ul a').each(function() {
  if (this.href === path)
   $(this).addClass('active');
  })
 });




