
function payWithPaystack(e) {

    e.preventDefault();

    let handler = PaystackPop.setup({
        key: 'pk_live_b6ecc2c0884739c40d0797efc4f0f7387ac3e9aa', // Replace with your public key
        amount: parseFloat(total).toFixed(2),
        ref: "" + Math.floor(Math.random() * 1000000000 + 1), 
        onClose: function () {
            alert("Window closed.");
        },
        callback: function (response) {
            let message = "Payment complete! Reference: " + response.reference;
            alert(message);
        },
    });

    handler.openIframe();
}
