type Last = <T>(items: T[]) => T;
const last: Last = (items) => items[items.length - 1];

type Prepend = <T>(items: T[], item: T) => T[];
const prepend: Prepend = (items, item) =>  [item, ...items]


const items = [1, 2, 3, 4, 5, 6, 7, 8];
const lastItem = last(items);
const newItems = prepend(items, 9);
console.log(lastItem, newItems);
