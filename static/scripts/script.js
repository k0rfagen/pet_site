function searchTips() {
    const input = document.querySelector('.search-text').value;
    if (input !== '') {
        const items = document.querySelectorAll('.item');
        let finalItems = [];
        for (let i = 0; i < items.length; i++) {
            const name = items[i].querySelector('h1').innerText;
            if (name.toLowerCase().includes(input.toLowerCase())) {
                finalItems.push(name);
            }
        }
        console.log(finalItems[0]);
        if (finalItems[0]) {
            document.querySelector('.tip1').innerText = finalItems[0];
        }
        if (finalItems[1]) {
            document.querySelector('.tip2').innerText = finalItems[1];
        }
        if (finalItems[2]) {
            document.querySelector('.tip3').innerText = finalItems[2];
        }
    } else {
        document.querySelector('.tip1').innerText = '';
        document.querySelector('.tip2').innerText = '';
        document.querySelector('.tip3').innerText = '';
    }
}