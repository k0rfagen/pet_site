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

const tips = document.querySelector('.search-tips');
const input = document.querySelector('.search-text');

const radio0 = document.getElementById('radio0');
const radio1 = document.getElementById('radio1');
const radio2 = document.getElementById('radio2');

const radioP = document.querySelector('.radio-p');

radio0.addEventListener('change', () => {
    itemGrid.innerHTML = sortedItems0;
    radioP.innerText = 'По умолчанию';
});

radio1.addEventListener('change', () => {
    let html = ``;
    sortedItems1.forEach((value) => {
        html += value.outerHTML;
    });
    itemGrid.innerHTML = html;
    radioP.innerText = 'По возрастанию цены';
});

radio2.addEventListener('change', () => {
    let html = ``;
    sortedItems2.forEach((value) => {
        html += value.outerHTML;
    });
    itemGrid.innerHTML = html;
    radioP.innerText = 'По убыванию цены';
});

function searchTips() {
    const inputValue = input.value;
    let tipHTML = '';
    if (inputValue !== '') {
        let finalItems = [];
        let finalUrl = [];
        for (let i = 0; i < items.length; i++) {
            const item = items[i];
            const name = item.querySelector('h1').innerText;
            if (name.toLowerCase().includes(inputValue.toLowerCase())) {
                finalItems.push(name);
                finalUrl.push(item.dataset.url);
            }
        }
        console.log(finalItems);
        console.log(finalUrl);
        if (finalItems.length > 0) {
            tipHTML += `
            <div>
                <img src="/media/media/images/search.svg">
                <a href="${finalUrl[0]}">
                ${finalItems[0]}</a>
            </div>
            `;
        }
        if (finalItems.length > 1) {
            tipHTML += `
            <div>
                <img src="/media/media/images/search.svg">
                <a href="${finalUrl[1]}">
                ${finalItems[1]}</a>
            </div>
            `
        }
        if (finalItems.length > 2) {
            tipHTML += `
            <div>
                <img src="/media/media/images/search.svg">
                <a href="${finalUrl[2]}">
                ${finalItems[2]}</a>
            </div>
            `;
        }
    }
    tips.innerHTML = tipHTML;
}