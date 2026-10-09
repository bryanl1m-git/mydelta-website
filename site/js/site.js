/*
  MyDelta session 1 behaviour.

  Wired now:
  - Mobile menu open/close (basic).
  - Contact form opens WhatsApp, with a mailto link as the fallback.
    Nothing is posted to a server.

  TODO session 2 — hero slider (manual, 3 slides, no autoplay):
  - Read [data-slider] on the home hero. Slides 2 and 3 are in the DOM with hidden.
  - Desktop: previous/next buttons, dots, and the 01 / 03 counter.
  - Mobile: no arrows. Swipe, about 40px, without blocking vertical scroll.
  - Dots and arrows are buttons. Left/Right keys change the slide.
  - Transition 400–500ms. prefers-reduced-motion: instant.
  - Do not add autoplay.

  TODO session 2 — mobile menu polish:
  - Trap Tab inside the open menu, and mark the page inert.
  - Restore scroll position and animate the overlay.
  - Match the mobile menu frame once it is exported.
*/

(function () {
  var toggle = document.querySelector("[data-nav-toggle]");
  var menu = document.getElementById("mobile-menu");
  var closeBtn = document.querySelector("[data-nav-close]");

  function setMenu(open) {
    if (!menu || !toggle) return;
    if (open) {
      menu.removeAttribute("hidden");
      toggle.setAttribute("aria-expanded", "true");
      document.body.classList.add("menu-open");
      if (closeBtn) closeBtn.focus();
    } else {
      menu.setAttribute("hidden", "");
      toggle.setAttribute("aria-expanded", "false");
      document.body.classList.remove("menu-open");
      toggle.focus();
    }
  }

  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      setMenu(menu.hasAttribute("hidden"));
    });
  }

  if (closeBtn) {
    closeBtn.addEventListener("click", function () {
      setMenu(false);
    });
  }

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && menu && !menu.hasAttribute("hidden")) {
      setMenu(false);
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
    /* TODO session 2: manual 3-slide slider. No autoplay. See the file header. */
  }

  initSlider();
})();
