
document.addEventListener("DOMContentLoaded", function () {

    const packageBox = document.getElementById("package");
    const truck = document.getElementById("deliveryTruck");
    const truckDoor = document.getElementById("truckDoor");

    const loadingText = document.getElementById("loadingText");

    const statusPreparing =
        document.getElementById("statusPreparing");

    const statusLoading =
        document.getElementById("statusLoading");

    const statusTransit =
        document.getElementById("statusTransit");

    const connectorOne =
        document.getElementById("connectorOne");

    const connectorTwo =
        document.getElementById("connectorTwo");

    const finalSuccess =
        document.getElementById("finalSuccess");


    /* =====================================================
       STEP 1
       Order is ready
    ===================================================== */

    setTimeout(function () {

        loadingText.textContent =
            "Loading your order into the truck...";

        statusLoading.classList.add("active");

        connectorOne.classList.add("active");

    }, 1800);


    /* =====================================================
       STEP 2
       Package moves into truck
    ===================================================== */

    setTimeout(function () {

        /*
        Move package toward truck
        */

        packageBox.style.left = "52%";

        packageBox.style.bottom = "150px";

        packageBox.style.transform =
            "scale(0.55)";

    }, 2600);


    /* =====================================================
       STEP 3
       Package disappears inside truck
    ===================================================== */

    setTimeout(function () {

        packageBox.style.opacity = "0";

        truckDoor.style.opacity = "1";

        loadingText.textContent =
            "Order loaded successfully";

    }, 4200);


    /* =====================================================
       STEP 4
       Loading completed
    ===================================================== */

    setTimeout(function () {

        statusLoading.classList.remove("active");

        statusLoading.classList.add("completed");

        statusTransit.classList.add("active");

        connectorTwo.classList.add("active");

        loadingText.textContent =
            "Your order is on the way...";

    }, 5000);


    /* =====================================================
       STEP 5
       TRUCK STARTS RUNNING
    ===================================================== */

    setTimeout(function () {

        truck.style.left = "120%";

        loadingText.textContent =
            "Order in transit...";

    }, 5600);


    /* =====================================================
       STEP 6
       Truck completes journey
    ===================================================== */

    setTimeout(function () {

        statusTransit.classList.remove("active");

        statusTransit.classList.add("completed");

        loadingText.style.opacity = "0";

    }, 10000);


    /* =====================================================
       STEP 7
       FINAL CONFIRMATION
    ===================================================== */

    setTimeout(function () {

        finalSuccess.classList.add("show");

    }, 10600);


});

