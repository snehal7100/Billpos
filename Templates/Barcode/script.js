document.getElementById('symbology').addEventListener('change', generateBarcode);
document.getElementById('data').addEventListener('input', generateBarcode);
document.getElementById('size').addEventListener('change', generateBarcode);

function generateBarcode() {
    const symbology = document.getElementById('symbology').value;
    const data = document.getElementById('data').value;
    const size = document.getElementById('size').value;

    document.getElementById('barcode').innerHTML = '';

    if (data.trim() === '') {
        return;
    }

    if (symbology === 'QR') {
        generateQRCode(data, size);
    } else if (symbology === 'CODE128') {
        generate1DBarcode(symbology, data, size);
    }
}

function generate1DBarcode(format, data, size) {
    const canvas = document.createElement('canvas');
    JsBarcode(canvas, data, {
        format: format,
        width: 2 * size,
        height: 100 * size,
        displayValue: true
    });
    document.getElementById('barcode').appendChild(canvas);
}

function generateQRCode(data, size) {
    const qrContainer = document.createElement('div');
    new QRCode(qrContainer, {
        text: data,
        width: 100 * size,
        height: 100 * size,
    });
    document.getElementById('barcode').appendChild(qrContainer);
}

// Initial barcode generation (optional)
generateBarcode();