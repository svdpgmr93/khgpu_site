//  vanilla js for dropdown main menu
const menuLink = document.getElementById("#m-link-university");
const univerMenu = document.getElementById("#univer-menu");

const menuLinkEdu = document.getElementById("#m-link-education");
const eduMenu = document.getElementById("#edu-menu");

function menuOpen() {
  univerMenu.classList.toggle("d-none");
}

function menuOpenEdu() {
  eduMenu.classList.toggle("d-none");
}

menuLink.addEventListener("click", menuOpen);
univerMenu.addEventListener('mouseleave', menuOpen)

menuLinkEdu.addEventListener("click", menuOpenEdu);
eduMenu.addEventListener('mouseleave', menuOpenEdu)

// jquery for counter

function visible(partial) {
  var $t = partial,
    $w = jQuery(window),
    viewTop = $w.scrollTop(),
    viewBottom = viewTop + $w.height(),
    _top = $t.offset().top,
    _bottom = _top + $t.height(),
    compareTop = partial === true ? _bottom : _top,
    compareBottom = partial === true ? _top : _bottom;
  return (
    compareBottom <= viewBottom && compareTop >= viewTop && $t.is(":visible")
  );
}

function startCounter() {
  if ($(".counter").hasClass("counter-loaded")) return;
  $(".counter").addClass("counter-loaded");
  $(".counter").each(function () {
    var $this = $(this);
    jQuery({ Counter: 0 }).animate(
      { Counter: $this.text() },
      {
        duration: 2000,
        easing: "swing",
        step: function () {
          $this.text(Math.ceil(this.Counter));
        },
      }
    );
  });
}

$(document).ready(function () {
  // Check if the counter section is visible on page load
  if (visible($(".counter"))) {
    startCounter();
  }

  // Also start the counter on scroll if it becomes visible
  $(window).scroll(function () {
    if (visible($(".counter"))) {
      startCounter();
    }
  });
});
