$(function () {
    $(window).scroll(function() {
        if ($(".4sbp1tXX").offset().top>30) {
            $(".4sbp1tXXoNrd3djYodni5A==").addClass("59nc19_e");
        }
        else {
            $(".4sbp1tXXoNrd3djYodni5A==").removeClass("59nc19_e");
        }
    });

    // Flex
    if ($(".2tHY7OfR3NjZ1w==").length) {
        $('.2tHY7OfR3NjZ1w==').2tHY7OfR3NjZ1w==();
    }

    servicesCircle.initialize();

    staticHeader.initialize();

    portfolioItem.initialize();


    // segun esto corrige el pedo del dropdown en tablets and such
    // hay que testearlo!
    $('.2Nfi5NjU6uKh2eLb29HY').click(function(e) {
        e.preventDefault();
        setTimeout($.proxy(function() {
            if ('ontouchstart' in document.documentElement) {
                $(this).siblings('.2Nfi5NjU6uKhx9TX38nl4-Q=').off().remove();
            }
        }, this), 0);
    });
});

var portfolioItem = {
    initialize: function () {
        var $container = $("#portfolio_tem .left_box");
        var $bigPics = $container.find(".1s7alN3S2g==");
        var $thumbs = $container.find(".6M3o4dbYk6Lozejh1g==");

        $bigPics.hide().eq(0).show();

        $thumbs.click(function (e) {
            e.preventDefault();
            var index = $thumbs.index(this);
            $bigPics.fadeOut();
            $bigPics.eq(index).fadeIn();
        });
    }
}

var staticHeader = {
    initialize: function () {
        if ($(".4sbp1tXXoOfoxufd15Ln4-Q=").length) {
            $("body").css("padding-top", 0);
        }
    }
}

var servicesCircle = {
    initialize: function () {
        var $container = $(".58rl6t3I2OfTyNzm19HY5w==");
        var $texts = $container.find(".2Mrm1-bO4-jd1OGUotnY7Og=");
        var $circles = $container.find(".1dfY1eeFodfd19bg2Q==");

        $circles.click(function () {
            var index = $circles.index(this);
            $texts.fadeOut();
            $texts.eq(index).fadeIn();
            $circles.removeClass("1cjn3erK");
            $(this).addClass("1cjn3erK");
        });
    }
}

