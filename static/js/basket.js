$('.basket_list').on('click', 'input[type=number]',function(event){
    let pk = event.target.name;
    let quantity = event.target.value;
    $.ajax({
        url: `/basket/edit/${pk}/${quantity}/`,
        success: function (data) {
            $('.basket_list').html(data.result);
        }
    });
});
