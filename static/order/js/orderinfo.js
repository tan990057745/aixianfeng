$(function () {
    $('.orderinfo').width(innerWidth)

    $('#pay').click(function () {
        console.log('支付')

        var identifier = $(this).attr('identifier')
        
        $.get('/pay/', {'identifier':identifier},function (response) {
            console.log(response['alipay_url'])
            window.open(response['alipay_url'], target='_self')
        })
    })
})