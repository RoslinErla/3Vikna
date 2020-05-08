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
