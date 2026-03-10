function formatSeat(input, totalSeats) {

    // remove tudo que não for letra ou número
    let value = input.value.replace(/[^a-zA-Z0-9]/g, "");

    // separa letra e número
    let letter = value.replace(/[^a-zA-Z]/g, "").toUpperCase().slice(0, 1);
    let number = value.replace(/[^0-9]/g, "").slice(0, 2);

    // calcula quantidade de linhas baseado nos assentos
    const columns = 6; // A-F padrão
    const rows = Math.ceil(totalSeats / columns);

    // limitar letra (A-F)
    if (letter) {
        const maxLetter = String.fromCharCode(65 + columns - 1);
        if (letter > maxLetter) {
            letter = maxLetter;
        }
    }

    // limitar número de linha
    if (number) {
        let num = parseInt(number);

        if (num > rows) {
            num = rows;
        }

        number = num.toString().padStart(2, "0");
    }

    input.value = letter + number;
}