document.addEventListener("DOMContentLoaded", function () {

  // Tag the body with a class on pages where we don't want the
  // integrated TOC to clutter the sidebar (Home and Screenshots).
  function tagBodyForTocSuppression() {
    var p = window.location.pathname;
    // strip trailing index.html if present
    p = p.replace(/index\.html$/, "");
    if (p === "/" || p === "/screenshots/") {
      document.body.classList.add("hide-integrated-toc");
    }
  }

  function init() {
    if (document.getElementById("nav-expand-btn")) return true;

    // Find the sidebar nav list - try multiple selectors
    var target =
      document.querySelector(".md-sidebar--primary .md-sidebar__inner .md-nav__list") ||
      document.querySelector(".md-sidebar--primary .md-nav__list") ||
      document.querySelector(".md-nav--primary .md-nav__list");

    if (!target) return false;

    var btn = document.createElement("button");
    btn.id = "nav-expand-btn";
    btn.textContent = "Expand all";

    var li = document.createElement("li");
    li.className = "md-nav__item";
    li.style.cssText = "padding:0.3rem 0.6rem 0.5rem; list-style:none;";
    li.appendChild(btn);
    target.insertBefore(li, target.firstChild);

    var expanded = false;
    btn.addEventListener("click", function () {
      expanded = !expanded;
      var toggles = document.querySelectorAll(".md-nav__toggle");
      for (var i = 0; i < toggles.length; i++) {
        toggles[i].checked = expanded;
      }
      btn.textContent = expanded ? "Collapse all" : "Expand all";
    });

    return true;
  }

  tagBodyForTocSuppression();
  if (!init()) { setTimeout(function(){ if(!init()) setTimeout(init, 1000); }, 300); }
});
