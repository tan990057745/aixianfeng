$(function () {
    $('.market').width(innerWidth)

    // cookie()设置之前导入的重要步骤，导入cookie.js文件
    // 获取typeIndex
    typeIndex = $.cookie('typeIndex')
    if (typeIndex){ // 已经有点击分类
        $('.type-slider .type-item').eq(typeIndex).addClass('active')
    } else {    // 没有点击分类
        // 没有点击默认第一个
        $('.type-slider .type-item:first').addClass('active')
    }

    $('.type-item').click(function () {
        $.cookie('typeIndex', $(this).index(), {expires:3, path:'/'})
    })

    // 分类按钮
    categoryBt = false  // 默认是隐藏
    $('#categoryBt').click(function () {
        // 取反
        categoryBt = !categoryBt

        categoryBt ? categoryViewShow() : categoryViewHide()

    })


    // 排序按钮
    sortBt = false  // 默认是隐藏
    $('#sortBt').click(function () {
        // 取反
        sortBt = !sortBt

        sortBt ? sortViewShow() : sortViewHide()
    })

    // 灰色蒙层
    $('.bounce-view').click(function () {
        sortBt = false
        sortViewHide()
        categoryBt = false
        categoryViewHide()
    })

    function categoryViewShow() {
        sortBt = false
        sortViewHide()
        $('.bounce-view.category-view').show()
        $('#categoryBt i').removeClass('glyphicon-triangle-top').addClass('glyphicon-triangle-bottom')
    }
    function categoryViewHide() {
        $('.bounce-view.category-view').hide()
        $('#categoryBt i').removeClass('glyphicon-triangle-bottom').addClass('glyphicon-triangle-top')
    }

    function sortViewShow() {
        categoryBt = false
        categoryViewHide()
        $('.bounce-view.sort-view').show()
        $('#sortBt i').removeClass('glyphicon-triangle-top').addClass('glyphicon-triangle-bottom')
    }
    function sortViewHide() {
        $('.bounce-view.sort-view').hide()
        $('#sortBt i').removeClass('glyphicon-triangle-bottom').addClass('glyphicon-triangle-top')
    }
})