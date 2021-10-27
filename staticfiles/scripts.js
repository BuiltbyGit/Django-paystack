const paymentForm = document.getElementById('payment-wrapper');
paymentForm.addEventListener("submit", payWithPaystack, false);
function payWithPaystack(e) {
  e.preventDefault();
  let handler = PaystackPop.setup({
    key: 'pk_test_7ee106676dc9e7751bce4bf08c1d93917545aa3d', // Replace with your public key
    email: document.getElementById("email-address").value,
    amount: document.getElementById("amount").value * 100,
    ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
    // label: "Optional string that replaces customer email"
    onClose: function(){
      alert('Window closed.');
    },
    callback: function(response){
      let message = 'Payment complete! Reference: ' + response.reference;
      alert(message);

      var myEvent = {id: calEvent.id, start: calEvent.start, end: calEvent.end,
        allDay: calEvent.allDay };
      $.ajax({
      url: '/event/save-json/',
      type: 'POST',
      contentType: 'application/json; charset=utf-8',
      data: $.toJSON(myEvent),
      dataType: 'text',
      success: function(result) {
      alert(result.Result);
      }
      });

    }
  });
  handler.openIframe();
}