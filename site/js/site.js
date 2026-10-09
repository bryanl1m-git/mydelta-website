/*
  MyDelta behaviour.

  Wired:
  - Manual hero slider. Three slides, previous / next / dots, no autoplay.
  - Mobile menu: focus trap, inert page, Escape, focus returned to the toggle.
  - Contact form opens WhatsApp, with a mailto link as the fallback.
    Nothing is posted to a server.

  The slider crossfade is 450ms in CSS, or instant under prefers-reduced-motion.
  The menu uses the same motion preference for its open and close fade.
*/

(function () {
  var toggle = document.querySelector("[data-nav-toggle]");
  var menu = document.getElementById("mobile-menu");
  var closeBtn = document.querySelector("[data-nav-close]");
  var menuPhase = "closed";
  var scrollY = 0;
  var MENU_MS = 320;

  function prefersReducedMotion() {
    return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  }

  function pageSurfaces() {
    return document.querySelectorAll(".skip-link, .site-header, main, .site-footer");
  }

  function setInert(on) {
    var nodes = pageSurfaces();
    for (var i = 0; i < nodes.length; i++) {
      if (on) nodes[i].setAttribute("inert", "");
      else nodes[i].removeAttribute("inert");
    }
  }

  function lockScroll() {
    scrollY = window.scrollY || document.documentElement.scrollTop || 0;
    document.body.style.position = "fixed";
    document.body.style.top = "-" + scrollY + "px";
    document.body.style.left = "0";
    document.body.style.right = "0";
    document.body.style.width = "100%";
  }

  function unlockScroll() {
    document.body.style.position = "";
    document.body.style.top = "";
    document.body.style.left = "";
    document.body.style.right = "";
    document.body.style.width = "";
    window.scrollTo(0, scrollY);
  }

  function focusable(container) {
    var nodes = container.querySelectorAll(
      "a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled])"
    );
    var list = [];
    for (var i = 0; i < nodes.length; i++) {
      if (nodes[i].tabIndex >= 0) list.push(nodes[i]);
    }
    return list;
  }

  function setMenu(open) {
    if (!menu || !toggle) return;
    if (open) {
      if (menuPhase === "open") return;
      menuPhase = "open";
      lockScroll();
      setInert(true);
      menu.removeAttribute("hidden");
      document.body.classList.add("menu-open");
      toggle.setAttribute("aria-expanded", "true");
      if (prefersReducedMotion()) {
        menu.classList.add("is-open");
      } else {
        menu.classList.remove("is-open");
        void menu.offsetWidth;
        menu.classList.add("is-open");
      }
      if (closeBtn) closeBtn.focus();
      return;
    }

    if (menuPhase === "closed" || menuPhase === "closing") return;
    menuPhase = "closing";
    menu.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");

    var done = false;
    function finish() {
      if (done) return;
      done = true;
      menu.setAttribute("hidden", "");
      setInert(false);
      document.body.classList.remove("menu-open");
      unlockScroll();
      menuPhase = "closed";
      toggle.focus();
    }

    if (prefersReducedMotion()) {
      finish();
      return;
    }

    function onEnd(event) {
      if (event.target !== menu || event.propertyName !== "opacity") return;
      menu.removeEventListener("transitionend", onEnd);
      finish();
    }

    menu.addEventListener("transitionend", onEnd);
    window.setTimeout(finish, MENU_MS + 80);
  }

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      setMenu(true);
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", function () {
      setMenu(false);
    });
  }

  if (menu) {
    menu.addEventListener("click", function (event) {
      var node = event.target;
      while (node && node !== menu) {
        if (node.tagName === "A") {
          setMenu(false);
          return;
        }
        node = node.parentNode;
      }
    });
  }

  document.addEventListener("keydown", function (event) {
    if (!menu || (menuPhase !== "open" && menuPhase !== "closing")) return;
    if (event.key === "Escape") {
      event.preventDefault();
      setMenu(false);
      return;
    }
    if (event.key !== "Tab") return;
    var items = focusable(menu);
    if (!items.length) return;
    var first = items[0];
    var last = items[items.length - 1];
    var active = document.activeElement;
    if (event.shiftKey && (active === first || !menu.contains(active))) {
      event.preventDefault();
      last.focus();
    } else if (!event.shiftKey && (active === last || !menu.contains(active))) {
      event.preventDefault();
      first.focus();
    }
  });

  var form = document.getElementById("enquiry-form");
  if (form) {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var data = new FormData(form);
      var parent = String(data.get("parent_name") || "").trim();
      var phone = String(data.get("phone") || "").trim();
      var service = String(data.get("service") || "").trim();
      var message = [
        "Hi MyDelta, I'd like to enquire.",
        "Parent: " + parent,
        "Phone: " + phone,
        "Service: " + service
      ].join("\n");
      var whatsapp = "https://wa.me/60126726140?text=" + encodeURIComponent(message);
      var mail = "mailto:mydeltaedu@gmail.com?subject=" +
        encodeURIComponent("MyDelta enquiry: " + service) +
        "&body=" + encodeURIComponent(message);
      var status = document.getElementById("enquiry-status");
      var mailLink = document.getElementById("enquiry-mailto");
      if (mailLink) {
        mailLink.href = mail;
        mailLink.hidden = false;
      }
      if (status) {
        status.textContent = "Opening WhatsApp with your enquiry. If it does not open, use the email link.";
      }
      var opened = window.open(whatsapp, "_blank", "noopener,noreferrer");
      if (!opened && status) {
        status.textContent = "WhatsApp did not open. Use the email link to send the same enquiry.";
      }
    });
  }

  function initSlider() {
    var hero = document.querySelector("[data-slider]");
    if (!hero) return;
    /* data-autoplay is ignored. This slider never advances on a timer. */
    var slides = hero.querySelectorAll("[data-slide]");
    var dots = hero.querySelectorAll(".hero__dots button");
    var prev = hero.querySelector("[data-slider-prev]");
    var next = hero.querySelector("[data-slider-next]");
    var chip = hero.querySelector("[data-slider-chip]");
    var status = hero.querySelector("[data-slider-status]");
    var count = slides.length;
    var index = 0;
    if (!count) return;

    for (var i = 0; i < count; i++) {
      slides[i].removeAttribute("hidden");
      slides[i].setAttribute("role", "group");
      slides[i].setAttribute("aria-roledescription", "slide");
      slides[i].setAttribute("aria-label", (i + 1) + " of " + count);
    }

    function show(nextIndex, moveDotFocus, announce) {
      var active = document.activeElement;
      var leaving = active && active.closest ? active.closest("[data-slide]") : null;
      index = (nextIndex % count + count) % count;
      for (var i = 0; i < count; i++) {
        var on = i === index;
        slides[i].classList.toggle("is-active", on);
        if (on) {
          slides[i].removeAttribute("aria-hidden");
          slides[i].removeAttribute("inert");
        } else {
          slides[i].setAttribute("aria-hidden", "true");
          slides[i].setAttribute("inert", "");
        }
        if (dots[i]) {
          dots[i].classList.toggle("is-active", on);
          if (on) dots[i].setAttribute("aria-current", "true");
          else dots[i].removeAttribute("aria-current");
          dots[i].tabIndex = on ? 0 : -1;
        }
      }
      if (chip) chip.textContent = (index + 1) + " / " + count;
      if (announce && status) {
        status.textContent = "Slide " + (index + 1) + " of " + count;
      }
      if (moveDotFocus && dots[index]) {
        dots[index].focus();
      } else if (leaving && leaving !== slides[index] && dots[index]) {
        dots[index].focus();
      }
    }

    show(0, false, false);

    if (prev) {
      prev.addEventListener("click", function () {
        show(index - 1, false, true);
      });
    }
    if (next) {
      next.addEventListener("click", function () {
        show(index + 1, false, true);
      });
    }
    for (var d = 0; d < dots.length; d++) {
      (function (dotIndex) {
        dots[dotIndex].addEventListener("click", function () {
          show(dotIndex, false, true);
        });
      })(d);
    }

    hero.addEventListener("keydown", function (event) {
      if (event.key !== "ArrowLeft" && event.key !== "ArrowRight") return;
      var target = event.target;
      if (!target || !hero.contains(target)) return;
      var tag = target.tagName;
      if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
      event.preventDefault();
      var fromDot = target.parentNode && target.parentNode.classList.contains("hero__dots");
      show(index + (event.key === "ArrowRight" ? 1 : -1), fromDot, true);
    });

    var tracking = false;
    var startX = 0;
    var startY = 0;
    var deltaX = 0;
    var deltaY = 0;
    var axis = "";
    var startTarget = null;

    hero.addEventListener("touchstart", function (event) {
      if (event.touches.length !== 1) {
        tracking = false;
        return;
      }
      tracking = true;
      axis = "";
      startTarget = event.target;
      startX = event.touches[0].clientX;
      startY = event.touches[0].clientY;
      deltaX = 0;
      deltaY = 0;
    }, { passive: true });

    hero.addEventListener("touchmove", function (event) {
      if (!tracking || !event.touches.length) return;
      deltaX = event.touches[0].clientX - startX;
      deltaY = event.touches[0].clientY - startY;
      if (!axis) {
        if (Math.abs(deltaX) < 8 && Math.abs(deltaY) < 8) return;
        axis = Math.abs(deltaX) > Math.abs(deltaY) ? "x" : "y";
      }
      if (axis === "x") event.preventDefault();
    }, { passive: false });

    function endSwipe() {
      if (!tracking) return;
      var horizontal = axis === "x" && Math.abs(deltaX) >= 40;
      var onControl = startTarget && startTarget.closest && startTarget.closest("button, a");
      tracking = false;
      if (!horizontal || onControl) return;
      show(index + (deltaX < 0 ? 1 : -1), false, true);
    }

    hero.addEventListener("touchend", endSwipe);
    hero.addEventListener("touchcancel", function () {
      tracking = false;
    });
  }

  initSlider();
})();
