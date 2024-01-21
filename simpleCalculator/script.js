let currentInput = "";

function display(value) {
    currentInput += value;
    document.getElementById('display').value = currentInput;
}

function clearDisplay() {
    currentInput = "";
    document.getElementById('display').value = "0";
}

function deleteLast() {
    currentInput = currentInput.slice(0, -1);
    document.getElementById('display').value = currentInput;
}

function calculate() {
    try {
        let result = eval(currentInput);
        currentInput = result.toString();
        document.getElementById('display').value = result;
    } catch (e) {
        alert('Invalid expression');
        clearDisplay();
    }
}

document.addEventListener('keydown', function(event) {
    const key = event.key;
    if (key === 'Enter') {
        event.preventDefault();
        calculate();
    } else if (key === 'Backspace') {
        event.preventDefault();
        deleteLast();
    } else if (/[\d+\-*/.]/.test(key)) {
        event.preventDefault();
        display(key);
    }
});
