export function print(...args) {
    console.log(...args)
}

export function warning(...args) {
    console.error(...args)
}

export function input(message) {
    return prompt(message)
}

global.input = input
global.print = print
global.warning = warning
