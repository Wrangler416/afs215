class Discount {
    constructor(item, discount){
        this.item = item
        this.discount = discount

    }
}
class Item {
    constructor(item, price){
        this.item = item
        this.price = price
    }
}
class Checkout {
    constructor(){
        this.items = []
        this.discounts = []
    }

    addItem(item){
        this.items.push(item)
        return this.items
    }

    addPrice(item, price){
        this.items
    }

    addDiscount(dis) {
        this.addDiscount.push(dis)
        return this.addDiscount
    }
}

export {Checkout, Item, Discount}

