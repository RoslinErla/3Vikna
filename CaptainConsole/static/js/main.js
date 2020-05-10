jQuery(function($) {
 var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
  $('ul a').each(function() {
  if (this.href === path) {
   console.log(this)
   $(this).addClass('active');
  }
 });
});

let itemRemover = document.getElementsByClassName('remove-button')
for (let i = 0; i <itemRemover.length; i++) {
 let button = itemRemover[i]
 button.addEventListener('click', cartItemRemover)
}

    let inputsToItemQuantity = document.getElementsByClassName('cart-quantity')
    for (let i = 0; i < inputsToItemQuantity.length; i++) {
        let input = inputsToItemQuantity[i]
        input.addEventListener('change', changingQuantity)
    }

let itemToCartButton = document.getElementsByClassName('add-to-cart-btn')
for (let i = 0; i <itemToCartButton.length; i++) {
    let button = itemToCartButton[i]
    button.addEventListener('click', cartAddClick)
}

function cartAddClick(event){
    let button = event.target
    let singleProductList = button.id.split(",")
    console.log(singleProductList)
    let productName = singleProductList[1]
    let productPrice = singleProductList[2]
    let productImgSrc = singleProductList[3]
    console.log(productName, productPrice, productImgSrc)
    moveItemToCart(productName, productPrice, productImgSrc)
}

//function moveItemToCart(productName, productPrice, productImgSrc){
//    localStorage.setItem('product-name', productName)
//    console.log(localStorage)
//}
function moveItemToCart(productName, productPrice, productImgSrc){
    let newItem = document.createElement('div')
    newItem.classList.add('all-items')
    //let itemsInCart = document.getElementsByClassName('all-items')[0]
    let cartRowContents = `
        <div class="cart-item-info">
        <img class="cart-item-image" src="${productImgSrc}" width="100" height="100">
        &emsp;
        <p class="cart-item-title">${productName}</p>
        &emsp;
        <span class="price">${productPrice}</span>
        &emsp;
        <input class="cart-quantity" type="number" value="1">
        &emsp;
        <button class="remove-button" type="button">X</button>
        </div>`
    newItem.innerHTML = cartRowContents
    console.log(newItem)
    document.getElementsByClassName('all-items')[0].append(newItem)
}

function changingQuantity(event) {
    let input = event.target
    if(isNaN(input.value) || input.value <=0){
        input.value = 1
    }
    if(isNaN(input.value) || 5 < input.value){
        input.value = 5
    }
    updateTotal()
}

function cartItemRemover(event){
  let onClick = event.target
  onClick.parentElement.remove()
  updateTotal()
}

function updateTotal() {
 let allItems = document.getElementsByClassName('all-items')[0]
 let singleItems = allItems.getElementsByClassName('cart-item-info')
 let total = 0
 for (let i = 0; i < singleItems.length; i++) {
   let singleItem = singleItems[i]
   let itemPrice = singleItem.getElementsByClassName('price')[0]
   let itemQuantity = singleItem.getElementsByClassName('cart-quantity')[0]
   console.log(itemPrice,itemQuantity)
   let price = parseFloat(itemPrice.innerText.replace('isk', ''))
   console.log(price)
   let numberQuantity = itemQuantity.value
   total = total + (price * numberQuantity)
 }
 total = Math.round(total * 100) / 100
 document.getElementsByClassName('total-price')[0].innerText = total + 'isk'
}
