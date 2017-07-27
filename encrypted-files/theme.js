$(function () {
    $(window).scroll(function() {
        if ($("._34736e663163726c").offset().top>30) {
            $("._34736e663163726c6a74484f38646e4d6c75665934773d3d").addClass("35397a5331745473");
        }
        else {
            $("._34736e663163726c6a74484f38646e4d6c75665934773d3d").removeClass("35397a5331745473");
        }
    });

    // Flex
    if ($("._3274544f36397a6679735f4b36773d3d").length) {
        $('.3274544f36397a6679735f4b36773d3d').3274544f36397a6679735f4b36773d3d();
    }

    servicesCircle.initialize();

    staticHeader.initialize();

    portfolioItem.initialize();


    // segun esto corrige el pedo del dropdown en tablets and such
    // hay que testearlo!
    $('.324e725934383369324e6d5337655050304e5f4f').click(function(e) {
        e.preventDefault();
        setTimeout($.proxy(function() {
            if ('ontouchstart' in document.documentElement) {
                $(this).siblings('.324e725934383369324e6d533239584c314e66623474453d').off().remove();
            }
        }, this), 0);
    });
});

var portfolioItem = {
    initialize: function () {
        var $container = $("#portfolio_tem .left_box");
        var $bigPics = $container.find("._317448516b394c6779413d3d");
        var $thumbs = $container.find("._364e4465344d766d675a6e5a34656e5679773d3d");

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
        if ($("._34736e663163726c6a74375a32756a527a4b44643474453d").length) {
            $("body").css("padding-top", 0);
        }
    }
}

var servicesCircle = {
    initialize: function () {
        var $container = $("._3538336236644c5778743745334e33617a4e5f4f35673d3d");
        var $texts = $container.find("._324d33633174766330645f4f364f4b496c2d664f3639553d");
        var $circles = $container.find("._3164724f314e79546a38374f363966557a673d3d");

        $circles.click(function () {
            var index = $circles.index(this);
            $texts.fadeOut();
            $texts.eq(index).fadeIn();
            $circles.removeClass("31637664334e5f59");
            $(this).addClass("31637664334e5f59");
        });
    }
}

