// This is a manifest file that'll be compiled into application.js, which will include all the files
// listed below.
//
// Any JavaScript/Coffee file within this directory, lib/assets/javascripts, or any plugin's
// vendor/assets/javascripts directory can be referenced here using a relative path.
//
// It's not advisable to add code directly here, but if you do, it'll appear at the bottom of the
// compiled file. JavaScript code in this file should be added after the last require_* statement.
//
// Read Sprockets README (https://github.com/rails/sprockets#sprockets-directives) for details
// about supported directives.
//
//= require jquery3
//= require popper
//= require rails-ujs
//= require bootstrap-sprockets
//= require_tree .

$(document).ready(function () {
  // Dropdown menu
  $(".sidebar-dropdown > a").click(function () {
    $(".sidebar-submenu").slideUp(200);
    if ($(this).parent().hasClass("active")) {
      $(".sidebar-dropdown").removeClass("active");
      $(this).parent().removeClass("active");
    } else {
      $(".sidebar-dropdown").removeClass("active");
      $(this).next(".sidebar-submenu").slideDown(200);
      $(this).parent().addClass("active");
    }

  });

  //toggle sidebar
  $("#toggle-sidebar").click(function () {
    $(".page-wrapper").toggleClass("toggled");
  });
  // //Pin sidebar
  // $("#pin-sidebar").click(function () {
  //   if ($(".page-wrapper").hasClass("pinned")) {
  //     // unpin sidebar when hovered
  //     $(".page-wrapper").removeClass("pinned");
  //     $("#sidebar").unbind( "hover");
  //   } else {
  //     $(".page-wrapper").addClass("pinned");
  //     $("#sidebar").hover(
  //       function () {
  //         console.log("mouseenter");
  //         $(".page-wrapper").addClass("sidebar-hovered");
  //       },
  //       function () {
  //         console.log("mouseout");
  //         $(".page-wrapper").removeClass("sidebar-hovered");
  //       }
  //     )
  //
  //   }
  // });


  //toggle sidebar overlay
  $("#overlay").click(function () {
    $(".page-wrapper").toggleClass("toggled");
  });

  //switch between themes
  var themes = "default-theme legacy-theme chiller-theme ice-theme cool-theme light-theme";
  $('[data-theme]').click(function () {
    $('[data-theme]').removeClass("selected");
    $(this).addClass("selected");
    $('.page-wrapper').removeClass(themes);
    $('.page-wrapper').addClass($(this).attr('data-theme'));
  });

  // switch between background images
  var bgs = "bg1 bg2 bg3 bg4";
  $('[data-bg]').click(function () {
    $('[data-bg]').removeClass("selected");
    $(this).addClass("selected");
    $('.page-wrapper').removeClass(bgs);
    $('.page-wrapper').addClass($(this).attr('data-bg'));
  });

  // toggle background image
  $("#toggle-bg").change(function (e) {
    e.preventDefault();
    $('.page-wrapper').toggleClass("sidebar-bg");
  });

  // toggle border radius
  $("#toggle-border-radius").change(function (e) {
    e.preventDefault();
    $('.page-wrapper').toggleClass("boder-radius-on");
  });

  //custom scroll bar is only used on desktop
  if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    $(".page-wrapper").toggleClass("toggled");
  }
});