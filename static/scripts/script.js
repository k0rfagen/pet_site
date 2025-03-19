const items = document.querySelectorAll('.item');;

const btn1 = document.querySelector('.btn1');
const btn2 = document.querySelector('.btn2');

btn1.addEventListener('click', () => {
    const sortedItems = Array.from(items).sort(
        (a, b) =>
            a.dataset.price - b.dataset.price
    )
    let html = ``;
    sortedItems.forEach((value) => {
        html += value.outerHTML;
    });
    document.querySelector('.item-grid').innerHTML = html;
});
btn2.addEventListener('click', () => {
    const sortedItems = Array.from(items).sort(
        (a, b) =>
            b.dataset.price - a.dataset.price
    )
    let html = ``;
    sortedItems.forEach((value) => {
        html += value.outerHTML;
    });
    document.querySelector('.item-grid').innerHTML = html;
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