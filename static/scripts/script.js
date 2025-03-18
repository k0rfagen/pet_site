const itemGrid = document.querySelector('.item-grid');
const items = Array.from(document.querySelectorAll('.item'));

const btn1 = document.querySelector('.btn1');
const btn2 = document.querySelector('.btn2');

btn1.addEventListener('click', () => {
    console.log(items);
    items.sort();
    let html = '';
    items.forEach(() => {
        html += `
            <div class="item">
                <div class="item-img">
                    <a href="{% url 'item_card' item.id %}">
                        <img src="{{ item.image.url }}" alt="">
                    </a>
                </div>
                <div class="item-info">
                    <div>
                        <h1>{{ item.name }}</h1>
                        <h2>{{ item.price }} ₽</h2>
                    </div>
                    <div>
                        <form method="post" action="{% url 'add_to_cart' item.id %}">
                            {% csrf_token  %}
                            <button type="submit">buy</button>
                        </form>
                    </div>
                </div>
            </div>
        `
    });
    itemGrid.innerHTML = html;
});

btn2.addEventListener('click', () => {
    items.sort((a, b) => b - a);
    let html = '';
    items.forEach(() => {
        html += `
            <div class="item">
                <div class="item-img">
                    <a href="{% url 'item_card' item.id %}">
                        <img src="{{ item.image.url }}" alt="">
                    </a>
                </div>
                <div class="item-info">
                    <div>
                        <h1>{{ item.name }}</h1>
                        <h2>{{ item.price }} ₽</h2>
                    </div>
                    <div>
                        <form method="post" action="{% url 'add_to_cart' item.id %}">
                            {% csrf_token  %}
                            <button type="submit">buy</button>
                        </form>
                    </div>
                </div>
            </div>
        `
    });
    itemGrid.innerHTML = html;
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