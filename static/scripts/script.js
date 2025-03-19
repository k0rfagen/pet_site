const itemGrid = document.querySelector('.item-grid');
const items = document.querySelectorAll('.item');

const sortedItems0 = itemGrid.innerHTML;
const sortedItems1 = Array.from(items).sort(
        (a, b) =>
            a.dataset.price - b.dataset.price
    )
const sortedItems2 = Array.from(items).sort(
        (a, b) =>
            b.dataset.price - a.dataset.price
    )

const radio0 = document.getElementById('radio0');
const radio1 = document.getElementById('radio1');
const radio2 = document.getElementById('radio2');

const radioP = document.querySelector('.radio-p');

radio0.addEventListener('change', () => {
    itemGrid.innerHTML = sortedItems0;
    radioP.innerText = 'По умолчанию';
})

radio1.addEventListener('change', () => {
    let html = ``;
    sortedItems1.forEach((value) => {
        html += value.outerHTML;
    });
    document.querySelector('.item-grid').innerHTML = html;
    radioP.innerText = 'По возрастанию цены';
});

radio2.addEventListener('change', () => {
    let html = ``;
    sortedItems2.forEach((value) => {
        html += value.outerHTML;
    });
    document.querySelector('.item-grid').innerHTML = html;
    radioP.innerText = 'По убыванию цены';
});


function searchTips() {
    const input = document.querySelector('.search-text').value;
    if (input !== '') {
        let finalItems = [];
        for (let i = 0; i < items.length; i++) {
            const name = items[i].querySelector('h1').innerText;
            if (name.toLowerCase().includes(input.toLowerCase())) {
                finalItems.push(name);
            }
        }
        if (finalItems.length > 0) {
            if (finalItems[0]) {
                document.querySelector('.tip1').innerText = finalItems[0];
                document.querySelector('.tip2').innerText = '';
                document.querySelector('.tip3').innerText = '';
            }
            if (finalItems[1]) {
                document.querySelector('.tip2').innerText = finalItems[1];
                document.querySelector('.tip3').innerText = '';
            }
            if (finalItems[2]) {
                document.querySelector('.tip3').innerText = finalItems[2];
            }
        } else {
            document.querySelector('.tip1').innerText = '';
            document.querySelector('.tip2').innerText = '';
            document.querySelector('.tip3').innerText = '';
        }
    } else {
        document.querySelector('.tip1').innerText = '';
        document.querySelector('.tip2').innerText = '';
        document.querySelector('.tip3').innerText = '';
    }
}