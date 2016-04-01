var count = 2;
$(window).scroll(function(){
    if  (($(window).scrollTop() >= $(document).height() - $(window).height() - 65) && count <= number_pages){
        loadArticle(count);
        count ++;
    }

    function loadArticle(pageNumber){
        $.ajax({
            url: "?page=" + count,
            type:'GET',
            success: function(html){
                $("#blog_list").append(html);
            }
        });
        return false;
    }
});