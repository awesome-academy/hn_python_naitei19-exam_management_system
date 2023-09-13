jQuery(document).ready(function ($) {
  $("#sidebarToggle").on("click", function (event) {
    event.preventDefault();
    $("body").toggleClass("sb-sidenav-toggled");
  });

  $(".close").on("click", function (event) {
    event.preventDefault();
    $(".message-toast").remove();
  });

  $("#registration-form").on("submit", function (e) {
    e.preventDefault();
    var formData = $(this).serialize();
    var registrationUrl = $(this).data("registration-url");

    $.ajax({
      url: registrationUrl,
      type: "POST",
      data: formData,
      success: function (data) {
        $("#registration-status").html(data.message);
        $("#enroll-button").prop("disabled", true);
        $("#enroll-button").text("Enrolled");
      },
      error: function () {
        $("#registration-status").html("An error occurred.");
      },
    });
  });
  const countdownElement = $("#countdown");
  let remainingTime = countdownElement.data("remaining-seconds");
  let intTime = parseInt(remainingTime);
  function submitExamAndRedirect() {
    $("#countdown").text("Countdown expired");
    // Automatically submit the exam form
    $("#exam-form").submit();
  }
  updateCountdown = function () {
    if (intTime > 0) {
      const minutes = Math.floor(intTime / 60);
      const seconds = intTime % 60;
      countdownElement.text(`${minutes}:${seconds < 10 ? "0" : ""}${seconds}`);
      --intTime;
      setTimeout(updateCountdown, 1000);
    } else {
      submitExamAndRedirect();
    }
  };
  updateCountdown();
});
