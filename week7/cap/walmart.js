class Discounts {
    constructor(unit, discount) {
        this.unit = unit
        this.discount = discount
    }
}
class Item {
    constructor(item, price) {
        this.item = item
        this.price = price
    }
}
class Checkout {
    constructor() {
        this.items = []
        this.discounts = []
    }

    addItem(item) {

        this.items.push(item)
        return this.items
        
    }
    getTotal() {
        let total = 0
        this.items.forEach(item => {
            total += item.price
        });
        return total
    }

    addDiscount(discount) {
        this.discounts.push(discount)
        return this.discounts
    }

}

export { Checkout, Item, Discounts }