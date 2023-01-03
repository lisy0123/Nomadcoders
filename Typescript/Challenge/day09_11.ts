/**
 * @see [source](https://github.com/lodash/lodash/blob/master/head.js)
 * @see [source](https://github.com/lodash/lodash/blob/master/hasIn.js)
 * @see [source](https://github.com/lodash/lodash/blob/master/isBoolean.js)
 * @see [source](https://github.com/lodash/lodash/blob/master/toString.js)
 * @see [source](https://github.com/lodash/lodash/blob/master/split.js)
 * @see [source](https://github.com/lodash/lodash/blob/master/hasPath.js)
 * @see [source](https://github.com/lodash/lodash/blob/master/filter.js)
 * @see [source](https://github.com/lodash/lodash/blob/master/every.js)
 * @see [source](map.js: https://github.com/lodash/lodash/blob/master/map.js)
 */


declare module "lodash" {
    function head(array: Array<any>): any | undefined
    function hasIn(object: Object, key: string): boolean
    function isBoolean(value: any): boolean
    function toString(value: any): string
    function split(str: string, separator: RegExp | string, limit: number): Array<string>
    function hasPath(object: Object, path: Array<any> | string): boolean
    function filter(array: Array<any>, predicate: Function): Array<any>
    function every(array: Array<any>, predicate: Function): boolean
    function map(array: Array<any>, predicate: Function): Array<any>
}
