function formatMoney(input) {
    let value = input.value.replace(/\D/g, "");

    value = (value / 100).toFixed(2) + "";
    value = value.replace(".", ",");
    value = value.replace(/\B(?=(\d{3})+(?!\d))/g, ".");

    input.value = "R$ " + value;
}