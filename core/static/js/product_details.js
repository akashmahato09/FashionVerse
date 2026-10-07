document.addEventListener("DOMContentLoaded", () => {
  const mainImg = document.getElementById("mainProductImg");
  const zoomContainer = document.getElementById("zoomContainer");
  const thumbButtons = document.querySelectorAll(".thumb-btn");
  const colorSwatches = document.querySelectorAll(".color-swatch-item");
  const colorLabel = document.getElementById("activeColorName");
  const sizeBoxes = document.querySelectorAll(".size-box:not(.out-of-stock)");
  const qtyInput = document.getElementById("quantityInput");
  const qtyMinus = document.getElementById("qtyMinus");
  const qtyPlus = document.getElementById("qtyPlus");
  const pincodeBtn = document.getElementById("pincodeCheckBtn");
  const pincodeInput = document.getElementById("pincodeField");
  const deliveryStatus = document.getElementById("deliveryStatus");

  /* ========================================================
     HELPER: Activate Swatch by Color Name
  ======================================================== */
  function selectColorByName(colorName) {
    if (!colorName) return;

    colorSwatches.forEach((swatch) => {
      const isMatch = swatch.getAttribute("data-color") === colorName;
      swatch.classList.toggle("active", isMatch);

      const radio = swatch.querySelector('input[type="radio"]');
      if (radio) {
        radio.checked = isMatch;
      }
    });

    if (colorLabel) {
      colorLabel.innerText = colorName;
    }
  }

  /* ========================================================
     1. Click Thumbnail -> Update Main Image & Active Swatch
  ======================================================== */
  thumbButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const newImg = btn.getAttribute("data-img");
      const associatedColor = btn.getAttribute("data-color");

      // Update main picture
      if (newImg && mainImg) {
        mainImg.src = newImg;
      }

      // Highlight clicked thumbnail
      thumbButtons.forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");

      // Activate matching swatch, radio input, and label
      selectColorByName(associatedColor);
    });
  });

  /* ========================================================
     2. Click Swatch -> Update Swatch, Main Image & Thumbnail
  ======================================================== */
  colorSwatches.forEach((swatch) => {
    swatch.addEventListener("click", function () {
      const colorName = this.getAttribute("data-color");
      const swatchImg = this.getAttribute("data-img");

      // Activate swatch, radio, and label
      selectColorByName(colorName);

      // Update main picture
      if (swatchImg && mainImg) {
        mainImg.src = swatchImg;
      }

      // Highlight matching thumbnail
      thumbButtons.forEach((btn) => {
        const match =
          btn.getAttribute("data-color") === colorName ||
          btn.getAttribute("data-img") === swatchImg;
        btn.classList.toggle("active", match);
      });
    });
  });

  /* ========================================================
     3. Smooth Cursor Zoom on Main Image
  ======================================================== */
  if (zoomContainer && mainImg) {
    zoomContainer.addEventListener("mousemove", (e) => {
      const rect = zoomContainer.getBoundingClientRect();
      const x = ((e.clientX - rect.left) / rect.width) * 100;
      const y = ((e.clientY - rect.top) / rect.height) * 100;
      mainImg.style.transformOrigin = `${x}% ${y}%`;
      mainImg.style.transform = "scale(1.7)";
    });

    zoomContainer.addEventListener("mouseleave", () => {
      mainImg.style.transform = "scale(1)";
      mainImg.style.transformOrigin = "center center";
    });
  }

  /* ========================================================
     4. Size Pill Selection
  ======================================================== */
  sizeBoxes.forEach((box) => {
    box.addEventListener("click", function () {
      sizeBoxes.forEach((item) => item.classList.remove("active"));
      this.classList.add("active");
      const radio = this.querySelector('input[type="radio"]');
      if (radio) radio.checked = true;
    });
  });

  /* ========================================================
     5. Quantity Controller Stepper
  ======================================================== */
  if (qtyMinus && qtyPlus && qtyInput) {
    qtyMinus.addEventListener("click", () => {
      let currentVal = parseInt(qtyInput.value, 10) || 1;
      if (currentVal > 1) {
        qtyInput.value = currentVal - 1;
      }
    });

    qtyPlus.addEventListener("click", () => {
      let currentVal = parseInt(qtyInput.value, 10) || 1;
      if (currentVal < 10) {
        qtyInput.value = currentVal + 1;
      }
    });
  }

  /* ========================================================
     6. Pincode Availability Checker
  ======================================================== */
  if (pincodeBtn && pincodeInput && deliveryStatus) {
    pincodeBtn.addEventListener("click", () => {
      const pin = pincodeInput.value.trim();
      if (/^\d{6}$/.test(pin)) {
        deliveryStatus.className = "delivery-status success";
        deliveryStatus.innerHTML = `<i class="fa-solid fa-truck-ramp-box"></i> Delivery available to <strong>${pin}</strong>. Estimated arrival: <strong>2-3 Days</strong>. Cash on Delivery is eligible.`;
      } else {
        deliveryStatus.className = "delivery-status error";
        deliveryStatus.innerText = "Please enter a valid 6-digit Indian postal code.";
      }
    });
  }
});

/* ========================================================
   7. Wishlist Submission
======================================================== */
function toggleWishlist() {
  const wishlistBtn = document.getElementById("wishlistBtn");
  const form = document.getElementById("wishlistForm");

  if (wishlistBtn) {
    const icon = wishlistBtn.querySelector("i");
    if (icon) {
      icon.classList.toggle("fa-regular");
      icon.classList.toggle("fa-solid");
      wishlistBtn.classList.toggle("saved");
    }
  }

  if (form) {
    form.submit();
  }
}

/* ========================================================
   8. Size Modal Handlers
======================================================== */
function openSizeModal() {
  const modal = document.getElementById("sizeModal");
  if (modal) modal.classList.add("open");
}

function closeSizeModal() {
  const modal = document.getElementById("sizeModal");
  if (modal) modal.classList.remove("open");
}

window.addEventListener("click", (e) => {
  const modal = document.getElementById("sizeModal");
  if (e.target === modal) {
    closeSizeModal();
  }
});

function openFullscreenModal() {
  const mainImg = document.getElementById("mainProductImg");
  if (mainImg) {
    window.open(mainImg.src, "_blank");
  }
}