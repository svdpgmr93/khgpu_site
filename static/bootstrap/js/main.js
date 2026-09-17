// document.addEventListener("DOMContentLoaded", () => {
//   const myAccordionItems = document.querySelectorAll(".my-accordion-item");

//   myAccordionItems.forEach((item) => {
//     const header = item.querySelector(".my-accordion-header");
//     const content = item.querySelector(".my-accordion-content");
//     header.addEventListener('click', () => {
//       const isActive = item.classList.contains('active');
//       if (isActive) {
//         item.classList.remove('active');
//         header.classList.remove('active');
//         return
//       }
//       myAccordionItems.forEach((otherItem) => {
//         otherItem.classList.remove('active');
//         const otherHeader = otherItem.querySelector('.my-accordion-header');
//         if (otherHeader) otherHeader.classList.remove('active');
//       });
//       item.classList.add('active')
//       header.classList.add('active')
//     });
//   });
// });

// script for accordion

// Yellow background for institute card
const yellowBg = document.querySelector('.yellow-bg')
if (yellowBg) {
  yellowBg.style.backgroundColor = '#ffaa00';
}

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
univerMenu.addEventListener("mouseleave", menuOpen);

menuLinkEdu.addEventListener("click", menuOpenEdu);
eduMenu.addEventListener("mouseleave", menuOpenEdu);

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


// Play video script

const vid = document.getElementById('#vid_1');
const btnPlay = document.getElementById('#btnPlay1');
const hideElems = document.querySelectorAll('.videoverlay')

if (btnPlay) {
  btnPlay.addEventListener('click', () => {
  hideElems.forEach(hideElem => hideElem.classList.add('d-none'));
  vid.src += '&autoplay=1'
})
}

// carousel jquery antiterror 

const antiterror_carousel = document.getElementById('antiterror_carousel')
const antiterror_carousel_2 = document.getElementById('antiterror_carousel_2')
if (antiterror_carousel) {
  $("#antiterror_carousel").owlCarousel({
  itemsCustom: [
    [0, 1],
    [300, 1],
    [700, 2],
    [950, 2],
    [1200, 3],
  ],
});
}

if (antiterror_carousel_2) {
  $("#antiterror_carousel_2").owlCarousel({
  itemsCustom: [
    [0, 1],
    [300, 1],
    [700, 2],
    [950, 2],
    [1200, 3],
  ],
});
}


$(document).ready(function(){
  $('#cpp_carousel').owlCarousel({
    loop:true,
    margin:40,
    nav:true,
    dots: false,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:true,
    smartSpeed: 1500,
    navText: [
      '<svg width="24" height="24"><path d="M15 3l-9 9 9 9" fill="none" stroke="#ffffff" stroke-width="2"/></svg>',
      '<svg width="24" height="24"><path d="M9 3l9 9-9 9" fill="none" stroke="#ffffff" stroke-width="2"/></svg>'
    ],
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:3
        }
    }
})
});

$(document).ready(function(){
  $('#cpp_carousel_2').owlCarousel({
    items: 2,
    loop:false,
    margin:20,
    nav:true,
    dots: false,
    autoplay:false,
    navText: [
      '<svg width="24" height="24"><path d="M15 3l-9 9 9 9" fill="none" stroke="#ffffff" stroke-width="2"/></svg>',
      '<svg width="24" height="24"><path d="M9 3l9 9-9 9" fill="none" stroke="#ffffff" stroke-width="2"/></svg>'
    ],
})
});

$(document).ready(function(){
  $('#rector_page_news_carousel').owlCarousel({
    items: 3,
    loop:false,
    margin:40,
    nav:true,
    dots: false,
    autoplay:false,
    navText: [
      '<svg width="24" height="24"><path d="M15 3l-9 9 9 9" fill="none" stroke="#ffffff" stroke-width="2"/></svg>',
      '<svg width="24" height="24"><path d="M9 3l9 9-9 9" fill="none" stroke="#ffffff" stroke-width="2"/></svg>'
    ],
})
});

// аудио-дорожка
// const player = document.getElementById('player');
//       const audio = document.getElementById('track');
//       const timeDisplay = document.getElementById('time');
//       const barsContainer = document.getElementById('bars');
//       const progressOverlay = document.getElementById('progressOverlay');

//       // Создаем 64 колонки
//       const barCount = 64;
//       for (let i = 0; i < barCount; i++) {
//         const bar = document.createElement('div');
//         bar.className = 'bar';
//         barsContainer.appendChild(bar);
//       }
//       const bars = barsContainer.querySelectorAll('.bar');

//       let audioCtx = null;
//       let analyser = null;
//       let source = null;
//       let dataArray = null;

//       function initAudioAPI() {
//         if (!audioCtx) {
//           audioCtx = new (window.AudioContext || window.webkitAudioContext)();
//           analyser = audioCtx.createAnalyser();
//           analyser.fftSize = 128;
//           const bufferLength = analyser.frequencyBinCount;
//           dataArray = new Uint8Array(bufferLength);
//         }
//       }

//       function togglePlay() {
//         if (audio.paused || audio.ended) {
//           audio.play();
//           player.classList.add('active');
//           initAudioAPI();
//           if (source) source.disconnect();
//           source = audioCtx.createMediaElementSource(audio);
//           source.connect(analyser);
//           source.connect(audioCtx.destination);
//           animateVisualizer();
//         } else {
//           audio.pause();
//           player.classList.remove('active');
//         }
//       }

//       function animateVisualizer() {
//         if (!player.classList.contains('active')) return;

//         analyser.getByteFrequencyData(dataArray);

//         bars.forEach((bar, i) => {
//           const height = (dataArray[i] / 255) * 100;
//           bar.style.height = `${height}%`;
//         });

//         requestAnimationFrame(animateVisualizer);
//       }

//       audio.addEventListener('timeupdate', () => {
//         const current = audio.currentTime;
//         const duration = audio.duration;
//         const percent = duration ? (current / duration) * 100 : 0;
//         progressOverlay.style.width = `${percent}%`;

//         const formatTime = (seconds) => {
//           const mins = Math.floor(seconds / 60);
//           const secs = Math.floor(seconds % 60);
//           return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
//         };
//         timeDisplay.textContent = formatTime(current);
//       });

//       audio.addEventListener('ended', () => {
//         player.classList.remove('active');
//         timeDisplay.textContent = '00:00';
//         progressOverlay.style.width = '0%';
//       });